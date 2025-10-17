kalimat = input ("masukkan kalimat anda : ")

vokal = 0 
konsonan = 0 
kata = 1

for huruf in kalimat :
    if huruf in "aiueo":
        vokal = vokal + 1 
    elif huruf != " " and huruf != "." and huruf != "," :
        konsonan = konsonan + 1
    elif huruf == " " :
        kata = kata + 1 

print ("jumlah huruf vokalnya adalah : " , vokal)
print ("jumlah huruf konsonan nya adalah : " , konsonan )
print ("jumlah katanya adalah : " , kata)