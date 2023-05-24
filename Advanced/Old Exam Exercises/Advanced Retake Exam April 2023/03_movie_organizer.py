def movie_organizer(*args):
    movies_info = {}
    result = ""

    for arg in args:
        name = arg[0]
        genre = arg[1]
        movies_info[genre] = movies_info.get(genre, [])
        movies_info[genre].append(name)

    for genre, names in dict(sorted(movies_info.items(), key= lambda x: (-len(x[1]), x[0]))).items():
        result += f"{genre} - {len(names)}\n"
        for name in sorted(names):
            result += f"* {name}\n"

    return result
















print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
