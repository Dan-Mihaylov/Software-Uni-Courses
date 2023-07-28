from project.movie_specification.movie import Movie


class Thriller(Movie):

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
