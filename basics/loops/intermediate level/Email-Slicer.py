# Email Slicer.

email = input("Enter your email address: ").strip()

if email.count("@") != 1:
    print("Invalid email format.")
else:
    username, domain = email.split("@")

    if not username or "." not in domain:
        print("Invalid email format.")
    else:
        print("\n===== EMAIL DETAILS =====")
        print("Username:", username)
        print("Domain:", domain)