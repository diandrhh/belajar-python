import math

class Rumus():
    def pangkatdua(self, x):
        return x ** 2
    def pangkattiga(self,x):
        return x ** 3
    def pangkat(self, x, y):
        return x ** y
    def nilaimutlak(self, x):
        if x < 0:
            return x * -1
        return x
    def pythagorasmiring(self, a, b):
        return math.sqrt(math.pow(a, 2) + math.pow(b,2))
    def pythagorassisi(self, c, b):
        return math.sqrt(math.pow(c, 2) - math.pow(b, 2))

