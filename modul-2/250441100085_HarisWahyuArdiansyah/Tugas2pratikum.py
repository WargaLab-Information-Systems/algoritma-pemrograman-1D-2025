# soal no 2

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")

harganormal = 50000
diskon = 0

if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20

diskon_usia = 50 if usia < 12 else 0
diskon_pelajar = 30 if pelajar == "ya" else 0
diskon_hari = 20 if hari == "selasa" else 0
diskon_terbesar = max(diskon_usia, diskon_pelajar, diskon_hari)

harga_bayar = harganormal - (harganormal * diskon_terbesar / 100)

print(f"Diskon yang diterapkan : {diskon_terbesar}")
print(f"Total harga tiket yang harus dibayar: Rp{harga_bayar}")