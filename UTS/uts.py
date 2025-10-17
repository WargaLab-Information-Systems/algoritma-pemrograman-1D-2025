print ("perhitungan harga jenis motor")
 
motor_matic = 50000
motor_trail = 1000000
motor_sport = 75000

ulang = "y" 
batas_sewa = 3 

   
jumlah= 0
total = 0
kupon = "AcongkGG"

while ulang == "y":
   jenis_motor = print("masukkan jenis motor : ")
   jumlah_motor = print("berapa jumlah motor yang ingin di sewa")
 
   
   if jumlah >= 3:
    asuransi = 15000

    if total >= 150000:
      diskon = 0.10
    elif kupon == "AconkGG":
      diskon = 0.5

total = jenis_motor * jumlah_motor
 


print("apakah anda ingin menyewa motor lagi (y/n)").lower()
print("terimakasih sudah menyewa motor di RENTAL MOTOR ACONK")

