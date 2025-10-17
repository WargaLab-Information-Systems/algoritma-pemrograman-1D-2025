#modul 3
#soal 1



n = int(input("Masukkan nilai n: "))

print("Bilangan prima dari 1 sampai", n, "adalah:")

for angka in range(2, n + 1):      
    prima = True                  
    for pembagi in range(2, angka):
        if angka % pembagi == 0:   
            prima = False           
            break
    if prima:
        print(angka, end= " ")



        #MODUL3
#SOAL2



pin_benar = "12345"      
kesempatan = 3             

for i in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")
    
    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")


else:
    print("Akses ditolak, kartu diblokir.")



#MODUL3
#SOAL3

kalimat = str(input("Masukkan sebuah kalimat: "))

vokal = "aeiou"
jumlah_huruf_vokal = 0
jumlah_huruf_konsonan = 0
jumlah_kata = 0

for karakter in kalimat:
    if karakter.isalpha(): 
        if karakter in vokal:
            jumlah_huruf_vokal += 1
        else:
            jumlah_huruf_konsonan += 1


kata = kalimat.split() 
jumlah_kata = len(kata)


print("Kalimat :", kalimat)
print("Jumlah huruf vokal     :", jumlah_huruf_vokal)
print("Jumlah huruf konsonan  :", jumlah_huruf_konsonan)
print("Jumlah kata            :", jumlah_kata)