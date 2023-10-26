print("program menghitung luas permukaan dan volume limas segitiga")
""" 
Programmer  : Dissa salwa aurellia
Pertemuan   : 1
Tanggal     : 22 oktober 2023 
""" 
# Nilai 
alas = 70
tinggi = 75
sisi_tegak = 65

# Rumus 
luas_alas = 0.5 * alas * tinggi 
luas_sisi_tegak = 3 * (alas * sisi_tegak) / 2
luas = (luas_alas) + (luas_sisi_tegak)
volume = (luas_alas * tinggi) / 3

# Output 
print("alas :",alas)
print("tinggi :",tinggi)
print("sisi_tegak :",sisi_tegak)
print("luas :",luas)
print("volume :",volume)