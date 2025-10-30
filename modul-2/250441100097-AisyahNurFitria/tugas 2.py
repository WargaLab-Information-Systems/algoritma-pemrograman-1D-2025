#program menghitung harga tiket bioskop

#harga tiket normal
harga_normal = 50000

#meminta input dari pengguna
usia = int(input("masukkan usia: "))
pelajar = input("apakah kamu pelajar SMA (ya/tidak)? ").lower()
hari = input("hari menonton: ").lower()

#menentukan besar diskon
diskon = 0  # nilai awal diskon 0%

# Jika anak-anak (<12 tahun), dapat diskon 50%
if usia < 12:
    diskon = 50

#jika pelajar SMA (dengan kartu pelajar), dapat diskon 30%
if pelajar == "ya":
    diskon = max(diskon, 30)  # pilih diskon terbesar

#jika menonton hari Selasa, dapat diskon 20%
if hari == "selasa":
    diskon = max(diskon, 20)  # pilih diskon terbesar

#hitung harga akhir
harga_bayar = harga_normal - (harga_normal * diskon / 100)

# Tampilkan hasil
print("\n=== RINCIAN PEMBAYARAN ===")
print(f"harga normal : Rp{harga_normal:,}")
print(f"diskon        : {diskon}%")
print(f"harga bayar   : Rp{int(harga_bayar):,}")