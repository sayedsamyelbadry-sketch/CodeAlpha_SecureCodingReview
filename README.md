# CodeAlpha Secure Coding Review

## Project Overview

This project demonstrates a secure coding review process for a Python application.

The goal of this project is to identify security vulnerabilities in source code, analyze their impact, and apply secure coding practices to fix them.

---

## Objectives

- Perform manual code review.
- Use Bandit Static Code Analyzer to identify vulnerabilities.
- Document security findings.
- Apply remediation techniques.
- Improve application security.

---

## Technologies Used

- Python 3
- Bandit (SAST Tool)
- Linux (Kali)

---

## Project Structure
```
CodeAlpha_SecureCodingReview/

├── vulnerable_app.py
├── secure_app.py
├── findings.md
└── README.md
```

---

## Vulnerabilities Identified

### 1. Hardcoded Password

**Issue:**
Sensitive credentials were stored directly inside the source code.

**Fix:**
Used environment variables to store sensitive information securely.


### 2. Command Injection

**Issue:**
User input was executed using subprocess with shell=True.

**Fix:**
Removed shell=True and implemented command whitelisting.


### 3. Unsafe Deserialization

**Issue:**
Used pickle.load() which can be dangerous with untrusted data.

**Fix:**
Replaced pickle with JSON-based data handling.


### 4. Code Injection

**Issue:**
Used eval() to execute user input.

**Fix:**
Replaced eval() with ast.literal_eval().

---

## Security Analysis

Bandit was used to scan the vulnerable application.

Before Fixes:

- High Severity Issues: 1
- Medium Severity Issues: 2
- Low Severity Issues: 3

After Fixes:

- High Severity Issues: 0
- Medium Severity Issues: 0
- Low Severity Issues: 2

---

## Conclusion

This project demonstrates how secure coding practices and Static Application Security Testing (SAST) tools can help identify and mitigate security vulnerabilities before deployment.
