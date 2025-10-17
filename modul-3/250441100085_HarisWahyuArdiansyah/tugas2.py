PINBENAR = 25085
kesempatan = 3

for i in range(kesempatan):
    pininput = input("Masukkan PIN (5 digit): ")
    if not pininput.isdigit() or len(pininput) != 5 :
        print("PIN harus berupa 5 digit angka")
        continue
    
    # digunakan untuk mengubah tipe data dari str ke integer
    pin = int(pininput)

    if pin == PINBENAR:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("Akses ditolak, kartu diblokir")
