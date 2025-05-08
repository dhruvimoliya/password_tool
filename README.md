# Password Tool

Passwords are the **first line of defence**. strong passwords prevent huge losses.
This is a **simple yet powerful command-line utility** for password management, that helps assess password strength and secure password generation.

## Features

- **Password Strength Checker**: Evaluates passwords based on multiple security criteria:
  - Length (minimum 8 characters recommended, 12+ preferred)
  - Character diversity (uppercase, lowercase, numbers, special characters)
  - Common pattern detection (sequential numbers, keyboard patterns, etc.)
  - Entropy estimation

- **Secure Password Generator**: Creates cryptographically strong passwords with:
  - Customizable length (8-30 characters)
  - Configurable character sets (uppercase, lowercase, numbers, and special characters)
  - Uses Python's `secrets` module for cryptographic security

## Installation

1. Ensure you have Python v3.6 or later installed
2. Download the `password_tool.py` file
3. No additional dependencies required - uses only Python standard library

## Usage

To run the program:

```
python password_tool.py
```

### Menu Options

1. **Check Password Strength**: Analyze an existing password
   - Provides a strength score (out of 6)
   - Offers specific improvement feedback
   - Estimates password entropy

2. **Generate Strong Password**: Create a new secure password
   - Customize password length
   - Select which character types to include
   - Automatically checks the strength of generated passwords

3. **Exit**: Quit the program

## Security Features

- Uses Python's `secrets` module for cryptographically secure random generation
- Ensures generated passwords include at least one character from each selected type
- Shuffles character placement to prevent predictable patterns
- Detects common weak patterns in passwords

## Best Practices

For maximum security:
- Use passwords at least 12 characters long
- Include a mix of character types (uppercase, lowercase, numbers, special characters)
- Avoid common words, patterns, or personal information
- Use different passwords for different services

## License

This tool is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This tool is for educational and personal use. Always follow your organization's security policies for password management.
