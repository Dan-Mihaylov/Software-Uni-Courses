from project.movie_specification.movie import Movie


class Action(Movie):

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
