print("=== Program Kasir Apotek Fuad Farma ===")
print("Masukkan harga obat satu per satu.")
print("Ketik 0 jika sudah selesai.\n")

total_harga = 0     # Menyimpan total harga semua obat
jumlah_obat = 0     # Menghitung berapa banyak obat yang dibeli

while True:
    harga = float(input("Masukkan harga obat (0 untuk selesai): "))

    if harga == 0:
        break  # Menghentikan perulangan jika kasir memasukkan 0

    total_harga += harga   # Menambahkan harga ke total
    jumlah_obat += 1       # Menambah jumlah obat

# Menampilkan hasil perhitungan
print("\n=== Hasil Perhitungan ===")
if jumlah_obat > 0:
    rata_rata = total_harga / jumlah_obat
    print(f"Total harga seluruh obat : Rp{total_harga:.0f}")
    print(f"Jumlah obat yang dibeli  : {jumlah_obat} obat")
    print(f"Rata-rata harga obat     : Rp{rata_rata:.0f}")
else:
    print("Tidak ada obat yang dibeli.")
