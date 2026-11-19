import csv
from pathlib import Path


def check_password(password):    
    longEnough = False
    hasUppercase = False
    hasLowercase = False
    hasSymbol = False
    
    lengthCriteria = 16
    
    passwordLength = len(password)
    
    if passwordLength >= lengthCriteria:
        return True

    for character in password:
        if character.isupper():
            hasUppercase = True

        if character.islower():
            hasLowercase = True

        if character == "." or character == "!" or character == "-":
            hasSymbol = True
        elif character == "_" or character == "#" or character == "?":
            hasSymbol = True

    if longEnough == True:
        if hasUppercase == True:
            if hasLowercase == True:
                if hasSymbol == True:
                    return True

    return False

strong_count = 0
weak_count = 0

print("PASSWORD SECURITY AUDIT")
print("-----------------------")

with open("passwords.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row["username"]
        username = username.strip()
        username = username.title()
        password = row["password"]
        password_is_strong = check_password(password)

        if password_is_strong == True:
            print(username, "- STRONG")
            strong_count = strong_count + 1
        else:
            print(username, "- WEAK")
            weak_count = weak_count + 1

print()
print("SUMMARY")
print("Strong passwords:", strong_count)
print("Weak passwords:", weak_count)
