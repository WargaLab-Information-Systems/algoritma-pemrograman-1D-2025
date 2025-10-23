#Program rental motor Aconk

while True:
    print("\n=== RENTAL MOTOR ACONK ===")
    print("1.motor_matic  = Rp50.000/hari")
    print("2.motor_trail  = Rp100.000/hari")
    print("3.motor_sport  = Rp75.000/hari")

    jenis = input("masukkan jenis motor (matic/trail/sport): ").lower()
    lama = int(input("masukkan lama sewa (hari): "))

    #harga sewa per jenis motor
    if jenis == "matic":
        harga = 50000
    elif jenis == "trail":
        harga = 100000
    elif jenis == "sport":
        harga = 75000
    else:
        print("Jenis motor tidak tersedia!")
        continue