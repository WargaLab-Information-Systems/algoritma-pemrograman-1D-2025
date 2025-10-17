NIM  = "25101"
for i in range (3) :
    pin = input ("masukkan pin anda : ")

    panjang = 0 
    for angka in pin :
        panjang += 1

        angka = True 
    for karakter in pin :
        if karakter < "0" or karakter  > "9" :
            angka = False 
            break 

    if angka and panjang == 5 and pin == NIM :
        print ("pin benar, akses diterima!")
        break

    if i == 2 :
        print ("akses ditolak, kartu di blokir ! ")
    else :
        print ("pin salah, coba lagi !")