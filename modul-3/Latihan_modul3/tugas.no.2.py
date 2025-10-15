pin_benar = 25071
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