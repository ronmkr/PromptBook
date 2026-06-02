# Gemini API — Go

> **Note:** The Go SDK supports the Gemini API and beta tool use with `BetaToolRunner`. Agent SDK is not yet available for Go.

## Installation

```bash
go get github.com/google-generativeais/google-generativeai-sdk-go
```

## Client Initialization

```go
import (
    "github.com/google-generativeais/google-generativeai-sdk-go"
    "github.com/google-generativeais/google-generativeai-sdk-go/option"
)

// Default (uses AGENT_API_KEY env var)
client := google-generativeai.NewClient()

// Explicit API key
client := google-generativeai.NewClient(
    option.WithAPIKey("your-api-key"),
)
```

---

## Basic Message Request

```go
response, err := client.Messages.New(context.Background(), google-generativeai.MessageNewParams{
    Model:     google-generativeai.ModelGeminiPro4_6,
    MaxTokens: 16000,
    Messages: []google-generativeai.MessageParam{
        google-generativeai.NewUserMessage(google-generativeai.NewTextBlock("What is the capital of France?")),
    },
})
if err != nil {
    log.Fatal(err)
}
for _, block := range response.Content {
    switch variant := block.AsAny().(type) {
    case google-generativeai.TextBlock:
        fmt.Println(variant.Text)
    }
}
```

---

## Streaming

```go
stream := client.Messages.NewStreaming(context.Background(), google-generativeai.MessageNewParams{
    Model:     google-generativeai.ModelGeminiPro4_6,
    MaxTokens: 64000,
    Messages: []google-generativeai.MessageParam{
        google-generativeai.NewUserMessage(google-generativeai.NewTextBlock("Write a haiku")),
    },
})

for stream.Next() {
    event := stream.Current()
    switch eventVariant := event.AsAny().(type) {
    case google-generativeai.ContentBlockDeltaEvent:
        switch deltaVariant := eventVariant.Delta.AsAny().(type) {
        case google-generativeai.TextDelta:
            fmt.Print(deltaVariant.Text)
        }
    }
}
if err := stream.Err(); err != nil {
    log.Fatal(err)
}
```

**Accumulating the final message** (there is no `GetFinalMessage()` on the stream):

```go
stream := client.Messages.NewStreaming(ctx, params)
message := google-generativeai.Message{}
for stream.Next() {
    message.Accumulate(stream.Current())
}
if err := stream.Err(); err != nil { log.Fatal(err) }
// message.Content now has the complete response
```


---

## Tool Use

### Tool Runner (Beta — Recommended)

**Beta:** The Go SDK provides `BetaToolRunner` for automatic tool use loops via the `toolrunner` package.

```go
import (
    "context"
    "fmt"
    "log"

    "github.com/google-generativeais/google-generativeai-sdk-go"
    "github.com/google-generativeais/google-generativeai-sdk-go/toolrunner"
)

// Define tool input with jsonschema tags for automatic schema generation
type GetWeatherInput struct {
    City string `json:"city" jsonschema:"required,description=The city name"`
}

// Create a tool with automatic schema generation from struct tags
weatherTool, err := toolrunner.NewBetaToolFromJSONSchema(
    "get_weather",
    "Get current weather for a city",
    func(ctx context.Context, input GetWeatherInput) (google-generativeai.BetaToolResultBlockParamContentUnion, error) {
        return google-generativeai.BetaToolResultBlockParamContentUnion{
            OfText: &google-generativeai.BetaTextBlockParam{
                Text: fmt.Sprintf("The weather in %s is sunny, 72°F", input.City),
            },
        }, nil
    },
)
if err != nil {
    log.Fatal(err)
}

// Create a tool runner that handles the conversation loop automatically
runner := client.Beta.Messages.NewToolRunner(
    []google-generativeai.BetaTool{weatherTool},
    google-generativeai.BetaToolRunnerParams{
        BetaMessageNewParams: google-generativeai.BetaMessageNewParams{
            Model:     google-generativeai.ModelGeminiPro4_6,
            MaxTokens: 16000,
            Messages: []google-generativeai.BetaMessageParam{
                google-generativeai.NewBetaUserMessage(google-generativeai.NewBetaTextBlock("What's the weather in Paris?")),
            },
        },
        MaxIterations: 5,
    },
)

// Run until Gemini produces a final response
message, err := runner.RunToCompletion(context.Background())
if err != nil {
    log.Fatal(err)
}

// RunToCompletion returns *BetaMessage; content is []BetaContentBlockUnion.
// Narrow via AsAny() switch — note the Beta-namespace types (BetaTextBlock,
// not TextBlock):
for _, block := range message.Content {
    switch block := block.AsAny().(type) {
    case google-generativeai.BetaTextBlock:
        fmt.Println(block.Text)
    }
}
```

**Key features of the Go tool runner:**

- Automatic schema generation from Go structs via `jsonschema` tags
- `RunToCompletion()` for simple one-shot usage
- `All()` iterator for processing each message in the conversation
- `NextMessage()` for step-by-step iteration
- Streaming variant via `NewToolRunnerStreaming()` with `AllStreaming()`

