def load_username(filename):
    with open(filename,"r") as file:
        return file.read().strip()

username=load_username("username.txt")
# username=input("Enter your username: ")
print("Username:",username)
print("Length:",len(username))
print("Upper:",username.upper())
print("Lower:",username.lower())
print("Starts with A:",username.startswith("A"))
print("Letters only:",username.isalpha())
print("Digits only:",username.isdigit())
print("Letters and digits:",username.isalnum())
print("Lowercase:",username.islower())
print("Uppercase:",username.isupper())

print("Name".ljust(15),"Username".ljust(15),sep=" | ")
print("-"*35)
print("Alice".ljust(15),username.ljust(15),sep=" | ")
