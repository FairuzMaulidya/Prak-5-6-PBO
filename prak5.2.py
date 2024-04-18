# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:06:39 2024

@author: Fairuz Maulidya
"""
print("Prak 5 (Fairuz Maulidya 064002300018) - ELKOM 2")
print("-----------------ELKOM 2-------------------")
class Film:
    def __init__(self, title, release_year, director):
        self.title = title
        self.release_year = release_year
        self.director = director


class FilmList:
    def __init__(self):
        self.film_list = []

    def add_film(self, film):
        self.film_list.append(film)

    def set_default_favorites(self):
        for i in range(1, 6):
            print(f"Film favorit ke-{i}:")
            title = input("Judul: ")
            release_year = input("Rilis: ")
            director = input("Director: ")
            film = Film(title, release_year, director)
            self.add_film(film)
            print("===================")

if __name__ == "__main__":
    film_list = FilmList()
    film_list.set_default_favorites()