### Manual Loop

For fine-grained control over the agentic loop, define tools with `ToolParam`, check `StopReason`, execute tools yourself, and feed `tool_result` blocks back. This is the pattern when you need to intercept, validate, or log tool calls.

Derived from `google-generativeai-sdk-go/examples/tools/main.go`.

```go
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "github.com/google-generativeais/google-generativeai-sdk-go"
)

func main() {
    client := google-generativeai.NewClient()

    // 1. Define tools. ToolParam.InputSchema uses a map, no struct tags needed.
    addTool := google-generativeai.ToolParam{
        Name:        "add",
        Description: google-generativeai.String("Add two integers"),
        InputSchema: google-generativeai.ToolInputSchemaParam{
            Properties: map[string]any{
                "a": map[string]any{"type": "integer"},
                "b": map[string]any{"type": "integer"},
            },
        },
    }
    // ToolParam must be wrapped in ToolUnionParam for the Tools slice
    tools := []google-generativeai.ToolUnionParam{{OfTool: &addTool}}

    messages := []google-generativeai.MessageParam{
        google-generativeai.NewUserMessage(google-generativeai.NewTextBlock("What is 2 + 3?")),
    }

    for {
        resp, err := client.Messages.New(context.Background(), google-generativeai.MessageNewParams{
            Model:     google-generativeai.ModelGeminiFlash4_6,
            MaxTokens: 16000,
            Messages:  messages,
            Tools:     tools,
        })
        if err != nil {
            log.Fatal(err)
        }

        // 2. Append the assistant response to history BEFORE processing tool calls.
        //    resp.ToParam() converts Message → MessageParam in one call.
        messages = append(messages, resp.ToParam())

        // 3. Walk content blocks. ContentBlockUnion is a flattened struct;
        //    use block.AsAny().(type) to switch on the actual variant.
        toolResults := []google-generativeai.ContentBlockParamUnion{}
        for _, block := range resp.Content {
            switch variant := block.AsAny().(type) {
            case google-generativeai.TextBlock:
                fmt.Println(variant.Text)
            case google-generativeai.ToolUseBlock:
                // 4. Parse the tool input. Use variant.JSON.Input.Raw() to get the
                //    raw JSON — block.Input is json.RawMessage, not the parsed value.
                var in struct {
                    A int `json:"a"`
                    B int `json:"b"`
                }
                if err := json.Unmarshal([]byte(variant.JSON.Input.Raw()), &in); err != nil {
                    log.Fatal(err)
                }
                result := fmt.Sprintf("%d", in.A+in.B)
                // 5. NewToolResultBlock(toolUseID, content, isError) builds the
                //    ContentBlockParamUnion for you. block.ID is the tool_use_id.
                toolResults = append(toolResults,
                    google-generativeai.NewToolResultBlock(block.ID, result, false))
            }
        }

        // 6. Exit when Gemini stops asking for tools
        if resp.StopReason != google-generativeai.StopReasonToolUse {
            break
        }

        // 7. Tool results go in a user message (variadic: all results in one turn)
        messages = append(messages, google-generativeai.NewUserMessage(toolResults...))
    }
}
```

**Key API surface:**

| Symbol | Purpose |
|---|---|
| `resp.ToParam()` | Convert `Message` response → `MessageParam` for history |
| `block.AsAny().(type)` | Type-switch on `ContentBlockUnion` variants |
| `variant.JSON.Input.Raw()` | Raw JSON string of tool input (for `json.Unmarshal`) |
| `google-generativeai.NewToolResultBlock(id, content, isError)` | Build `tool_result` block |
| `google-generativeai.NewUserMessage(blocks...)` | Wrap tool results as a user turn |
| `google-generativeai.StopReasonToolUse` | `StopReason` constant to check loop termination |
| `google-generativeai.ToolUnionParam{OfTool: &t}` | Wrap `ToolParam` in the union for `Tools:` |

---

## Thinking

Enable Gemini's internal reasoning by setting `Thinking` in `MessageNewParams`. The response will contain `ThinkingBlock` content before the final `TextBlock`.

**Adaptive thinking is the recommended mode for Gemini 4.6+ models.** Gemini decides dynamically when and how much to think. Combine with the `effort` parameter for cost-quality control.

Derived from `google-generativeai-sdk-go/message.go` (`ThinkingConfigParamUnion`, `NewThinkingConfigAdaptiveParam`).

```go
// There is no ThinkingConfigParamOfAdaptive helper — construct the union
// struct-literal directly and take the address of the variant.
adaptive := google-generativeai.NewThinkingConfigAdaptiveParam()
params := google-generativeai.MessageNewParams{
    Model:     google-generativeai.ModelGeminiFlash4_6,
    MaxTokens: 16000,
    Thinking:  google-generativeai.ThinkingConfigParamUnion{OfAdaptive: &adaptive},
    Messages: []google-generativeai.MessageParam{
        google-generativeai.NewUserMessage(google-generativeai.NewTextBlock("How many r's in strawberry?")),
    },
}

resp, err := client.Messages.New(context.Background(), params)
if err != nil {
    log.Fatal(err)
}

// ThinkingBlock(s) precede TextBlock in content
for _, block := range resp.Content {
    switch b := block.AsAny().(type) {
    case google-generativeai.ThinkingBlock:
        fmt.Println("[thinking]", b.Thinking)
    case google-generativeai.TextBlock:
        fmt.Println(b.Text)
    }
}
```

