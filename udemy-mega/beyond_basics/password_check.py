correct_password = "python123"
password = input("Enter password: ")

while correct_password != password:
    password = input("Enter password: ")

print("Logged in!")
