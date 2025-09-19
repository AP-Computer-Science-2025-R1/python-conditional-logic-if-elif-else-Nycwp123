username = "user"
password_length = 12

if username == "admin":
    if password_length >= 10: 
        print ("Login successful.")
    else:
        print("Admin password incorect.")
else:
    if password_length >= 6:
        print("Login successful")
    else:
        print("users password must be 6+ character.")