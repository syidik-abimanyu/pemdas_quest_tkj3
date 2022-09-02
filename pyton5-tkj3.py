'''Bangun dasar
   - persegi
   -segitiga
   -jajargenjang
   -lingkaran'''


# Rumus persegi sisi * sisi

sisi1 = 10
sisi2 = 10
luas_p = sisi1 * sisi2

print("luas persegi adalah", luas_p)

# Rumus segitiga A * T / 2

alas = 20
tinggi = 10
luas_s = alas * tinggi / 2

print("luas segitiga adalah", luas_s)

# Rumus jajargenjang A * T

alas = 10
tinggi = 20
luas_j = alas * tinggi

print(" luas jajargenjang adalah", luas_j)

# Rumus lingkaran phi * r * r

phi = 22/7
r = 21
r = 21
luas_l = phi * r * r

print("luas lingkaran adalah",luas_j)



#progam dinamis

print("\n1.luas persegi")
sisi = int(input("Masukan nilai sisi:"))
luas_p = sisi * sisi
print("luas persegi adalah", luas_p)
