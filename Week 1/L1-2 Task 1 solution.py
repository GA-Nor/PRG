# Task 1 Example solution
#prints a border of asterisks
def print_border():
    print("*" * 40)

#cleans the movie title by removing leading/trailing whitespace and capitalizing the first letter of each word
def clean_title(movie):
    return movie.strip().title()

#displays the movie title with a number and asterisks on either side
def display_movie(number, movie):

    entry = f"{number}. {movie}"

    print("* " + entry.ljust(36) + "*")

#Stores the users name and favorite movies in variables.
name = input("Enter your name: ").strip()

movies = input(
    "Enter your favourite movies (comma separated): "
)

#Creates the list of movies, as the split() method returns a list of strings, split by the comma in this case
movie_list = movies.split(",")

#prepare a new empty list to store the cleaned movie titles
clean_movies = []

#for loop to clean the movie titles and add them to a new list
for movie in movie_list:

    movie = clean_title(movie)

    if movie != "":
        clean_movies.append(movie)


#check the number of movies and store the correct message in a variable
if len(clean_movies) < 3:

    message = "You should watch more movies!"

elif len(clean_movies) <= 5:

    message = "Nice movie collection!"

else:

    message = "You are a movie enthusiast!"


#print the movie collection with a border and assessment message
print()
print_border()

title = f"{name.upper()}'S MOVIE COLLECTION"

print("*" + title.center(38) + "*")

print_border()

print()
print(message)
print()


#add a counter, as the items are listed
counter = 1

for movie in clean_movies:

    display_movie(counter, movie)

    counter += 1

print()
print_border()
        


