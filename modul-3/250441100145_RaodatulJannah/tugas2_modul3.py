pin_ATM = "25145"
kesempatan = 3

while kesempatan > 0:
    pin = input("masukkan PIN (5 digit): ")

    if len(pin) != 5:
        print("PIN harus 5 digit!\n") 
        continue

    if pin == pin_ATM:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan = kesempatan - 1
        print("PIN salah, coba lagi.\n")
        
if kesempatan == 0:
    print("akses ditolak, kartu terblokir")
