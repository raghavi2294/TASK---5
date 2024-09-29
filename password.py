import re
password = "Raghaviraji2122$"


def validate_password(data):
    pattern = r"^[a-zA-Z0-9$]\d{15}$"
    if re.match(pattern, data):
        return True
    else:
        return False


print("Validate Password  : ", validate_password(password))
