# data_kunjungan = []

# def hanya_huruf(teks):
#     return all(c.isalpha() or c.isspace() for c in teks)

# def input_valid(pesan, cek_huruf=False, pilihan=None):
#     while True:
#         nilai = input(pesan).strip()
#         if not nilai:
#             print(" Tidak boleh kosong!"); continue
#         if cek_huruf and not hanya_huruf(nilai):
#             print(" Hanya boleh huruf dan spasi!"); continue
#         if pilihan and nilai.capitalize() not in pilihan:
#             print(f" Harus salah satu dari: {', '.join(pilihan)}!"); continue
#         return nilai.capitalize() if pilihan else nilai

# def tambah_data():
#     print("\n=== TAMBAH DATA KUNJUNGAN ===")
#     nama_pengunjung = input_valid("Nama pengunjung: ", cek_huruf=True)
#     nama_santri = input_valid("Nama santri yang dijenguk: ", cek_huruf=True)
#     daerah = input_valid("Daerah asal (Sumatra/Kalimantan/Jawa): ", cek_huruf=True,
#     pilihan=["Sumatra", "Kalimantan", "Jawa"])
    
#     while True:
#         id_antrian = input("ID Antrian (angka): ")
#         if not id_antrian.isdigit(): print(" ID harus berupa angka!"); continue
#         if any(d[3] == id_antrian for d in data_kunjungan):
#             print(" ID ini sudah digunakan!"); continue
#         break

#     data_kunjungan.append([nama_pengunjung, nama_santri, daerah, id_antrian])
#     print(" Data berhasil ditambahkan!\n")

# def tampilkan_data():
#     print("\n=== DAFTAR KUNJUNGAN SANTRI ===")
#     if not data_kunjungan: print(" Belum ada data kunjungan.\n"); return
#     for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
#         print(f"\n--- Pengunjung dari {daerah} ---")
#         pengunjung = [d for d in data_kunjungan if d[2].lower() == daerah.lower()]
#         if pengunjung:
#             for d in pengunjung: print(f"ID {d[3]} | {d[0]} menjenguk {d[1]}")
#         else: print("(Belum ada pengunjung dari daerah ini.)")

# def update_data():
#     print("\n=== UPDATE DATA KUNJUNGAN ===")
#     id_edit = input("Masukkan ID Antrian: ")
#     if not id_edit.isdigit(): print(" ID harus berupa angka!"); return
#     for d in data_kunjungan:
#         if d[3] == id_edit:
#             print(f"Data ditemukan: {d}")
#             n = input("Nama pengunjung baru (kosong=skip): ")
#             s = input("Nama santri baru (kosong=skip): ")
#             a = input("Daerah asal baru (kosong=skip): ")
#             if n and hanya_huruf(n): d[0] = n
#             if s and hanya_huruf(s): d[1] = s
#             if a and a.capitalize() in ["Sumatra", "Kalimantan", "Jawa"]: d[2] = a.capitalize()
#             print(" Data berhasil diperbarui!\n"); return
#     print(" ID tidak ditemukan!\n")

# def hapus_data():
#     print("\n=== HAPUS DATA KUNJUNGAN ===")
#     id_hapus = input("Masukkan ID Antrian: ")
#     if not id_hapus.isdigit():
#         print(" ID harus berupa angka!\n")
#         return

#     for d in data_kunjungan:
#         if d[3] == id_hapus:
#             data_kunjungan.remove(d)
#             print(" Data berhasil dihapus!\n")
#             return
#     print(" ID tidak ditemukan!\n")

# while True:
#     print("\nSISTEM KUNJUNGAN SANTRI")
#     print("1. Tambah Data\n2. Tampilkan Data\n3. Ubah Data\n4. Hapus Data\n5. Keluar")
#     pilih = input("Pilih menu [1-5]: ")
#     if not pilih.isdigit(): print(" Masukkan hanya angka 1-5!\n"); continue
#     match int(pilih):
#         case 1: tambah_data()
#         case 2: tampilkan_data()
#         case 3: update_data()
#         case 4: hapus_data()
#         case 5: print(" Program selesai. Terima kasih!"); break
#         case _: print(" Pilihan tidak valid!\n")