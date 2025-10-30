Nbaris = int(input("Masukan jumlah baris lampu : "))

for baris in range(1,Nbaris+1):
    jumlahlampu = int(input(f"Masukan Jumlah lampu pada baris {baris} : "))
    
    for lampu in range (1,jumlahlampu+1):
        if lampu % 3 == 0:
            print(f"Lampu ke {lampu} pada baris {baris} Rusak")
        else:
            print(f"Lampu ke {lampu} pada baris {baris} Menyala")
    
    if baris == Nbaris:
        print("Periksa sambungan daya utama")