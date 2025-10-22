motor_matic = 50000
motor_trail = 100000
motor_sport = 75000




sewa_motor = (input("nama motor yang ingin anda sewa :"))
berapa_hari =int(input("berapa hari ingin menyawa motor :"))

if sewa_motor == "matic":
    harga = 50000
elif sewa_motor = "sport":
    harga = 75000
elif sewa_motor = "trail":
else:
    print("tidak ada pilihan")

    subtotal = harga * berapa_hari

    if subtotal > 15000:
        diskon1 = subtotal * 0.10
    else:
        diskon1 = 0

if kupon == "AnconkGG":
    diskon2 = subtotal + diskon1 * 0.05
else:
    diskon2 = 0

    total = subtotal + diskon + diskon2


print("total :", total)
print("harga sewa :", harga )
print("diskon :", diskon)




