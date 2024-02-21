# movies_by_year

A short program I wrote in Python to help me sort my list of movies to watch.

My list was formatted but unordered, the format of my list was:

```text
Movie A (Release Year)
Movie B (Release Year)
Movie C (Release Year)
.
.
.
```

I wanted to sort my list of movies by release year, ascending.

So I came up with the following steps:

1. Open the .txt file.
2. Transform the data into a tuple containing all movies but the title and release year as two separate elements.
3. Sort the movies using the *sorted* function and the *lambda* function as the key to sort by release year.
4. Print the sorted tuple to the console for testing purposes.
5. Save the tuple inside a new .txt file in the original format.
6. Run the code.
