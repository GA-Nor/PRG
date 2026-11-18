"""
Topics:
- Input and Output
- Strings
- String Manipulation
- split(), strip(), title(), upper()
- Lists
- if / elif / else
- For-each loops
- Counter-controlled loops
- String formatting
- ljust(), center(), rjust()
- User-defined functions

====================================================
INPUT AND STRING MANIPULATION
====================================================
"""


#Store users name in a variable. The order matters, first method (strip()) runs before the next (capitalize())
name = input("Enter your name: ").strip().capitalize()  
print("Hi "+name)


#Stores the users games as a string
games = input("Enter your favourite games (separated by comma): ")
print(games)

#Removes whitespaces in string
#games = games.replace(" ", "")  #Remove all spaces from the string
#Create the list of games entered by the user

game_list = games.split(",")

print (game_list)

#Prepare the list, this just creates an empty list we can use to store processed (.strip().title()) strings.
clean_games = []

#Clean the games and remove blank entries
for game in game_list:  # for-each loop

    #Clean the game name, removing leading/trailing spaces and capitalising the first letter of each word
    game = game.strip().title()

    #Remove blank entries, in case the user entered a comma with no game name
    if game != "":
        clean_games.append(game)


print("\nCleaned Games")
#Goes through each game in the list, and prints each game
for game in clean_games:
    print(game)



#FOR LOOP (With counter)
print("\nCounter Example")
#Print the same list of games, but adding an incrementing counter for each element.
#Initialize a counter variable to 1, count starts at 1
counter = 1
#For every game in the list of cleaned games, print the game with a number in front of it, and increase the counter by 1
for game in clean_games:

    #Using an "f-string" to include variables into printed text. (optionally: print(counter,"- ",game))
    print(f"{counter}- {game}")
    #Increases the counter for each loop (iteration), so the next printed item will be 1 higher
    counter += 1
    

#IF / ELIF / ELSE
lengthOfList = len(clean_games)
print(f"The length of the list is: {lengthOfList}")

# if the length of the list is less than 3, print a message
if lengthOfList < 3:
    print("You need more favourite games!")
# if the length of the list is between 3 and 5, print a different message
elif lengthOfList <= 5:
    print("Nice collection!")
# if the length of the list is greater than 5, print a different message, since this is the last condition, we can use else instead of elif
else:
    print("You are a serious gamer!")




#STRING ALIGNMENT
name = input("Input name: ")
print(f"Number of chars in name: {len(name)}")
#Print a new line and a border of 40 asterisks
print("\n" + "*" * 40)

#Create a title using the users name, and convert it to uppercase
title = f"{name.upper()}'S FAVOURITE GAMES"

#Print the title, centered (relative to 38 character width), with a border of asterisks on either side
print("*" + title.center(38) + "*")

#Print another border of 40 asterisks
print("*" * 40)




#DEMONSTRATION 6 - FUNCTIONS

#this function prints a border of 40 asterisks
def print_border():
    print("*" * 40)


#this function cleans the game name, removing leading/trailing spaces and capitalising the first letter of each work
def clean_game(game):
    return game.strip().title()


#this function displays the title
def create_title(name):
    return f"{name.upper()}'S FAVOURITE GAMES"


#this function displays the game entry with a number and proper formatting (Number. gameName)
def display_game(number, game):

    entry = f"{number}. {game}"

    print("* " + entry.ljust(38) + "*")



print("\nFunction Demonstration")


#Call the border function
print_border()
#Call the create_title function, passing in the users name, and print the result
#Optional: Can store the title in a variable, or use the function directly in the print statement.
titleName = create_title(name)
print("*" + titleName.center(38) + "*")
#Call the border function again
print_border()



#initialize the counter variable to 1, count starts at 1
counter = 1
#For every game in the list of cleaned games, call the display_game function, passing in the counter
for game in clean_games:

    display_game(counter, game)

    counter += 1

#print the border again
print_border()
