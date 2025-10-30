ulang = "iya"

while ulang.lower()== "iya" :

    harga = 0

    rental = input("Pilihlah motor yang akan di rental! (Motor Matic/Motor Trail/Motor Sport) : ")

    if rental.lower() == "motor matic" :
        print ("50.000,00")
    elif rental.lower() == "motor trail":
        print ("100.000,00")
    elif rental.lower() == "motor sport" :
        print ("75.000,00")
    else:
        print()
        ulang = input("Apakah ada yang mau disewa lagi? iya/tidak : ")