from random import randrange


class MoviePicker:
    """Helps picks movies when you are lazy"""

    def __init__(self, movies):
        self.movies = movies

    def add(self, movie):
        if type(movie) is not str or movie is None:
            print('[error] movie should be a string')
            return
        self.movies.append(movie)

    def pick(self):
        if len(self.movies) == 0:
            print('[error] oops, you do not have any movies yet.')
            return
        choice = randrange(len(self.movies))
        return self.movies[choice]

my_movies = raw_input('Enter movies(separated by comma): ').split(',')
picker = MoviePicker(my_movies)
picker.add('i love you')
print(picker.pick())