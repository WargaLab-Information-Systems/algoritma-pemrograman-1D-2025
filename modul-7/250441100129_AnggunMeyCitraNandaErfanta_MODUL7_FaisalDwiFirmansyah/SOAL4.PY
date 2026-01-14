# Sebuah sekolah memiliki dua klub ekstrakurikuler, yaitu Klub Basket dan Klub Renang. 
# Data anggota kedua klub tersebut disimpan dalam set. 
# Sekolah juga ingin menyimpan informasi tambahan mengenai kedua klub menggunakan dictionary,
# yaitu jumlah pelatih setiap klub.

# Tugas kamu adalah :

# a. Buat dua set berisi nama siswa yang mengikuti Klub Basket dan Klub Renang.
# b. Buat sebuah dictionary yang berisi jumlah pelatih untuk masing-masing kluB
# c. Tampilkan daftar siswa yang mengikuti kedua klub.
# d. Tampilkan daftar siswa yang hanya mengikuti satu klub.
# e. Gunakan dictionary untuk menampilkan kalimat:
# "Klub Basket memiliki X pelatih." dan
# "Klub Renang memiliki Y pelatih."



klub_basket = {"Andi", "Budi", "Citra", "Dewi", "Eka", "Fajar"}
klub_renang = {"Citra", "Dewi", "Gita", "Hadi", "Indra", "Joko"}

info_klub = {
    "basket": 2,
    "renang": 3
}

print(" Daftar Anggota Klub:")
print(f"Klub Basket: {klub_basket}")
print(f"Klub Renang: {klub_renang}")
print()

anggota_kedua_klub = klub_basket & klub_renang
print(" siswa mengikuti kedua klub:")
print(anggota_kedua_klub)
print()

hanya_satu_klub = klub_basket ^ klub_renang
print(" siswa yang mengikuti satu klub:")
print(hanya_satu_klub)
print()

print("informasi pelatih")
print(f"klub renang ada {info_klub['basket']} pelatih.")
print(f"klub renang ada {info_klub['renang']} pelatih.")
print()




