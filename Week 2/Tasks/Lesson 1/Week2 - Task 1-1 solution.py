from pathlib import Path


def load_username(filename):
    with open(filename, "r") as file:
        return file.read().strip()


username_file = Path(__file__).resolve().parent / "username.txt"
saved_username = load_username(username_file)

name = input("Enter your name: ").strip()
username = input(f"Enter your username [{saved_username}]: ").strip()
if not username:
    username = saved_username

print("\nUSERNAME INFORMATION")
print("Username:", username)
print("Length:", len(username))
print("Upper:", username.upper())
print("Lower:", username.lower())

print("\nUSERNAME CHECKS")
print("Starts with A:", username.startswith("A"))
print("Letters only:", username.isalpha())
print("Digits only:", username.isdigit())
print("Letters and digits:", username.isalnum())
print("Lowercase:", username.islower())
print("Uppercase:", username.isupper())

print("\nNUMBER CALCULATIONS")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number == 0:
    print("Division: undefined (cannot divide by zero)")
    print("Floor division: undefined (cannot divide by zero)")
    print("Modulus: undefined (cannot divide by zero)")
else:
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Modulus:", first_number % second_number)

print("\nUSER REPORT")
print("Name".ljust(15), "Username".ljust(15), sep=" | ")
print("-" * 35)
print(name.ljust(15), username.ljust(15), sep=" | ")
