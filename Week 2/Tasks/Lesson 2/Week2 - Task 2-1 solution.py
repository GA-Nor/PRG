def clean_name(name):
    return name.strip().title()


def load_users(filename):
    users = []
    with open(filename) as file:
        for line in file:
            name = clean_name(line)
            if name:
                users.append(name)
    return users


def get_statistics(users):
    if not users:
        return "", "", 0

    longest_name = users[0]
    shortest_name = users[0]

    for name in users:
        if len(name) > len(longest_name):
            longest_name = name
        if len(name) < len(shortest_name):
            shortest_name = name

    return longest_name, shortest_name, len(users)


cleaned_users = load_users("users2.txt")
cleaned_users.sort()

print("Name".ljust(20))
print("-" * 20)
for user in cleaned_users:
    print(user.ljust(20))

longest_name, shortest_name, total_users = get_statistics(cleaned_users)
print("Longest name:", longest_name)
print("Shortest name:", shortest_name)
print("Total users:", total_users)
