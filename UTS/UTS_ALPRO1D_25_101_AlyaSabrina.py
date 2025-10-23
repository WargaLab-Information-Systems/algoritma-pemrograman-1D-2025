while True : 
    motor_matic = 50000
    motor_trail = 100000
    motor_sport = 75000
    asuransi = 15000 
    kupon = "AconkGG"
    total_matic = motor_matic + asuransi
    total_trail = motor_trail+ asuransi
    total_sport = motor_sport + asuransi
    print ("hi! selamat datang di rental motor Aconk")
    input_sewa = input ("anda ingin sewa motor jenis apa ? : ")

    input_voucher = input ("apakah anda memiliki voucher? , jika ya masukkan voucher anda  : ")

    sewa = 72
    hari = sewa / 24 
    if hari > sewa :
        asuransi += 15000
        if total_matic or total_sport or total_sport > 150000 :
            diskon = 0.1 
        if kupon == "AconkGG":
            diskon = 0,5
    total_bayar = total_matic or total_sport or total_trail + diskon  
    print ("total pembayaran anda adalah : Rp. " , total_bayar  )

    