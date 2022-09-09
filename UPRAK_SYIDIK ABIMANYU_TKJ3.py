'''BUATLAH SINTAKS MENGHITUNG BANGUN RUANG'''

# BALOK

print("\n1.Volume balok")
panjang_balok = int(input("masukan nilai panjang:"))
lebar_balok = int(input("masukan nilai lebar:"))
tinggi_balok = int(input("masukan nilai tinggi:"))
volume_balok = panjang_balok * lebar_balok * tinggi_balok

print("volume balok adalah",volume_balok)

# KUBUS

print("\n2.Volume kubus")
sisi1 = int(input("masukan nilai sisi:"))
sisi2 = int(input("masukan nilai sisi:"))
sisi3 = int(input("masukan nilai sisi:"))
volume_kubus = sisi1 * sisi2 * sisi3

print("volume kubus adalah",volume_kubus)           

# LIMAS

print("\n3.Volume limas")
phi = 1/3
la_persegi = int(input("masukan nilai luas alas persegi:"))
tinggi_limas = int(input("masukan nilai tinggi:"))
volume_limas = phi * (la_persegi * la_persegi) * tinggi_limas

print("volume limas adalah",volume_limas)

# TABUNG

print("\n4.Volume tabumg")
phi = 22/7
r = int(input("masukan nilai jari jari:"))
t = int(input("masukan nilai tinggi:"))
volume_tabung = phi * r * r * t

print("volume tabung adalah",volume_tabung)


# CELCIUS TO REAMUR

print("\n5.nilai celcius ke reamur")
celcius_1 = int(input("masukan nilai celcius:"))
nilai_r = 4/5 * celcius_1

print("masukan nilai reamur adalah",nilai_r)
