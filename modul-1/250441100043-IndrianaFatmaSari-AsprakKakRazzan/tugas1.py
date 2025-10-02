#soal 1
total_buku = 3
total_pulpen = 2
harga_buku = 5000
harga_pulpen = 4500
pajak = 0.10 

# hitung total harga sebelum pajak
total_harga_buku = total_buku * harga_buku

total_harga_pulpen = total_pulpen * harga_pulpen

# hitung total semua belanja
total_semua_belanja = total_harga_buku + total_harga_pulpen

#hitung total pajak
total_pajak = total_semua_belanja * pajak 

# hitung harga belanja setelah kena pajak
total_harga_keseluruhan = total_semua_belanja + total_pajak

print("total harga barang = Rp", total_semua_belanja)
print("pajak 10%  = Rp", total_pajak)
print("total yang harus dibayar =", total_harga_keseluruhan)


# soal 2
p = int(input("masukan panjang balok(cm):"))
l = int(input("masukan lebar balok (cm):"))
t = int(input("masukan tinggi balok (cm):"))

volume = p * l * t
luas_permukaan = 2 * (p*l + l*t)

print("volume balok =", volume, "cm3")
print("luas permukaan balok = ", luas_permukaan,"cm2")


#soal 3
bola_merah = 8
bola_biru = 6
bola_diambil = 3
total_bola = bola_merah + bola_biru

#c(14,3) = (14 x 13 x 12) / (3 x 2 x 1)
pembilang = 14 * 13 * 12
penyebut = 3 * 2 * 1
kombinasi = pembilang // penyebut

print("jumlah bola:", total_bola)
print("jumlah kombinasi mengambil 3 bola:", kombinasi)

