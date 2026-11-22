def process_user(record):
    name, login_count = record.split(",")
    return name.strip().title(), int(login_count)


def calculate_statistics(users):
    highest = users[0][1]
    lowest = users[0][1]
    total_logins = 0

    for user in users:
        login_count = user[1]
        total_logins += login_count

        if login_count > highest:
            highest = login_count
        if login_count < lowest:
            lowest = login_count

    average = total_logins / len(users)
    return highest, lowest, average


def load_login_data(filename):
    users = []
    with open(filename, "r") as file:
        for line in file:
            for record in line.strip().split(";"):
                if record:
                    name, login_count = process_user(record)
                    users.append([name, login_count])
    return users


# Read each record and save the user's name and login count.
users = load_login_data("logins.csv")

# Search for a username without case sensitivity.
search_name = input("Enter a username to search for: ").strip().lower()
found_user = None
for user in users:
    if user[0].lower() == search_name:
        found_user = user
        break

if found_user:
    print("Found:", found_user[0], "- Logins:", found_user[1])
else:
    print("User not found:", search_name)

# Calculate the highest, lowest, average, and total login counts.
total_logins = 0
for user in users:
    total_logins += user[1]

highest, lowest, average = calculate_statistics(users)

# Print the users and their login counts in a table.
print("Name".ljust(15) + " | " + "Logins".rjust(10))
print("-" * 30)
for user in users:
    name = user[0]
    login_count = user[1]
    print(name.ljust(15) + " | " + str(login_count).rjust(10))

print("Total:", total_logins)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
