from rumus import Rumus
from kubus import Kubus
from balok import balok
from segitiga import SegitigaSamaSisi
from lingkaran import Lingkaran
from jajargenjang import jajargenjang
import math



hitung = Rumus()

#print(math.pi)

# Slingkarankecil = Lingkaran(10)

# print 'luasnya adalah ', lingkarankecil.luas()
# print 'kelilingnya adalah ', lingkarankecil.keliling()
# print 'volume bolanya adalah ', lingkarankecil.volumebola()

# lingkarangede = Lingkaran(14)

#print 'luas lingkaran gede-nya adalah ', round(lingkarangede.luas(),2)
#print 'keliling lingkaran gede-nya adalah ', round(lingkarangede.keliling(),5)
#print 'volume bola gede-nya adalah ', round(lingkarangede.volumebola(),2)

# jajargenjang = jajargenjang(2, 10, 4)

#print 'keliling jajar genjang adalah ', jajargenjang.keliling()
#print 'luas jajar genjang adalah ', jajargenjang.luas()

print("Selamat Datang")
print("Anda mau apa?")
print("1. Balok")
print("2. Segitiga ")
print("3. Kubus")
print("4. Lingkaran")
print("5. Jajar Genjang")

pilihan = input("hitung : ")

if pilihan == 1:
    print("Anda akan menghitung Balok\n")
    panjang = input("panjang Balok adalah ")
    lebar = input("lebar Balok adalah ")
    tinggi = input("tinggi Balok adalah ")

    balok = balok(panjang, lebar, tinggi)
    print "Luas Balok adalah", balok.luas()
    print "Keliling Balok adalah", balok.keliling()
    print "Volume Balok adalah", balok.volume()

elif pilihan == 2:
    print("Anda akan menghitung segitiga sama sisi\n")
    sisi = input("sisi dari segitiga adalah ")
    print("")

    segitiga = SegitigaSamaSisi(sisi)
    print "Luas Segitiga adalah", segitiga.luas()

elif pilihan == 3:
    print("Anda akan menghitung kubus\n")
    sisi = input("sisi kubus adalah ")
    print("")

    kubus = Kubus(sisi)
    print  "Luas Kubus adalah", kubus.luas()
    print  "keliling Kubus adalah", kubus.keliling()
    print  "volume Kubus adalah", kubus.volume()

elif pilihan == 4:
    print("anda akan menghitung lingkaran\n")
    jarijari = input("jari-jari lingkaran adalah ")
    print("")

    lingkaran = Lingkaran(jarijari)
    print  "Keliling lingkaran adalah ", lingkaran.keliling()
    print  "luas lingkaran adalah ", lingkaran.luas()
    print  "volume bola adalah ", lingkaran.volumebola()

elif pilihan == 5:
    print("anda akan menghitung jajar genjang\n")
    sisimiring = input("sisi miring jajar genjang adalah ") 
    alas = input("alas jajar genjang adalah ")
    tinggi = input("tinggi jajar genjang adalah ")
    print("")
    jajargenjang = jajargenjang(sisimiring, alas, tinggi)
    print  "Keliling jajar genjang adalah ", jajargenjang.keliling()
    print  "Luas jajar genjang adalah ", jajargenjang.luas()

else:
    print("salah, yu kembali yu, awokwawk")  