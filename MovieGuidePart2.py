# Joshua Flye, CIS261, Movie Guide Part 2

def display_menu():
    print("The Movie List program")
    print("\nCOMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit a program")

def load_movies_from_file(filename="movies.txt"):
    movies = []
    try:
        with open(filename, "r") as file:
            for line in file:
                movies.append(line.strip()) # .strip() removies newline characters
    except FileNotFoundError:
                    print(f"File '{filename}' not found. Starting with an empty movie list.")
    return movies

def write_movies_to_file(movies, filename="movies.txt"):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_movies(movie_list):
    if not movie_list:
        print("There are no movies in the list.")
        return
    for i, movie in enumerate(movie_list, 1):
        print(f"{i}. {movie}")

def add_movie(movie_list):
    movie_title = input("Movie: ")
    movie_list.append(movie_title)
    print(f"{movie_title} was added.")

def delete_movie(movie_list):
    if not movie_list:
        print("There are no movies to delete.")
        return

    while True:
        try:
            number_to_delete = int(input("Number: "))
            if 1 <= number_to_delete <= len(movie_list):
                deleted_movie = movie_list.pop(number_to_delete - 1)
                print(f"{deleted_movie} was deleted.")
                break
            else:
                print("Invalid movie number.")
        except ValueError:
            print("Invalid movie number.")

def main():
    initial_movies = ["Cat on a Hot Tin Roof", "On the Waterfront", "Monty Python and the Holy Grail"]
    try:
        with open("movies.txt", "x") as f:
            for movie in initial_movies:
                f.write(movie + "\n")
    except FileExistsError:
        pass

    movies = load_movies_from_file()

    display_menu()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            display_movies(movies)
        elif command == "add":
            add_movie(movies)
            write_movies_to_file(movies)
            display_movies(movies)
        elif command == "del":
            delete_movie(movies)
            write_movies_to_file(movies)
            display_movies(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
        print("\nPress any key to continue...")
        input() # Pause for user to press a key


if __name__ == "__main__":
    main()
   