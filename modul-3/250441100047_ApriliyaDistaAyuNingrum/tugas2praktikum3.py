# Simulasi ATM 
PIN_BENAR = 25047
kesempatan = 3 

print("Selamat datang di ATM!")
print("Masukkan PIN (tepat 5 digit angka, tanpa spasi):")

while kesempatan > 0:  
    pin = input("PIN: ")  
    if pin == PIN_BENAR:  
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
        kesempatan = kesempatan - 1
if kesempatan == 0:
    print("Akses ditolak, kartu diblokir")
