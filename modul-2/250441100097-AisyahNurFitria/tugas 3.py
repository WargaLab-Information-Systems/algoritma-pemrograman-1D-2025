lama_parkir = int(input("berapa lama anda parkir (jam) : "))
status = input ("apakah anda member VIP (ya/tidak) : ")
biaya = 0

hari = lama_parkir // 24
sisa_jam = lama_parkir % 24
biaya = hari * 20000

if status == "ya" :
    biaya = 0
else :
    if sisa_jam <=2 :
        biaya += 50
    else :
        biaya += 5000 + (sisa_jam - 2) * 3000
    if biaya > (hari + 1) * 20000 :
        biaya = (hari + 1) * 20000

print ("total biaya parkir anda adalah :" , biaya )