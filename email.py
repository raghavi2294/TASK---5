import re
email_address="raji@gmail.in"
def validate_email_address (data):
    pattern=r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("validate email:", validate_email_address(email_address))
