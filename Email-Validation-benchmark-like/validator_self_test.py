from email_rules import is_valid_email

tests = {
    "user@com": False,
    "user@.com": False,
    "user@exam!ple.com": False,
    "user@example.com": True,
    "user.name@example.com": True,
    "user..name@example.com": True,
    "user@exa..mple.com": False,
    "user@example": False,
    "user example@example.com": False,
}

for email, expected in tests.items():
    result = is_valid_email(email)
    assert result == expected, f"{email}: expected {expected}, got {result}"

print("Validator tests passed.")
