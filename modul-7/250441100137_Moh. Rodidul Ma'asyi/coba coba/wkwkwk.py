# mahasiswa = {"Andi": 85, "Radit": 98, "Dwi": 90, "Nia": 87}

# # Mencari nilai tertinggi
# tertinggi_key = max(mahasiswa, key=lambda x: mahasiswa[x])
# tertinggi_nilai = mahasiswa[tertinggi_key]

# # Menghitung rata-rata
# rata_rata = sum(mahasiswa.values()) / len(mahasiswa)

# print("Mahasiswa dengan nilai tertinggi :", tertinggi_key, "=", tertinggi_nilai)
# print("Rata-rata nilai mahasiswa        :", rata_rata)

# Warga_lab = {"Anam", "Radit", "Dani", "Rafael"}
# anggota_BEM = {"Radit", "Dani"}

# # Pengunjung yang juga anggota UKM (intersection)
# aktif = Warga_lab.intersection(anggota_BEM)

# # Gabungan semua nama tanpa duplikasi (union)
# semua_orang = Warga_lab.union(anggota_BEM)

# # Pengunjung yang bukan anggota UKM (difference)
# non_BEM = Warga_lab.difference(anggota_BEM)

# print("Aktif BEM dan Warga Lab :", aktif)
# print("Total nama unik         :", semua_orang)
# print("Bukan anggota BEM       :", non_BEM)

a = {"nama": "Andi"}
b = a.copy()
b["nama"] = "Budi"
# a tetap {"nama": "Andi"}, tidak ikut berubah

# dict = {25081: "angga", 25113: "hawwin"}
# print(dict[25081], "ini sebelum diubah")

# dict[25081] = "lia"

# print(dict[25081], "ini usai diubah")

# del dict [25113]
# print(dict)

# dict.clear()
# print(dict)

# set1 = set()
# set1.add(1)
# print(set1)

# himp1 = {1,2,3,4,}
# himp2 = {3,4,5,6,7,8,9,}

# gabung = himp1.union(himp2)
# print(gabung)

# ambil = himp1.intersection(himp2)
# print(ambil)

# pisah = himp2.difference(himp1)
# print(pisah)

# copy = himp2.symmetric_difference(himp1)
# print(copy)

