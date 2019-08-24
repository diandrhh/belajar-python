from rumus import Rumus

hitung = Rumus()

class Kubus():
    sisi = 0

    def __init__(self, sisi):
        self.sisi = sisi

    def keliling(self):
        return 4 * self.sisi

    def luas(self):
        return self.sisi * self.sisi
    def volume(self):
        return self.sisi * self.sisi * self.sisi
