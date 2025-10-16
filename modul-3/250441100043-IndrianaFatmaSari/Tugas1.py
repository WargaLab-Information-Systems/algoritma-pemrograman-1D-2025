# soal no 1
n = int(input("masukan batas angka: "))

print("bilangan prima dari 1 sampai", n, ":")

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break

    else:
            print(i)



# #soal 2
pin_benar = 25043
kesempatan = 3

for i in range(kesempatan):
    pin = int(input("masukan PIN : "))

    if pin == pin_benar:
         print("PIN benar, akses diterima")
         break
    else:
         if i < 2:
              print("PIN salah, coba lagi!")
         else:
              print("Akses ditolak, kartu diblokir")





# soal 3
kalimat = input("masukan kalimat: ")

vokal = 0
konsonan = 0
kata = 1

for huruf in kalimat:
     if huruf in "aiueo":
          vokal += 1
     elif huruf in "bcdfghjklmnpqrstvwxyz":
          konsonan += 1
     elif huruf == " ":
          kata += 1



print("Vokal:", vokal)
print("konsonan:", konsonan)
print("jumlah kata:", kata)




# #soal 4
while True:
    nama = input("Nama pembeli: ")
    total = 0

    while True:
        barang = input("Nama barang: ")
        harga = int(input("Harga: "))
        total += harga
       
        if input("Tambah barang lagi? (y/n):"):
            break

    
    print("Pembeli:", nama)
    print("Total: Rp", total)
    print("daftar barang :", barang)
    print("Terima kasih telah berbelanja di IndoMei")

    if input("Ada pembeli berikutnya? (y/n): "):
        print("Program selesai.")
        break







