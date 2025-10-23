print("""
== PENYYEWAAN RENTAL MOTOR ====
a. Motor Matic
b. motor Trail
c. Motor Sport
""")


while True:
    motor = input("Pilih Jenis Motor (a/b/c) : ").lower
    # subtotal = 0
    
    if motor == "a":
        durasi = int(input("Durasi Penyewaaan (Hari) : "))
        hargasewa = 5000000
        subtotal = hargasewa * durasi
        print(subtotal)
    
    elif motor == "b":
        durasi = int(input("Durasi Penyewaaan (Hari) : "))
        hargasewa = 10000000
        subtotal = hargasewa * durasi
        print(subtotal)
    
    elif motor == "c":
        durasi = int(input("Durasi Penyewaaan (Hari) : "))
        hargasewa = 7500000
        subtotal = hargasewa * durasi
        print(subtotal)
    else:
        print("Tidak ada didaftar")
    
    kupon = input("Silahkan masukan kupon (jika memiliki) : ").lower
    if subtotal >= 15000000:
        diskon = (subtotal * 0.10) - subtotal
    elif  subtotal >= 15000000 or kupon  == "aconkgg":
        diskon = (subtotal * 0.15) - subtotal
        

    lanjut = input ("ingin memesan kembali? (y/n) : ").lower
    if lanjut =="n":
        break
    
    print(diskon)