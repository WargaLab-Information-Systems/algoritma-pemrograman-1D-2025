PIN = 25059
kesempatan = 3

for i in range(kesempatan):
    pin = int(input("Masukkan PIN anda :"))

    if pin == PIN:
        print("PIN benar akses diterima")
        break
    else:
        print("PIN salah, coba lagi\n")

else:
    print("Akses ditolak, kartu di blokir")