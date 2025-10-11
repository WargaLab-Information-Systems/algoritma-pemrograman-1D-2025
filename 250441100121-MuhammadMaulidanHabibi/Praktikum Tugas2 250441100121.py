harga_tiket = 50000
usia = int(input("Masukkan usia Anda: "))
pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")
diskon = 0
if usia < 12:
   diskon = 50
if pelajar == "ya" or pelajar == "Ya":
    if diskon < 30:
        diskon = 30
if hari == "Selasa" or hari == "selasa":
    if diskon < 20:
        diskon = 20
harga_akhir = harga_tiket - (harga_tiket * diskon / 100)
print("Usia Anda:", usia, "tahun")
print("Status Pelajar:", pelajar)
print("Hari:", hari)
print("Diskon:", diskon, "%")
print("Total yang harus dibayar: Rp", int(harga_akhir))
