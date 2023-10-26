import math

print("program menghitung luas permukaan dan volume selinder(tabung)")
"""
Programmer : Dissa salwa aurellia
Pertemuan  : 1
Tanggal    : 22 oktober 2023 
""" 
# Nilai 
jari_jari = 10
tinggi = 30 

# Rumus 
luas_selimut = math.pi*jari_jari**2
luas_lingkaran = 2*math.pi*jari_jari*tinggi
luas = 2*(luas_selimut + luas_lingkaran)
volume = (luas_lingkaran)*(tinggi)

# Output 
print("jari_jari :",jari_jari)
print("tinggi :",tinggi)
print("luas :",luas)
print("volume :",volume)
