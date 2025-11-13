# angka = []  
# def hitung_panjang(data):
#     hitung = 0
#     for _ in data:
#         hitung += 1
#     return hitung

# def ubah_ke_angka(teks):
#     negatif = False
#     hasil = 0
#     i = 0
#     if teks != "":
#         if teks[0] == "-":
#             negatif = True
#             i = 1
#         while i < hitung_panjang(teks):
#             hasil = hasil * 10 + (ord(teks[i]) - 48)
#             i += 1
#     if negatif:
#         hasil = 0 - hasil
#     return hasil

# def tambah_data(data, nilai):
#     data_baru = []
#     for x in data:
#         data_baru += [x]
#     data_baru += [nilai]
#     return data_baru

# def hapus_data(data, nilai):
#     data_baru = []
#     sudah_hapus = False
#     for x in data:
#         if x == nilai and not sudah_hapus:
#             sudah_hapus = True
#         else:
#             data_baru += [x]
#     return data_baru

# def ubah_data(data, posisi, nilai_baru):
#     data_baru = []
#     i = 0
#     while i < hitung_panjang(data):
#         if i == posisi:
#             data_baru += [nilai_baru]
#         else:
#             data_baru += [data[i]]
#         i += 1
#     return data_baru

# def total_data(data):
#     total = 0
#     for x in data:
#         total += x
#     return total

# def cek_bagi_sama(data):
#     n = hitung_panjang(data)
#     if n < 2:
#         print("Data terlalu sedikit.")
#         return

#     i = 1
#     ada_sama = False 
#     while i < n:
#         kiri = []
#         kanan = []
#         j = 0
#         while j < n:
#             if j < i:
#                 kiri = tambah_data(kiri, data[j])
#             else:
#                 kanan = tambah_data(kanan, data[j])
#             j += 1

#         if total_data(kiri) == total_data(kanan):
#             print("True - bisa dibagi:", kiri, "dan", kanan)
#             ada_sama = True
#         i += 1

#     if not ada_sama:
#         print("False - tidak ada pembagian dengan jumlah sama")

# while True:
#     print("\n=== MENU DERET ANGKA ===")
#     print("1. Tambah angka")
#     print("2. Tampilkan angka")
#     print("3. Ubah angka")
#     print("4. Hapus angka")
#     print("5. Cek pembagian dua bagian sama")
#     print("6. Keluar")

#     pilih = input("Pilih menu [1-6]: ")

#     if pilih == "1":
#         teks = input("Masukkan angka: ")
#         valid = True
#         for c in teks:
#             if not (c >= "0" and c <= "9") and c != "-":
#                 valid = False
#         if valid:
#             nilai = ubah_ke_angka(teks)
#             angka = tambah_data(angka, nilai)
#             print("Angka ditambahkan!")
#         else:
#             print("Input harus berupa angka!")

#     elif pilih == "2":
#         print("Data angka:")
#         if hitung_panjang(angka) == 0:
#             print("Belum ada data.")
#         else:
#             i = 0
#             while i < hitung_panjang(angka):
#                 print("Posisi", i, ":", angka[i])
#                 i += 1

#     elif pilih == "3":
#         if hitung_panjang(angka) == 0:
#             print("Belum ada data untuk diubah.")
#         else:
#             print("Data sekarang:")
#             i = 0
#             while i < hitung_panjang(angka):
#                 print(i, ":", angka[i])
#                 i += 1

#             pos = input("Masukkan posisi yang ingin diubah: ")
#             if all(c >= "0" and c <= "9" for c in pos):
#                 pos_angka = ubah_ke_angka(pos)
#                 if pos_angka < hitung_panjang(angka):
#                     baru = input("Masukkan nilai baru: ")
#                     if all(c >= "0" and c <= "9" for c in baru):
#                         nilai_baru = ubah_ke_angka(baru)
#                         angka = ubah_data(angka, pos_angka, nilai_baru)
#                         print("Data berhasil diubah!")
#                     else:
#                         print("Nilai harus angka!")
#                 else:
#                     print("Posisi tidak valid!")
#             else:
#                 print("Posisi harus angka!")

#     elif pilih == "4":
#         if hitung_panjang(angka) == 0:
#             print("Belum ada data untuk dihapus.")
#         else:
#             val = input("Masukkan angka yang ingin dihapus: ")
#             if all(c >= "0" and c <= "9" for c in val):
#                 nilai = ubah_ke_angka(val)
#                 angka = hapus_data(angka, nilai)
#                 print("Data berhasil dihapus!")
#             else:
#                 print("Input harus angka!")

#     elif pilih == "5":
#         cek_bagi_sama(angka)

#     elif pilih == "6":
#         print("Program selesai.")
#         break

#     else:
#         print("Pilihan tidak valid.")