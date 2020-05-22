def password_validator(password):
    checks = 0
    if not 6 <= len(password) <= 10:
        checks += 1
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        checks += 1
        print("Password must consist only of letters and digits")
    if 2 > sum(1 for i in password if i.isdigit()):
        checks += 1
        print("Password must have at least 2 digits")
    if checks == 0:
        print("Password is valid")


passw = input()
password_validator(passw)
