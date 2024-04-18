# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 07:59:36 2024

@author: Fairuz Maulidya
"""

class FilmFavorites:
    def __init__(self):
        self.favorite_films = []

    def input_favorite_films(self):
        print("Film favorit KE-1: ", end="")
        film1 = input()
        print("Film favorit KE-2: ", end="")
        film2 = input()
        print("Film favorit KE-3: ", end="")
        film3 = input()
        print("Film favorit KE-4: ", end="")
        film4 = input()
        print("Film favorit KE-5: ", end="")
        film5 = input()

        self.favorite_films = [film1, film2, film3, film4, film5]

    def display_favorite_films(self):
        print("==========DAFTAR FILM FAVORIT==========")
        for i, film in enumerate(self.favorite_films, 1):
            print(f"{i}.) {film}")


if __name__ == "__main__":
    print('''Praktikum 5 (Fairuz 064002300018) 
===============ELKOM 1=============''')
    film_list = FilmFavorites()
    film_list.input_favorite_films()
    film_list.display_favorite_films()
