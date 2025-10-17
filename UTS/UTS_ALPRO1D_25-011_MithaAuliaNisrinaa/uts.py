# Bismillah UTS
# Penyewaan Rental Motor Aconk
 
motor_matic = 50000
motor_trail = 100000
motor_sport = 75000

motor = input("Masukkan Jenis Motor yang ingin anda sewa: ")

asuransi = 0
hari = int(input("Masukkan lama hari penyewaan: "))
if hari > 3:
    asuransi = 15000
else:
    asuransi = "Anda Tidak mendapatkan asuransi"

diskon_awal = 0
subtotal = 150000
if subtotal > 15000:
    diskon = 10

kupon = "AconkGG"
kupon_special = input("Masukkan Kupon jika ada: ").lower()
if kupon_special == "AconkGG":
    diskon = 5
else:
    diskon = "Anda Tidak Mendapatkan Diskon"
    breakpoint

for ulang in motor:
    ulang = input( "Apakah Anda ingin menyewa motor lagi (ya / tidak)? ")
if ulang != "ya":
    print("Semua Penyewaan Motor Sudah Selesai. Terima Kasih dan Jangan Lupa Menyewa Kembali")

print("Jenis Motor yang anda sewa yaitu: ", motor)
print("Lama har penyewaan motor yaitu: ", hari)
print("Asuransi yang didapat dari penyewaan motor yaitu: ", asuransi)
print("Diskon yang di dapat yaitu: ", diskon)