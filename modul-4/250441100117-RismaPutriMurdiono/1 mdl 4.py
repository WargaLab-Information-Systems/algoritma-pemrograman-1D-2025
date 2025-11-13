# # Meminta input jumlah baris lampu
# jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# # Perulangan untuk setiap baris
# for baris in range(1, jumlah_baris + 1):
#     # Meminta input jumlah lampu di setiap baris
#     jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))

#     # Perulangan untuk setiap lampu dalam baris
#     for lampu in range(1, jumlah_lampu + 1):
#         # Mengecek apakah nomor lampu kelipatan 3
#         if lampu % 3 == 0:
#             print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
#         else:
#             print(f"Lampu ke-{lampu} pada baris {baris} menyala.")

#     # Jika baris terakhir, tambahkan pesan tambahan
#     if baris == jumlah_baris:
#         print("Periksa sambungan daya utama.\n")
#     else:
#         print()  # Baris kosong sebagai pemisah antar baris


jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")

    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.\n")
    else:
        print()
