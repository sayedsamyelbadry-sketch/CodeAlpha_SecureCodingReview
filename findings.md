# Secure Coding Review Report

## Project: CodeAlpha Secure Coding Review

## Overview

This project demonstrates a secure code review process.
A vulnerable Python application was analyzed using Bandit Static Code Analyzer to identify security vulnerabilities.
After identifying the issues, security fixes were implemented in a secure version of the application.

---

# Findings

## 1. Hardcoded Password

### Vulnerability
The application stored an administrator password directly inside the source code.

### Risk
Attackers who gain access to the source code can easily discover sensitive credentials.

### Severity
Low

### Remediation
Sensitive information should not be stored inside source code.
Environment variables or secret management solutions should be used instead.

---

## 2. Command Injection

### Vulnerability
The application executed user-provided commands using subprocess with shell=True.

### Risk
An attacker could execute arbitrary operating system commands.

### Severity
High

### Remediation
Avoid executing raw user input.
Remove shell=True and implement input validation and command whitelisting.

---

## 3. Unsafe Deserialization

### Vulnerability
The application used pickle.load() to deserialize user-controlled data.

### Risk
Malicious serialized objects could execute unauthorized code.

### Severity
Medium

### Remediation
Use safer data formats such as JSON when handling untrusted data.

---

## 4. Code Injection

### Vulnerability
The application used eval() to execute user input.

### Risk
An attacker could execute arbitrary Python code.

### Severity
Medium

### Remediation
Replace eval() with safer alternatives such as ast.literal_eval().

---

# Tools Used

- Python
- Bandit Static Application Security Testing (SAST) Tool

---

# Conclusion

After applying security fixes, the application was scanned again using Bandit.
The number of vulnerabilities was significantly reduced, demonstrating the importance of secure coding practices and security reviews.
