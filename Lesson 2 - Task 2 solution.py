
# Task 2 Example solution
#prints a border of asterisks
def print_border():
    print("*" * 50)

#cleans the skill by removing leading/trailing whitespace and capitalizing the first letter of each word
def clean_skill(skill):

    return skill.strip().title()

#displays the skill with a number and asterisks on either side
def display_skill(number, skill):

    entry = f"{number}. {skill}"

    print("* " + entry.ljust(46) + "*")

#returns the assessment (as a string) based on the total number of skills
def get_assessment(total_skills):

    if total_skills <= 3:
        return "Beginner Level"

    elif total_skills <= 6:
        return "Developing Skills"

    else:
        return "Strong Skills Portfolio"

#takes the user input for student name, course name and skills
student_name = input(
    "Enter student name: "
).strip().title()

course_name = input(
    "Enter course name: "
).strip().title()

skills = input(
    "Enter skills (comma separated): "
)

#Creates the list of skills, as the split() method returns a list of strings, split by the comma in this case
skill_list = skills.split(",")

#prepare a new empty list to store the cleaned skills
clean_skills = []

#for loop to clean the skills and add them to a new list
for skill in skill_list:

    skill = clean_skill(skill)

    if skill != "":

        if skill not in clean_skills:
            clean_skills.append(skill)

#check the number of skills and store the correct assessment in a variable
assessment = get_assessment(len(clean_skills))


#print the student skills report with a border and assessment message
print()
print_border()

title = "STUDENT SKILLS REPORT"

print("*" + title.center(48) + "*")

print_border()

print()
print(f"Student : {student_name}")
print(f"Course  : {course_name}")

print()
print(f"Assessment : {assessment}")

print()
print("Skills")
print()


#add a counter, as the items are listed
counter = 1

for skill in clean_skills:

    display_skill(counter, skill)

    counter += 1

print()

total_skills = f"Total Skills: {len(clean_skills)}"

print(total_skills.rjust(50))

print_border()
