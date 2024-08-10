
from verify_account import verify_account
username = input("enter your username ")
password = input("enter your password ")

# verify the account
if (verify_account(username, password)):
    print("access authorized")
else:
    print("access denied")

