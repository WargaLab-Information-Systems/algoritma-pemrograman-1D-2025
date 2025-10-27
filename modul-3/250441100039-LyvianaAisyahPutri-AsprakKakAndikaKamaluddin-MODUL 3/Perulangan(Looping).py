#praktikum latihan
# a = 1
# while a<5:
#     print (a)
#     a += 1

# a=0
# while a<10:
#     a+=1
#     if a%2:
#        print("%d bilangan ganjil" %a)
#     else:
#         continue

# a=1
# while a<10:
#     print(a)
#     a+=1
#     if a>6:
#         break

# while 1:
#     print("perulangan tiada batas, tekan ^c untuk berhenti ")

# bulan={'januari', 'februari', 'maret', 'april', 'mei'}
# for a in bulan.value():
#     print(a)


#TUGAS PRAKTIKUM 
# 1.) Dalam matematika, bilangan prima merupakan bilangan asli lebih besar dari
# 1 yang hanya memiliki dua faktor yaitu 1 dan bilangan itu sendiri. Buatkan
# program untuk menampilkan bilangan prima dari 1 sampai n.

# N = int(input("Masukkan nilai N: "))
# print("Bilangan prima dari 1 sampai", N, "adalah:")
# for angka in range(2, N + 1):  
#     cek = True  

#     for i in range(2, angka):  
#         if angka % i == 0:
#             cek = False
#             break  
#     if cek:  
#         print(angka, end=" ")


# # #2 . ) Buatlah simulasi sederhana dari mesin ATM yang meminta user untuk
# # memasukkan PIN(XXYYY(X = 2 NIM awal, Y = 3 NIM terakhir)). User
# # memiliki kesempatan 3 kali untuk measukkan PIN yang benar. Jika PIN
# # benar, Tampilkan pesan “PIN benar, akses diterima”, jika salah, maka
# # tampilkan pesan “PIN salah, coba lagi”. Jika sudah 3 kali salah, tampilkan
# # pesan “Akses ditolak, kartu diblokir”. PIN harus diinput dalam bentuk angka
# # dan harus 5 digit.
# # # Simulasi PIN ATM (Format: 2 digit NIM awal + 3 digit NIM akhir)

# pin_benar = input("Masukkan PIN asli : ")
# percobaan = 0

# while percobaan < 3:
#     pin_input = input("Masukkan PIN: ")
#     if pin_input == pin_benar:
#         print("PIN benar, akses diterima")
#         break
#     else:
#         percobaan += 1
#         if percobaan < 3:
#             print("PIN salah, coba lagi")
#         else:
#             print("Akses ditolak, kartu diblokir")


# # 3.) Buatlah program yang meminta user untuk memasukkan sebuah kalimat.
# # Lalu program akan menganilsa kalimat tersebut dan menampilkan :
# # a. Jumlah huruf vokal dan konsonan
# # b. Jumlah kata dalam kalimat

# kalimat = input("Masukkan sebuah kalimat: ")

# vokal = "aiueoAIUEO"
# jumlah_vokal = 0
# jumlah_konsonan = 0
# jumlah_kata = 1  

# for huruf in kalimat:
#     if huruf in vokal:
#         jumlah_vokal += 1
#     elif huruf != " " and huruf not in vokal: 
#         jumlah_konsonan += 1

#     if huruf == " ":
#         jumlah_kata += 1

# print("Jumlah huruf vokal:", jumlah_vokal)
# print("Jumlah huruf konsonan:", jumlah_konsonan)
# print("Jumlah kata:", jumlah_kata)



# # Ambaki adalah seorang developer di sebuah IndoMei. Ambaki diminta untuk
# # membuat program yang menampilkan struk pembelian setiap pelanggan.
# # Program tersebut akan meminta input berupa nama pembeli, daftar barang
# # yang dibeli, dan harga dari setiap barang. Setelah itu, program akan
# # menampilkan struk pembelian yang berisi nama pembeli, daftar barang
# # beserta harganya, total harga keseluruhan, serta pesan “Terima kasih telah
# # berbelanja di IndoMei.” Program akan terus meminta input dari kasir untuk
# # pelanggan berikutnya hingga kasir memasukkan (y/n) pada pertanyaan
# # “Apakah ada pembeli berikutnya?”.

# while True:
#     nama = input("Masukkan nama pembeli: ")
#     total_harga = 0
#     daftar_barang = []

#     while True:
#         barang = input("Masukkan nama barang: ")
#         harga = int(input("Masukkan harga barang: "))
#         daftar_barang.append((barang, harga))
#         total_harga += harga

#         lagi = input("Tambah barang lagi? (y/n): ")
#         if lagi.lower() != 'iya':
#             break

#     print("\n===== STRUK PEMBELIAN =====")
#     print("Nama pembeli:", nama)
#     print("--------------------------")
#     for item, hrg in daftar_barang:
#         print(f"{item} - Rp{hrg}")
#     print("--------------------------")
#     print("Total Harga: Rp", total_harga)
#     print("Terima kasih telah berbelanja di IndoMei!")
#     print("===========================\n")

#     lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
#     if lanjut.lower() != 'ya':
#         break












