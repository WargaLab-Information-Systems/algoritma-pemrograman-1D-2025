
kalimat = input("Masukan sebuah kalimat : ")

hurufvokal = "aiueoAIUEO"
vokal = 0
konsonan = 0

kata = len(kalimat.split())  

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in hurufvokal:
            vokal += 1
        else:
            konsonan += 1
            
print(f"Jumlah Kata : {kata}")
print(f"Jumlah Huruf vokal : {vokal}")
print(f"Jumlah Huruf konsonan : {konsonan}")