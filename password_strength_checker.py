import re
def check_strength(password):
    if len(password) < 10:
        print("Weak password: Must be at least 10 characters long.")
        return
    if not re.search(r"[A-Z]", password):
        print("Weak password: Add at least one uppercase letter.")
        return
    if not re.search(r"[a-z]", password):
        print("Weak password: Add at least one lowercase letter.")
        return
    if not re.search(r"\d", password):
        print("Weak password: Add at least one number.")
        return
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Weak password: Add at least one special character (!@#$%^&* etc.).")
        return
    print("Strong Password")
user_password = input("Enter the password: ")
check_strength(user_password) 
