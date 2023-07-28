from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def _check_username_taken(self, username):

        for user in self.users_collection:
            if user.username == username:
                return True

        return False

    def register_user(self, username: str, age: int):

        if self._check_username_taken(username):
            raise Exception("User already exists!")

        new_user = User(username, age)

        if new_user not in self.users_collection:
            self.users_collection.append(new_user)
            return f"{username} registered successfully."

    def _find_user_by_username(self, username: str):

        for user in self.users_collection:
            if user.username == username:
                return user

        raise Exception("This user does not exist!")

    def upload_movie(self, username: str, movie):

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self._find_user_by_username(username)

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):

        user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():

            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie):

        user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):

        user = self._find_user_by_username(username)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):

        user = self._find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = []

        if len(self.movies_collection) == 0:
            result.append("No movies found.")
        else:
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result.append(movie.details())

        return "\n".join(result)

    def __str__(self):

        result = []

        if len(self.users_collection) == 0:
            result.append("All users: No users.")
        else:
            user_string = f"All users: {', '.join(x.username for x in self.users_collection)}"
            result.append(user_string)

        if len(self.movies_collection) == 0:
            result.append("All movies: No movies.")
        else:
            movies_string = f"All movies: {', '.join(m.title for m in self.movies_collection)}"
            result.append(movies_string)

        return f"\n".join(result)



