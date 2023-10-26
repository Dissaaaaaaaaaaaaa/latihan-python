print("program menghitung luas permukaan dan volume prisma segitiga")
"""
Programmer  : Dissa salwa aurellia 
Pertemuan   : 1
Tanggal     : 22 oktober 2023
""" 
# Nilai 
alas = 70
tinggi = 35
sisi_tegak = 38

# Rumus 
luas_alas = 0.5 * alas * tinggi 
luas_sisi_tegak = 3 * (alas * sisi_tegak)
luas = 2 * (luas_alas + luas_sisi_tegak)
volume = (luas_alas) * (sisi_tegak)

# Output 
print("alas :",alas)
print("tinggi :",tinggi)
print("sisi_tegak :",sisi_tegak)
print("luas :",luas)
print("volume :",volume)