print ("\n" + "="*80)
print ("program menghitung jumlah huruf vokal, konsonan dan jumlah kata dalam kalimat")
print ("="*80)

kalimat = input("masukkan kalimat: ").lower()

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0

vokal = ["a","i","u","e","o"]
konsonan = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
for i in kalimat:
    if i in vokal:
        jumlah_vokal +=1
    elif i in konsonan:
        jumlah_konsonan +=1
for kata in kalimat.split():
    jumlah_kata = jumlah_kata + 1      
        
print ("jumlah huruf vokal: ", jumlah_vokal)
print ("jumlah huruf konsonan: ", jumlah_konsonan)
print ("jumlah kata dalam kalimat: ", jumlah_kata)
