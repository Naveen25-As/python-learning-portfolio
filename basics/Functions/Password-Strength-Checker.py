# Password Strength Checker.

def check_password(password):
    
    upper = lower = digit = special = 0
    
    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        else:
            special += 1
            
    if len(password) >= 8 and upper and lower and digit and special:
        return "Strong password"
    else:
        return "Weak password"

password = input("Enter password: ")

print(check_password(password))