# TUGAS PRAKTIKUM NO.2

harga_normal = 50000

usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA yang dapat dibuktikan dengan Kartu Pelajar? (ada/tidak): ")
hari = input("Masukkan hari (contoh: Senin, Selasa, dst): ")

diskon = 0
if usia < 12:
    diskon = 50
elif status_pelajar == "ada":
    diskon = 30
elif hari == "Selasa":
    diskon = 20

harga_setelah_diskon = harga_normal - (harga_normal * diskon / 100)

print("\n=== RINCIAN TIKET BIOSKOP ===")
print(f"Usia              : {usia} tahun")
print(f"Status Pelajar    : {status_pelajar}")
print(f"Hari              : {hari}")
print(f"Diskon Diterapkan : {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_setelah_diskon):,}")
