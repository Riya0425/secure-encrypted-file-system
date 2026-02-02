# Secure Encrypted File System (Python)

## Project Overview
The Secure Encrypted File System is a Python-based application designed to demonstrate basic file security concepts using encryption and password-based access control.

The project is intended for **educational and academic purposes** and focuses on clarity and simplicity rather than real-world cryptographic security.

## Objectives
- Secure text file content using encryption
- Provide dual-level access using two passwords
- Demonstrate Python file handling and conditional logic
- Help students understand basic security mechanisms

## Features
- Dual-password system (Normal & Secret)
- Caesar Cipher–based encryption with fixed key
- Encrypted file storage
- Console-based and GUI-based implementations
- Access control based on password type

## Encryption Technique
- Uses **Caesar Cipher** with a fixed shift of `4`
- Encrypted text is **reversed** for additional obfuscation
- Decryption reverses the process to restore original content

> ⚠️ Note: This encryption method is for learning purposes only and is **not secure for real-world use**.

## Password System
- **Normal Password**
  - Allows access to the file
  - Displays only encrypted content

- **Secret Password**
  - Allows full access
  - Displays decrypted (original) content

- Incorrect password results in access denial

## Project Structure

