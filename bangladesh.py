import re
data = "880"
def validate_bangladesh_mobile_number(number):
    pattern = r"^[8]\d{2}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("Validate Mobile Number : ", validate_bangladesh_mobile_number(data))