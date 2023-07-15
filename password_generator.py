from random import choice
from string import ascii_letters, digits, punctuation

lenght = int(input("Enter password length to generate : "))
password = ""
for i in range(lenght):
    password = password + choice(ascii_letters + digits + punctuation)
print(f"Generated Password : {password}")
