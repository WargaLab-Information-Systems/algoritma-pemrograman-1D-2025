# program simulasi mesin ATM

pin_benar = 25051
kesempatan = 3

print("Selamat datang di mesin ATM")

while kesempatan > 0:
    pin_input = int(input("Masukkan pin anda : "))
    
    if pin_input == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
        kesempatan = kesempatan - 1
if kesempatan == 0:
    print("akses ditolak, kartu diblokir")