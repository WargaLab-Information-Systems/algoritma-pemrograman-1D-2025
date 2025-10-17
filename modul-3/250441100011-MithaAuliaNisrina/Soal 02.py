# Program simulasi sederhana mesin ATM

pin_benar = 25011
kesempatan = 3

while kesempatan > 0:
    pin = int(input("Masukkan PIN Anda (5 digit): "))

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan = kesempatan - 1
        if kesempatan > 0:
            print("PIN salah, coba lagi. Kesempatan tersisa:", kesempatan)
        else:
            print("Akses ditolak, kartu diblokir.")