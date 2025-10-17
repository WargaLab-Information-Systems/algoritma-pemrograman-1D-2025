while True: 
    motor_matic = 50000
    motor_trail = 100000
    motor_sport = 75000
    
    asuransi = 15000
    lama_sewa = 3
    total = 0
    
    jenis = input("Pilih jenis motor yang akan di sewa (matic/trail/sport) : ")
    lama = (input("Berapa lama hari penyewaan : "))

    while jenis == motor_matic:
        total = motor_matic
    if jenis == motor_sport:
        total = motor_sport
    if jenis == motor_trail : 
         total = motor_trail

    elif lama_sewa > 3:
        total = asuransi + jenis

        if total > 150000:
            diskon = 0.10

        kupon = "AconkGG"
        diskon_tambahan = input("Masukkan kupon : ")
        if diskon_tambahan == kupon:
            diskon = 0.5

    print("Totalnya adalah : ", total)

    sewa_lagi = input("Apakah ada penyewaan lagi? (y/n) : ")
    if sewa_lagi == "n":
        break
