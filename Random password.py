import secrets
import string
from time import sleep

while True:
    raw = string.ascii_letters + string.punctuation + string.digits + string.ascii_uppercase
    length = input("Please enter the length of password(min length is 6). ")

    if int(length) < 6:
        print("The password length should be > 6.")

    password = ''.join(secrets.choice(raw) for i in range(int(length)))
    print("Generating a strong password.. ")
    print("Here is your password {0}".format(password))
    sleep(1)
