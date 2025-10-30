print ("=== WELCOME TO RENTAL MOTOR ACONK ===")

asuran = 15000
diskon = 10.0
diskon_kupon = 5.0

trail = 100000
sport = 75000
matic = 50000

jenis = input("Masukkan Jenis Motor Anda (Trail, Sport, Matic): ").lower
asuransi= int(input("Sewa ke- :"))

if jenis == trail:
    print(" Harga Sewa = 10000")
elif jenis == sport:
    print("Harga Sewa 75000")
else:
    print("Harga Sewa 50000")

if asuransi == 3:
    print("Asuransi Sebesar:", asuran)
elif asuransi > 3:
    print("Asuransi Sebesar:", asuran + 5.0)
else: 
    print ("Asuransi 0")

cek_diskon = input("Masukkan Voucher: ")

if cek_diskon == "AconkGG":
    print("Anda Mendapatkan Diskon Tambahan Sebesar 5%")
elif cek_diskon != "AconkGG":
    print("Anda Tidak Mendapatkan Diskon")


