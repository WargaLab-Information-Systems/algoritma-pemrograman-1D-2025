usia = int(input("masukkan usia anda : "))
status =input ("apakah status anda pelajar SMA yang memiliki kartu pelajar? (ya/tidak) : ")
hari = input("pada hari apa anda menonton? : ")

harga_tiket = 50000  
diskon = 0

if usia < 12 :
    diskon = max(diskon,0.5)
elif status == "ya" : 
    diskon = max (diskon, 0.3)
elif hari == "selasa" : 
    diskon = max (diskon, 0.2) 
else :
    print ("tidak ada diskon")

total_bayar = harga_tiket * (1-diskon)

print ("total yang harus dibayarkan adalah : " , total_bayar )

