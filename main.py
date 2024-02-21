def read_movies_from_file(filename):
    """Reads movie data from a file and returns a list of tuples."""
    movies = []
    with open(filename, "r") as file:
        for line in file:
            name, year = line.strip().split("(")[:2]
            year = year.strip()[:-1]
            movies.append((name, year))
    return movies


def sort_movies_by_year(movies):
    """Sorts movies by year in ascending order."""
    return sorted(movies, reverse=False, key=lambda movie: movie[1])
   
   
def print_movies(movies):
    """Prints the list of movies to the console."""
    if movies:
        print(movies)
    else:
        print("File is empty!")


def save_movies_to_file(movies, filename):
    """Saves movies to a file in the specified format."""
    with open(filename, "w") as output:
        for name, year in movies:
            output.write(f"{name}({year})\n")
           
            
"""Executing the program."""
if __name__ == '__main__':
    movies = read_movies_from_file("movies_to_watch.txt")
    sorted_movies = sort_movies_by_year(movies)
    print_movies(sorted_movies)
    save_movies_to_file(sorted_movies, "movies_to_watch_by_year.txt")
