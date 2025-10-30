# soal no 1
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))


for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))
    
    for lampu in range(1, jumlah_lampu + 1):
        
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.")



# soal nomor 2
total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    lembur = int(input("Jumlah jam lembur: "))
    shift = input("Shift malam? (y/n): ")

    # Gaji pokok
    gaji = 100_000

    # Hitung lembur
    if lembur <= 3:
        tambahan = lembur * 25000
    elif lembur == 4:
        tambahan = 100000
    elif lembur == 5:
        tambahan = 125000   
    elif lembur == 6:
        tambahan = 200000
    elif lembur == 7:
        tambahan = 225000    
    elif lembur == 8:
        tambahan = 300000
    else:
        tambahan = 0
        print("Lembur melebihi batas, tidak dihitung.")

    gaji += tambahan
    total_lembur += lembur

    # Bonus shift malam
    if shift == 'y':
        gaji += 50000
        total_bonus += 50000

    total_gaji += gaji


print("Total jam lembur :", total_lembur, "jam")
print("Total bonus shift malam : Rp", total_bonus)
print("Total gaji seminggu : Rp", total_gaji)




# soal nomor 3
n = int(input("masukan nilai n: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    
    for k in range(2*(n-i)):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
