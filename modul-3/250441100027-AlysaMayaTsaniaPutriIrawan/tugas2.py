print ("\n" + "="*60)
print ("program simulasi sederhana mesin ATM")
print ("="*60)

pin_ATM = 25027 
kesempatan = 3

while kesempatan > 0:
    PIN = int(input("masukkan pin anda (5 digit) : "))
    
    if PIN == pin_ATM:
        print ("PIN benar, akses diterima")
        break
    else:
        kesempatan = kesempatan  - 1
        if kesempatan > 0:
            print ("PIN salah, coba lagi")
        else : 
            print("Akses ditolak. kartu diblokir")


