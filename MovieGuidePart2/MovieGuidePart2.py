def display_menu():
    print("\n  Movie Guide Directory   ")
    print("Command Menu")
    print("list - List all of the movies")
    print("add  - Add a movie to the list")
    print("del  - Delete a movie in the list")
    print("exit -Exit the movie guide directory")
    print()

def load_movies(filename):
    try:
        with open(filename, "r") as file:
            movies = [line.strip() for line in file.readlines()]
        return movies
    except FileNotFoundError:
        initial_movies = ["Cat on a Hot Tin Roof", 
                          "On the Waterfront", 
                          "Monty Python and the Holy Grail"]
        with open(filename, "w") as file:
            for movie in initial_movies:
                file.write(movie + "\n")
        return initial_movies
def save_movies(filename, movies):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(movie + "\n")
def list_movies(movies):
    if not movies:
        print("No movies in the list, please try adding.")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
    print()
def add_movie(movies, filename):
    movie = input("Enter the name of the movie you would lik to add to the list: ")
    movies.append(movie)
    save_movies(filename, movies) 
    print(f"'{movie}' has been added to the list.\n")
    list_movies(movies)
def delete_movie(movies, filename):
    try:
        number = int(input("Enter the number of the movie that you would like to delete: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number -1)
            save_movies(filename, movies)
            print(f"{removed}' has been removed from the list.\n")
            list_movies(movies) 
        else:
            print("Invalid Movie number selection, please try again.\n")
    except ValueError:
        print("Invalid input, please enter a valid number to try again.\n")

def main():
    filename = "movies.txt"
    movies = load_movies(filename)

    display_menu()
    while True:
        command = input("Enter a command please: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies, filename)
        elif command == "del":
            delete_movie(movies, filename)
        elif command == "exit":
            print("Thank you so much for using the movie directory, see you next time!! ")
            break
        else:
            print("Invalid command. Please try your input again.\n")

if __name__ == "__main__":
    main()