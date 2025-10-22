# Data barang
harga_buku = int(input("Masukkan Harga Buku:"))
jumlah_buku = int(input("Masukkan Jumlah Buku:"))
harga_pensil = int(input("Masukkan Harga Pensil:"))
jumlah_pensil = int(input("Masukkan Jumlah Pensil:"))

# Hitung total belanja
total = (jumlah_buku * harga_buku) + (jumlah_pensil * harga_pensil)
pajak = float(input("Masukkan pajak yang telah ditetapkan:"))
hasil_pajak = total * pajak 
total_bayar = total + hasil_pajak

# Output
print("Buku Tulis :", jumlah_buku, "x Rp", harga_buku)
print("Pensil     :", jumlah_pensil, "x Rp", harga_pensil)
print("Total Sebelum Pajak    = Rp", total)
print("Pajak                  = Rp", int(hasil_pajak))
print("Total Setelah Pajak    = Rp", int(total_bayar))
