import re

LOCAL_REGEX = re.compile(r"^[a-zA-Z0-9._-]+$")
DOMAIN_REGEX = re.compile(r"^[a-zA-Z0-9.]+$")

def is_valid_email(email: str) -> bool:
    if not email or " " in email:
        return False

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    # Local part rules
    if not local:
        return False
    if not LOCAL_REGEX.match(local):
        return False

    # Domain rules
    if not domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    if "." not in domain:
        return False
    if not DOMAIN_REGEX.match(domain):
        return False

    return True