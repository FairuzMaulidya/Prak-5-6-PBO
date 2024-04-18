# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:27:12 2024

@author: Fairuz Maulidya
"""

import math

class BangunRuang:
    def __init__(self, nama):
        self.nama = nama
    
    def luas(self):
        pass
    
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi
    
    def luas(self):
        return 6 * self.sisi ** 2
    
    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, nama, panjang, lebar, tinggi):
        super().__init__(nama)
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
    
    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, nama, jari_jari):
        super().__init__(nama)
        self.jari_jari = jari_jari
    
    def luas(self):
        return 4 * math.pi * self.jari_jari ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Silinder(BangunRuang):
    def __init__(self, nama, jari_jari, tinggi):
        super().__init__(nama)
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
    
    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, nama, alas, tinggi_alas, tinggi_prisma):
        super().__init__(nama)
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi_alas + 3 * self.alas * self.tinggi_prisma
    
    def volume(self):
        return 0.5 * self.alas * self.tinggi_alas * self.tinggi_prisma

# Membuat objek dari setiap bangun ruang
kubus = Kubus("Kubus", 5)
balok = Balok("Balok", 3, 4, 5)
bola = Bola("Bola", 7)
silinder = Silinder("Silinder", 4, 6)
prisma_segitiga = PrismaSegitiga("Prisma Segitiga", 8, 6, 4)

# Menampilkan hasil perhitungan luas dan volume
print("Nama: Fairuz Maulidya")
print("Nim: 064002300018")
print("==========================")
print(f"Luas {kubus.nama}: {kubus.luas()}")
print(f"Volume {kubus.nama}: {kubus.volume()}")
print(f"Luas {balok.nama}: {balok.luas()}")
print(f"Volume {balok.nama}: {balok.volume()}")
print(f"Luas {bola.nama}: {bola.luas()}")
print(f"Volume {bola.nama}: {bola.volume()}")
print(f"Luas {silinder.nama}: {silinder.luas()}")
print(f"Volume {silinder.nama}: {silinder.volume()}")
print(f"Luas {prisma_segitiga.nama}: {prisma_segitiga.luas()}")
print(f"Volume {prisma_segitiga.nama}: {prisma_segitiga.volume()}")