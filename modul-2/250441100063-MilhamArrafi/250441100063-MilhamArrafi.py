# Program Menghitung Harga Tiket Bioskop

harga_normal = 50000
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

diskon = 0

# Menentukan diskon terbesar yang berlaku
if usia < 12:
    diskon = 50
if pelajar == "ya" and diskon < 30:
    diskon = 30
if hari == "selasa" and diskon < 20:
    diskon = 20

# Menghitung harga akhir
harga_bayar = harga_normal - (harga_normal * diskon / 100)

print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_bayar)}")


#modul3


# Program Menghitung Biaya Parkir Mall

# Input data dari pengguna
lama = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (Ya/Tidak): ")

# Cek apakah VIP
if vip == "Ya":
    total = 0
else:
    # Jika bukan VIP
    if lama <= 2:
        total = 5000
        #kalau bukan itu, maka laukan yang ini
    else:
        total = 5000 + (lama - 2) * 3000

    # Batasi maksimal biaya parkir
    if total > 20000:
        total = 20000

# Tampilkan hasil
print(f"Total biaya parkir: Rp{total}")