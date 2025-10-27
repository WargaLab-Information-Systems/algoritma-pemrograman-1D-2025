print("==== PROGRAM MENAMPILKAN KONDISI LAMPU ====")

baris_lamp = int(input("Masukkan jumlah baris lampu: ")) 

for baris in range(1, baris_lamp + 1): 
    jumlah_lamp = int(input(f"Masukkan jumlah lampu di baris ke-{baris}: "))

    for lampu in range(1, jumlah_lamp + 1):
        if lampu % 2 == 0 or lampu % 3 == 0 or lampu % 5 == 0:
            print(f"Lampu baris ke-{lampu} pada baris {baris} rusak")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} nyala") 

if baris == baris_lamp:
    print("Periksa sambungan daya utama") 
