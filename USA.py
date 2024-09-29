import re
data = "3403578654"
def validate_USA_mobile_number(number):
    pattern = r"^[0-9]\d{9}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("Validate Mobile Number : ", validate_USA_mobile_number(data))