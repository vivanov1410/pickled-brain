from random import randrange


class PickMovies:
    def __init__(self):
        self.movies = []

    @staticmethod
    def is_string(string):
        return type(string) == str

    def add(self, movie):
        if not self.is_string(movie) or movie is None:
            return 'wrong format'
        self.movies.append(movie)

    def pick(self):
        choice = randrange(len(self.movies))
        return "I guess that, today you're watching  {0}".format(self.movies[choice])


my_movies = PickMovies()
my_movies.add("'The Matrix'")
my_movies.add("'Father of the Bride'")
my_movies.add("'Judge Dredd 1995'")
my_movies.add("'Dredd 2012'")
print(my_movies.add(2))
print(my_movies.add(""))
my_movies.pick()
print(my_movies.movies)
print(my_movies.pick())


"""from random import randrange

movies = ['The 6th Day', 'Riddick', 'Matrix']

choice = randrange(len(movies))
print("Today you're watching {0}".format(movies[choice]))"""