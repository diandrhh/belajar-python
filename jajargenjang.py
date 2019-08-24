import math

class jajargenjang():
    sisimiring = 0
    alas = 0
    tinggi = 0
    sudutlancip = 0
    suduttumpul = 0

    def __init__ (self, sisimiring, alas, tinggi):
        self.sisimiring = sisimiring
        self.alas = alas
        self.tinggi = tinggi

    def keliling(self):
        return 2 * self.sisimiring + 2 * self.alas

    def luas(self):
        return self.tinggi * self.alas