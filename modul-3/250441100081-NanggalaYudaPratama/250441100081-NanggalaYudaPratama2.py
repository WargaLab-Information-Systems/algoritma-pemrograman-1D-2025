pin_benar = 25081
kesempatan = 3

for i in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")

    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else: 
        print("PIN salah, coba lagi")
if i == kesempatan - 1:
    print("Akses ditolak, kartu diblokir")