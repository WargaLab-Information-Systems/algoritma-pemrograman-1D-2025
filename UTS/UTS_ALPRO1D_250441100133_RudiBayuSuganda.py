rental=input("Sewa motor apa?matic/trail/sport:").lower()
asuransi=int(input("Berapa Hari Sewa:"))
total=0
if rental=="matic":
    bayar=50000
elif rental=="trail":
    bayar=100000
elif rental=="sport":
    bayar=75000
else:
    print("Error")
print(bayar)
if asuransi>=3:
    asuransi=15000
    subtotal=bayar+asuransi
else:
    subtotal=bayar
print(subtotal)
if subtotal>=150000:
    diskon=0.10
else:
    diskon=0
kupon=(input("Masukkan Kupon:"))
if kupon=="AconkGG":
    tambahan=diskon+0.05
else:
    tambahan=0
print()
