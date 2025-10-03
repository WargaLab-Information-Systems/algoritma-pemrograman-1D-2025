print ("soal 4 : contoh operasi aritmatika ")

a = 11
b = 2

hasil_penjumlahan = a + b 
print ( a, "+", b , "=", hasil_penjumlahan)

hasil_pengurangan = a - b 
print (a, "-", b, "=", hasil_pengurangan )

hasil_perkalian = a * b
print (a,"*", b, "=", hasil_perkalian )

hasil_pembagian = a / b 
print (a,"/", b, "=", hasil_pembagian)

hasil_modulus = a % b 
print (a,"%",b, "=", hasil_modulus)

print ("soal 5 : menghitung sisa uang ") 

harga_buku = 45000
harga_pulpen = 7500

jumlah_buku = 3
jumlah_pulpen = 2

total_buku = harga_buku * jumlah_buku 
total_pulpen = harga_pulpen * jumlah_pulpen

total_belanja = total_buku + total_pulpen 

jumlah_uang = 200000

sisa_uang = jumlah_uang - total_belanja

print (total_buku, "+" , total_pulpen,"=", total_belanja ) 
print ("sisa uang nya adalah :" , sisa_uang )


#quiz
NIM = 101
celcius = NIM 

fahrenheit = (celcius * 1.8) + 32 
kelvin = celcius + 273.15

print("NIM saya adalah : " ,NIM ,"konversi fahrenheitnya : ", fahrenheit ,"konversi kelvinnya : ", kelvin )