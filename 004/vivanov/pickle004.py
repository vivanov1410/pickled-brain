from random import randrange
from time import sleep


class App:
    """Main class for our app"""
    def __init__(self, name):
        self.app_name = name
        self.welcome()

    def welcome(self):
        print('Welcome to {0}! First python app from Svetik :)'.format(self.app_name))
        print('Picker will help you make a hard choice by choosing a movie for you')
        print('')

    def run(self):
        movies = raw_input('Enter movies(separated by comma): ').split(',')

        if movies[0] == '':
            print('Very interesting... Then nothing indeed!')
            exit()

        print(self.hard())

        print('')
        print('Thinking. Answer will be ready in')
        for x in range(3, 0, -1):
            print('{0} sec'.format(x))
            sleep(1)

        picker = MoviePicker(movies)
        pick = picker.pick()
        print('')
        print('Finally! Today you should watch movie: {0}'.format(pick))
        print('Enjoy!')

    def hard(self):
        hard_phrases = ['Wow, thats hard...', 'I need to really think about it...', 'This is way too hard...', 'Why you treat me like that...', 'Love ya...']
        index = randrange(len(hard_phrases))
        return hard_phrases[index]


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

app = App('Movie Picker')
app.run()