import math

class Lingkaran():
    jarijari = 0
    diameter = 0

    def __init__(self,jarijari):
        self.jarijari = jarijari
        self.diameter = jarijari * 2

    def keliling(self):
        return self.diameter * math.pi

    def luas(self):
        return math.pow(self.jarijari,2) * math.pi

    def volumebola(self):
        return (4/3) * math.pow(self.jarijari,3) * math.pi