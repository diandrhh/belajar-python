from rumus import Rumus

hitung = Rumus()

class balok():
    panjang = 0
    lebar = 0
    tinggi = 0

    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def keliling (self):
        return 2 * self.panjang + 2 * self.lebar

    def luas(self):
        return self.panjang * self.lebar

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    def setnilailebar (self, lebar):
        self.lebar = lebar 
    
    def setnilaipanjang (self, panjang):
        self.panjang = panjang
        
    def setnilaitinggi (self, tinggi):
        self.tinggi = tinggi