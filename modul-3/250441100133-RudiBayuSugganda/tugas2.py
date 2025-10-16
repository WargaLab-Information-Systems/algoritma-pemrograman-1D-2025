pin_benar = "25133"  
kesempatan = 3
for i in range(kesempatan):
    pin = input("Masukkan PIN Anda: ")
    if pin == pin_benar:
        print("PIN benar, akses diterima ")
        break
    else:
        print("PIN salah, coba lagi ")
else:
    print("Akses ditolak, kartu diblokir ")