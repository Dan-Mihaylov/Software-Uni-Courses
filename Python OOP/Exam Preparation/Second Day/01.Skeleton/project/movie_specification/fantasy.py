from project.movie_specification.movie import Movie


class Fantasy(Movie):

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"


