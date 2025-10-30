
hari = 7
totalgaji = 0
totallembur = 0
total_bonusshift = 0

for harike in range(1, hari+1):  
    print()
    print(f" Hari ke {harike} ")
    

    while True:
        try: 
            jamlembur = int(input("Masukkan jumlah jam lembur: "))
            if jamlembur < 0:
                print("Jam lembur tidak boleh negatif!")
                continue 
            break
        except ValueError:
            print("input yang anda masukan tidak valid")
    

    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam not in ['y', 'n']:
            print("Input tidak valid!")
            continue
        break
    

    if shift_malam == 'y':
        bonusshift = 50000 
    else:
        bonusshift = 0
    

    gajiharian = 100000


    if jamlembur == 0:
        tambahanlembur = 0
    elif 1 <= jamlembur <= 3:
        tambahanlembur = jamlembur * 25000
    elif jamlembur == 4:
        tambahanlembur = 100000
    elif jamlembur == 5:
        tambahanlembur = 125000
    elif jamlembur == 6:
        tambahanlembur = 200000
    elif jamlembur == 7:
        tambahanlembur = 225000
    elif jamlembur == 8:
        tambahanlembur = 300000
    elif jamlembur > 8:
        print("Lembur melebihi batas")
        tambahanlembur = 0
    else:
        tambahanlembur = 0

    totalharian = gajiharian + tambahanlembur + bonusshift
    totalgaji += totalharian
    totallembur += jamlembur
    total_bonusshift += bonusshift
    


print(f"Total jam lembur             : {totallembur} jam")
print(f"Total bonus dari shift malam : Rp{total_bonusshift}")
print(f"Total gaji dalan seminggu    : Rp{totalgaji}")