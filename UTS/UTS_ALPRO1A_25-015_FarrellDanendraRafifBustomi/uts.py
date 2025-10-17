sewaMotorMatic = 50000
sewaMotorTrail = 100000
sewaMotorSport = 75000
asuransi = 15000
kupon = 0.5


print('---Selamat datang di Penyewaan Rental Motor Aconk---')

motor = (str(input("Pilih jenis motor yang ingin anda sewa: Motor Matic, Motor Trail, Motor Sport: ")))
sewa = (int(input("Berapa hari anda sewa: ")))

if motor == "motor matic":
    print("Motor yang anda sewa: ", motor)

elif motor == "motor trail":
    print("Motor yang anda sewa: ", motor)

elif motor == "motor sport":
    print("Motor yang anda sewa: ", motor)

else:
    print("Motor tidak ditemukan")



if motor == "motor matic" and sewa > 3:
    harga = sewaMotorMatic + asuransi
    print("Anda mendapatkan Asuransi sebesar 15.000: ", harga)

elif motor == "motor matic" and sewa > 3:
    harga = sewaMotorMatic + asuransi
    print("Anda mendapatkan Asuransi sebesar 15.000: ", harga)

elif motor == "motor matic" and sewa > 3:
    harga = sewaMotorMatic + asuransi
    print("Anda mendapatkan Asuransi sebesar 15.000: ", harga)

else:
    print("Anda tidak mendapatkan asuransi")
