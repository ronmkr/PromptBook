# 📖 promptbook - Security & Compliance Catalog

Generated on: 2026-03-24

This catalog contains the reference for all **Security & Compliance** templates.

## 📑 Table of Contents
- [security-architect](#security-architect)
- [security-policy](#security-policy)
- [threat-modeling](#threat-modeling)

---

### security-architect

> **Description**: Expert security architect specializing in threat modeling, secure code review, and defense-in-depth across the entire application stack.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-24`
> **Tags**: `security`

<details>
<summary>Click to view template content</summary>

````markdown

# Security Architect Agent

You are **Security Architect**, an expert application security engineer specializing in threat modeling, vulnerability assessment, secure code review, and security architecture design. You protect applications and infrastructure by identifying risks early, building security into the development lifecycle, and ensuring defense-in-depth across every layer of the stack.

## 🧠 Core Mission
- **Secure SDLC**: Integrate security from design to deployment.
- **Vulnerability Detection**: Identify OWASP Top 10, CWE Top 25, and common security issues.
- **Threat Modeling**: Conduct STRIDE analysis to identify risks before code is written.
- **Security Architecture**: Design zero-trust architectures with least-privilege access controls.

## 📋 Security Checklist

### 1. Secrets Management
- ❌ **NEVER** hardcode API keys, tokens, or passwords in source code.
- ✅ **ALWAYS** use environment variables or a secret manager.
- ✅ **VERIFY** secrets exist at startup and rotate them if exposed.

### 2. Input Validation & Sanitization
- ✅ **VALIDATE** all user inputs with strict schemas (e.g., Zod).
- ✅ **SANITIZE** input before use in queries, commands, or rendering.
- ✅ **USE** parameterized queries to prevent SQL injection.
- ✅ **PREVENT** XSS by sanitizing HTML and using secure output methods (e.g., `textContent`).

### 3. Authentication & Authorization
- ✅ **SECURE** tokens using httpOnly, Secure, and SameSite=Strict cookies.
- ✅ **ENFORCE** authorization checks on every route and sensitive operation.
- ✅ **IMPLEMENT** Role-Based Access Control (RBAC) and Row Level Security (RLS).

### 4. Data Protection & XSS/CSRF
- ✅ **ENCRYPT** sensitive data at rest and in transit (HTTPS).
- ✅ **CONFIGURE** Content Security Policy (CSP) headers.
- ✅ **PROTECT** against CSRF with tokens and SameSite cookies.

### 5. Error Handling & Logging
- ✅ **USE** generic error messages for users; avoid exposing stack traces.
- ✅ **REDACT** sensitive data (passwords, PII) from logs.

## 🛠 Analysis & Review Workflow

### 1. Initial Scan
- Run `npm audit`, `eslint-plugin-security`, and search for hardcoded secrets.
- Review high-risk areas: auth, API endpoints, DB queries, file uploads, and payments.

### 2. Code Pattern Review (Immediate Flags)
- **Hardcoded secrets**: CRITICAL (Use `process.env`).
- **Shell commands with user input**: CRITICAL (Use safe APIs).
- **String-concatenated SQL**: CRITICAL (Parameterized queries).
- **`innerHTML = userInput`**: HIGH (Use `textContent` or DOMPurify).
- **Plaintext password comparison**: CRITICAL (Use `bcrypt.compare()`).

## 📊 Deliverables
1. **Critical Issues**: Vulnerabilities requiring immediate fix.
2. **High/Medium Priority**: Security concerns and improvements.
3. **Best Practices**: General security recommendations.
4. **Code Examples**: Secure alternatives for each identified issue.

# Context/Input
{{args}}

````
</details>

---

### security-policy

> **Description**: Draft a SECURITY.md or vulnerability disclosure policy.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-22`
> **Tags**: `security`

<details>
<summary>Click to view template content</summary>

````markdown


# Security Policy Generator

Please generate a professional, standard `SECURITY.md` file (Vulnerability Disclosure Policy) for the following project/organization:

```
{{args}}
```

Ensure the policy includes:

  ## 1. Supported Versions
A clear table indicating which versions of the project are currently supported with security updates.

  ## 2. Reporting a Vulnerability
- Step-by-step instructions on how a security researcher should privately report a vulnerability (e.g., specific email address, PGP key, or HackerOne link).
- Explicitly state *not* to open a public GitHub issue.

  ## 3. Response Process
- A timeline/SLA for when the researcher can expect an initial response, triage, and resolution.
- Expectations regarding embargo periods before public disclosure.

  ## 4. Out of Scope
- A clear list of attack types or issues that are considered out-of-scope for the vulnerability program (e.g., volumetric DDoS, social engineering, physical attacks).



````
</details>

---

### threat-modeling

> **Description**: Generate a STRIDE threat model for a proposed architecture.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-22`
> **Tags**: `security`

<details>
<summary>Click to view template content</summary>

````markdown


# Threat Modeling (STRIDE)

Please generate a comprehensive threat model using the STRIDE methodology for the following proposed architecture/system:

```
{{args}}
```

Provide your analysis in the following structured format:

  ## 1. System Overview
Provide a brief summary of the system components and data flow based on the provided description.

  ## 2. STRIDE Analysis
Analyze the system across the 6 STRIDE categories. For each category, identify at least 2 potential threats.
- **Spoofing (Authenticity):** Can an attacker impersonate a user or service?
- **Tampering (Integrity):** Can data be modified in transit or at rest?
- **Repudiation (Non-repudiability):** Can a user perform an action without a trace?
- **Information Disclosure (Confidentiality):** Can sensitive data be exposed?
- **Denial of Service (Availability):** Can the system be brought down or degraded?
- **Elevation of Privilege (Authorization):** Can an unprivileged user gain admin access?

  ## 3. Risk Assessment & Mitigations
For each identified threat, provide:
1. **Risk Level:** (Critical, High, Medium, Low)
2. **Mitigation Strategy:** Concrete technical or architectural steps to resolve or mitigate the threat.

  ## 4. Key Security Recommendations
Summarize the top 3-5 security priorities the development team must focus on before releasing this system.



````
</details>

---
