from rumus import Rumus

hitung = Rumus()

class SegitigaSamaSisi():
    sisi = 0

    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        alas = self.sisi
        tinggi = hitung.pythagorassisi(self.sisi, self.sisi/2)
        return  alas/2 * tinggi
