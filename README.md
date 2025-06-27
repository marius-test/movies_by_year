# movies_by_year

A small Python program I wrote to solve a personal problem related to managing my movie watchlist.

### Background

I love movies and cinema. Whenever I hear about a movie I want to watch, I write it down in my notes in this format:
```bash
Movie Title (Year)
```
However, the list gets unordered and messy. I wanted a simple way to sort my movies by their release year in ascending order.

### How it works

1. Reads a `.txt` file containing the list of movies in the format:  
   `Movie Title (Year)`  
2. Parses each line into a tuple: `(Movie Title, Year)`  
3. Sorts the list by release year using Python’s `sorted()` function with a `lambda` key  
4. Prints the sorted list to the console  
5. Saves the sorted list back into a new `.txt` file, preserving the original format

### Usage

Run the script with your input file named `movies_to_watch.txt`. The sorted output will be saved to `movies_to_watch_by_year.txt`.

```python
if __name__ == '__main__':
    movies = read_movies_from_file("movies_to_watch.txt")
    sorted_movies = sort_movies_by_year(movies)
    print_movies(sorted_movies)
    save_movies_to_file(sorted_movies, "movies_to_watch_by_year.txt")
```
