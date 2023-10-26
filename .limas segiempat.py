print("program menghitung luas permukaan dan volume limas segiempat")
"""
Programmer  : Dissa salwa aurellia
Pertemuan   : 1
Tanggal     : 22 oktober 2023
"""
# Nilai 
alas = 68
tinggi = 34
sisi_tegak = 36 

# Rumus 
luas_alas = alas*alas
luas_sisi_tegak = 4 * (alas * sisi_tegak) / 2
luas = luas_alas + luas_sisi_tegak
volume = (luas_alas * tinggi) / 3 

# Output
print("alas :",alas)
print("tinggi :",tinggi)
print("sisi_tegak :",sisi_tegak) 
print("luas :",luas)
print("volume :",volume)