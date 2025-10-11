
# menghitung total belanja setelah pajak ditetapkan pajak
print ("===jawaban===")
# hitung total belanja 
harga_perbuku = int(input("masukkan harga perbuku: "))
harga_perpensil = int(input("masukkan harga perpensil: "))

jumlah_buku = int(input("masukkan jumlah buku: "))
jumlah_pensil = int(input("masukkan jumlah pensil: "))
total_harga = (jumlah_buku*harga_perbuku) + (jumlah_pensil*harga_perpensil)
print ("total harga barang keseluruhan =", total_harga)

# total belanja setelah pajak ditetapkan
pajak = float(input("masukkan pajak yang telah ditetapkan: "))
total_pajak = (total_harga * pajak)
total_biaya = (int(total_harga + total_pajak))
print ("total biaya yang harus dibayar setelah pajak ditetapkan =", total_biaya)