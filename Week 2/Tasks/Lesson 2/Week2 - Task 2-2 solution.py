def load_department(filename):
    with open(filename) as file:
        members = file.read().strip().split(",")
    return set(members)


def generate_report(department_a, department_b):
    common_users = department_a.intersection(department_b)
    only_in_a = department_a.difference(department_b)
    only_in_b = department_b.difference(department_a)
    return common_users, only_in_a, only_in_b


department_a = load_department("department_a.csv")
department_b = load_department("department_b.csv")
common_users, only_in_a, only_in_b = generate_report(department_a, department_b)

print("Users in both departments:")
for user in sorted(common_users):
    print(user)

print("Users only in department A:")
for user in sorted(only_in_a):
    print(user)

print("Users only in department B:")
for user in sorted(only_in_b):
    print(user)
