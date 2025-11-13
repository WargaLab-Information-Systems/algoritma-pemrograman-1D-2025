# Program menghitung total belanja (dinamis)
# Input harga dan jumlah barang
harga_buku = int(input("Masukkan harga buku   : Rp "))
jumlah_buku = int(input("Masukkan jumlah buku  : "))
harga_pensil = int(input("Masukkan harga pensil : Rp "))
jumlah_pensil = int(input("Masukkan jumlah pensil: "))
# Hitung total harga sebelum pajak
total_harga = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)
# Hitung pajak 10%
pajak = total_harga * 0.10
# Hitung total setelah pajak
total_setelah_pajak = total_harga + pajak
# Tampilkan hasil
print("=== RINCIAN BELANJA ===")
print("Total harga sebelum pajak : Rp", total_harga)
print("Pajak 10%                 : Rp", int(pajak))
print("Total harga setelah pajak : Rp", int(total_setelah_pajak))