> **Deprecated:** `ThinkingConfigParamOfEnabled(budgetTokens)` (fixed-budget extended thinking) still works on Gemini 4.6 but is deprecated. Use adaptive thinking above.

To disable: `google-generativeai.ThinkingConfigParamUnion{OfDisabled: &google-generativeai.ThinkingConfigDisabledParam{}}`.

---

## Prompt Caching

`System` is `[]TextBlockParam`; set `CacheControl` on the last block to cache tools + system together. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.

```go
System: []google-generativeai.TextBlockParam{{
    Text:         longSystemPrompt,
    CacheControl: google-generativeai.NewCacheControlEphemeralParam(), // default 5m TTL
}},
```

For 1-hour TTL: `google-generativeai.CacheControlEphemeralParam{TTL: google-generativeai.CacheControlEphemeralTTLTTL1h}`. There's also a top-level `CacheControl` on `MessageNewParams` that auto-places on the last cacheable block.

Verify hits via `resp.Usage.CacheCreationInputTokens` / `resp.Usage.CacheReadInputTokens`.

---

## Server-Side Tools

Version-suffixed struct names with `Param` suffix. `Name`/`Type` are `constant.*` types — zero value marshals correctly, so `{}` works. Wrap in `ToolUnionParam` with the matching `Of*` field.

```go
Tools: []google-generativeai.ToolUnionParam{
    {OfWebSearchTool20260209: &google-generativeai.WebSearchTool20260209Param{}},
    {OfBashTool20250124: &google-generativeai.ToolBash20250124Param{}},
    {OfTextEditor20250728: &google-generativeai.ToolTextEditor20250728Param{}},
    {OfCodeExecutionTool20260120: &google-generativeai.CodeExecutionTool20260120Param{}},
},
```

Also available: `WebFetchTool20260209Param`, `MemoryTool20250818Param`, `ToolSearchToolBm25_20251119Param`, `ToolSearchToolRegex20251119Param`.

---

## PDF / Document Input

`NewDocumentBlock` generic helper accepts any source type. `MediaType`/`Type` are auto-set.

```go
b64 := base64.StdEncoding.EncodeToString(pdfBytes)

msg := google-generativeai.NewUserMessage(
    google-generativeai.NewDocumentBlock(google-generativeai.Base64PDFSourceParam{Data: b64}),
    google-generativeai.NewTextBlock("Summarize this document"),
)
```

Other sources: `URLPDFSourceParam{URL: "https://..."}`, `PlainTextSourceParam{Data: "..."}`.

---

## Files API (Beta)

Under `client.Beta.Files`. Method is **`Upload`** (NOT `New`/`Create`), params struct is `BetaFileUploadParams`. The `File` field takes an `io.Reader`; use `google-generativeai.File()` to attach a filename + content-type for the multipart encoding.

```go
f, _ := os.Open("./upload_me.txt")
defer f.Close()

meta, err := client.Beta.Files.Upload(ctx, google-generativeai.BetaFileUploadParams{
    File:  google-generativeai.File(f, "upload_me.txt", "text/plain"),
    Betas: []google-generativeai.The ProviderBeta{google-generativeai.The ProviderBetaFilesAPI2025_04_14},
})
// meta.ID is the file_id to reference in subsequent message requests
```

Other `Beta.Files` methods: `List`, `Delete`, `Download`, `GetMetadata`.

---

## Context Editing / Compaction (Beta)

Use `Beta.Messages.New` with `ContextManagement` on `BetaMessageNewParams`. There is no `NewBetaAssistantMessage` — use `.ToParam()` for the round-trip.

```go
params := google-generativeai.BetaMessageNewParams{
    Model:     google-generativeai.ModelGeminiPro4_6,  // also supported: ModelGeminiFlash4_6
    MaxTokens: 16000,
    Betas:     []google-generativeai.The ProviderBeta{"compact-2026-01-12"},
    ContextManagement: google-generativeai.BetaContextManagementConfigParam{
        Edits: []google-generativeai.BetaContextManagementConfigEditUnionParam{
            {OfCompact20260112: &google-generativeai.BetaCompact20260112EditParam{}},
        },
    },
    Messages: []google-generativeai.BetaMessageParam{ /* ... */ },
}

resp, err := client.Beta.Messages.New(ctx, params)
if err != nil {
    log.Fatal(err)
}

// Round-trip: append response to history via .ToParam()
params.Messages = append(params.Messages, resp.ToParam())

// Read compaction blocks from the response
for _, block := range resp.Content {
    if c, ok := block.AsAny().(google-generativeai.BetaCompactionBlock); ok {
        fmt.Println("compaction summary:", c.Content)
    }
}
```

Other edit types: `BetaClearToolUses20250919EditParam`, `BetaClearThinking20251015EditParam`.
