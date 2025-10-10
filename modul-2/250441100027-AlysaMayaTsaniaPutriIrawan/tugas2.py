# menentukan harga tiket

tiket_normal = 50000
usia = int(input("masukkan usia: "))
status = input("apakah anda pelajar SMA : ")
hari = input ("masukkan hari menonton: ")

# diskon
if usia < 12 :
    diskon = 0.50 
elif status == "ya" :
    diskon = 0.30 
elif hari == "selasa" :
    diskon = 0.20 
else : 
    diskon = 0

harga_tiket = (tiket_normal-(tiket_normal * diskon))
print ("harga tiket yang harus dibayar = Rp", int(harga_tiket))


        