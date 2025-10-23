motor_matic = 50000
motor_trail = 100000
motor_sport = 75000
asuransi = 15000
diskon = 0.1
diskon_tambahan = 0.2
subtotal = 150000
nama_kupon = "AconkGG".lower()

while True:
    nama = input("Masukkan nama penyewa: ")
    jenis_motor = input("Masukkan jenis motor (motor matic/motor trail/motor sport): ")
    harga_sewa = int(input("Masukkan harga sewa: "))
    jumlah_hari = int(input("Masukkan jumlah hari sewa: "))
    break

total_harga = harga_sewa * jumlah_hari 
subttotal = total_harga
if jumlah_hari >= 3:
        asuransi_berkelipatan = (jumlah_hari/3) * 15000 
if subtotal <= 150000:
        subtotal = total_harga - diskon

if diskon_kupon = "AconkGG".lower()
    diskon_kupon = total_harga - diskon_tambahan 