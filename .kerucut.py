import math

print("program menghitung luas perkmukaan dan volume kerucut")
""" 
Programmer : Dissa salwa aurellia 
Pertemuan  : 1
Tanggal    : 22 oktober 2023 
""" 
# Nilai 
jari_jari = 5
tinggi = 12 

# Rumus 
sisi_miring = 1/3*(jari_jari**2 + tinggi**2)
luas_lingkaran = math.pi*jari_jari**2
luas_selimut = math.pi*jari_jari*sisi_miring
luas = (luas_lingkaran)+(luas_selimut)
volume =(luas_lingkaran*tinggi)/3

# Output
print("jari_jari :",jari_jari)
print("tinggi :",tinggi) 
print("luas :",luas)
print("volume :",volume)
