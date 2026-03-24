import os
import datetime
import re
import sys

# Add current directory to path so we can import our package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from promptbook import core  # noqa: E402

README_FILE = "README.md"
GEMINI_FILE = "GEMINI.md"
CATALOG_DIR = "docs/catalog"
FULL_CATALOG_FILE = "docs/FULL_CATALOG.md"


def get_prompts():
    """Wrapper around core.get_prompts to match the expected format for this script."""
    return core.get_prompts()


def generate_domain_markdown(tag_name, display_name, prompts):
    content = [
        f"# 📖 promptbook - {display_name} Catalog\n\n",
        f"Generated on: {datetime.date.today().isoformat()}\n\n",
        f"This catalog contains the reference for all **{display_name}** templates.\n\n",
        "## 📑 Table of Contents\n",
    ]

    for p in prompts:
        anchor = p["display_name"].lower().replace(":", "").replace(" ", "-")
        content.append(f"- [{p['display_name']}](#{anchor})\n")

    content.append("\n---\n\n")

    for p in prompts:
        content.extend(
            [
                f"### {p['display_name']}\n\n",
                f"> **Description**: {p['description']}\n",
                f"> **Input Needed**: `{p['args_description']}`\n",
                f"> **Version**: `{p['version']}` | **Last Updated**: `{p['last_updated']}`\n",
                f"> **Tags**: {', '.join([f'`{t}`' for t in p['tags']])}\n\n",
                "<details>\n",
                "<summary>Click to view template content</summary>\n\n",
                "````markdown\n",
                p["prompt"] + "\n",
                "````\n",
                "</details>\n\n",
                "---\n\n",
            ]
        )

    os.makedirs(CATALOG_DIR, exist_ok=True)
    # Sanitize filename: replace spaces, slashes, and ampersands
    filename = tag_name.lower().replace(" ", "-").replace("&", "and").replace("/", "-")
    filename = re.sub(r"-+", "-", filename)  # Remove double dashes
    filename += ".md"
    filepath = os.path.join(CATALOG_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(content)

    return filename


def generate_full_catalog(prompts):
    content = [
        "# 📚 Full promptbook Catalog\n\n",
        f"Generated on: {datetime.date.today().isoformat()}\n\n",
        "This file contains every template available in the library for exhaustive reference and search.\n\n",
        "## 📑 All Prompts\n\n",
    ]

    for p in sorted(prompts, key=lambda x: x["display_name"]):
        content.extend(
            [
                f"### {p['display_name']}\n\n",
                f"> {p['description']}\n\n",
                "<details>\n",
                "<summary>Metadata & Template</summary>\n\n",
                f"- **Input**: `{p['args_description']}`\n",
                f"- **Version**: `{p['version']}`\n",
                f"- **Tags**: {', '.join([f'`{t}`' for t in p['tags']])}\n\n",
                "````markdown\n",
                p["prompt"] + "\n",
                "````\n",
                "</details>\n\n",
                "---\n\n",
            ]
        )

    os.makedirs(os.path.dirname(FULL_CATALOG_FILE), exist_ok=True)
    with open(FULL_CATALOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(content)


def generate_catalog_index(domains):
    content = [
        "# 📂 Domain Catalogs\n\n",
        "Explore our curated collection of prompts organized by domain.\n\n",
        "| Domain | Description | Link |\n",
        "|---|---|---|\n",
    ]

    for domain_name, config in domains.items():
        if "filename" in config:
            count = len(config.get("prompts", []))
            content.append(
                f"| **{domain_name}** | {count} templates | [View Catalog]({config['filename']}) |\n"
            )

    content.append("\n\n---\n[← Back to Main README](../../README.md)")

    filepath = os.path.join(CATALOG_DIR, "README.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(content)


def update_docs(prompts):
    # Domain configuration for both README and Gemini
    domains = {
        "Code Review & Analysis": {"tags": ["code-review", "debug"], "links": []},
        "DevOps & Infrastructure": {"tags": ["devops", "infra"], "links": []},
        "Security & Compliance": {"tags": ["security"], "links": []},
        "Database & Data Engineering": {"tags": ["db"], "links": []},
        "Testing & Debugging": {"tags": ["test", "debug"], "links": []},
        "UI / UX & Frontend": {"tags": ["frontend"], "links": []},
        "Architecture & Design": {"tags": ["architecture"], "links": []},
        "Shell & Scripting": {"tags": ["shell"], "links": []},
        "Project Management & Agile": {"tags": ["agile"], "links": []},
        "Documentation & Learning": {
            "tags": ["docs", "learning", "writing"],
            "links": [],
        },
    }

    # 1. Generate Domain Markdown Files
    for domain_name, config in domains.items():
        domain_prompts = [
            p for p in prompts if any(t in p["tags"] for t in config["tags"])
        ]
        if domain_prompts:
            # Deduplicate by display_name
            seen = set()
            unique_prompts = []
            for p in domain_prompts:
                if p["display_name"] not in seen:
                    unique_prompts.append(p)
                    seen.add(p["display_name"])

            nb_filename = generate_domain_markdown(
                domain_name,
                domain_name,
                sorted(unique_prompts, key=lambda x: x["display_name"]),
            )
            config["filename"] = nb_filename
            config["prompts"] = sorted(unique_prompts, key=lambda x: x["display_name"])

    # 2. Generate Full Catalog
    generate_full_catalog(prompts)

    # 3. Generate Catalog Index
    generate_catalog_index(domains)

    # 4. Update GEMINI.md
    if os.path.exists(GEMINI_FILE):
        with open(GEMINI_FILE, "r", encoding="utf-8") as f:
            gemini_content = f.read()

        gemini_list = "## Available Prompts\n"
        for domain_name, config in domains.items():
            if "prompts" in config:
                gemini_list += f"### {domain_name}\n"
                for p in config["prompts"]:
                    gemini_list += f"- `/prompts:{p['display_name']}`: {p['description'].rstrip('.')}\n"

        gemini_pattern = r"## Available Prompts.*?(?=## How to Use Prompts)"
        gemini_content = re.sub(
            gemini_pattern, gemini_list, gemini_content, flags=re.DOTALL
        )
        with open(GEMINI_FILE, "w", encoding="utf-8") as f:
            f.write(gemini_content)

    # 5. Update README.md
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_content = f.read()

        readme_list = "## Available Templates\n\nTemplates are categorized by domain. Click a category to view its full reference catalog.\n\n"
        for domain_name, config in domains.items():
            if "prompts" in config:
                readme_list += (
                    f"### [{domain_name}]({CATALOG_DIR}/{config['filename']})\n"
                )
                for p in config["prompts"]:
                    readme_list += f"- `/prompts:{p['display_name']}` - {p['description'].rstrip('.')}\n"
                readme_list += "\n"

        # Update both categories and contributing link
        readme_pattern = r"## Available Templates.*?(?=## 🧪 Development & Quality|## 🤝 Contributing)"
        readme_content = re.sub(
            readme_pattern, readme_list, readme_content, flags=re.DOTALL
        )

        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_content)


if __name__ == "__main__":
    prompts = get_prompts()
    update_docs(prompts)
    print(f"\n🚀 Distributed documentation synchronized in {CATALOG_DIR}/")
