# Harga dasar tiket
harga_normal = 50000

# Meminta input dari pengguna
usia = int(input("Masukkan usia Anda: "))
pelajar = input("Apakah Anda punya kartu pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari (contoh: senin, selasa, dst): ").lower()

# Menentukan diskon berdasarkan kondisi
diskon = 0  # awalnya tidak ada diskon

if usia < 12:
    diskon = 50
if pelajar == "ya" and diskon < 30:
    diskon = 30
if hari == "selasa" and diskon < 20:
    diskon = 20

# Menghitung harga akhir
harga_bayar = harga_normal - (harga_normal * diskon / 100)

# Menampilkan hasil
print("\n=== Hasil Perhitungan ===")
print(f"Diskon yang didapat: {diskon}%")
print(f"Harga tiket yang harus dibayar: Rp {harga_bayar:,.0f}")
