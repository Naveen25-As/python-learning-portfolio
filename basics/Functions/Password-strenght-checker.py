# Password strenght checker.

def check_password(password):
    if len(password) < 8:
        return "Weak"

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong"
    else:
        return "Medium"

password = input("Enter Password: ")
print("Password Strength:", check_password(password))