# menentukan total biaya parkir 

lama_parkir = int(input("masukkan lama parkir(jam): "))
member = input("apakah anda member vip (ya/tidak)?: ")

if member == "ya" :
    biaya = 0 
else : 
    if lama_parkir <= 2:
        biaya = 5000
    else : 
        biaya = 5000 + (lama_parkir - 2)*3000
        if biaya > 20000: 
            biaya = 20000

print ("total biaya parkir yang harus dibayar =Rp ", biaya)