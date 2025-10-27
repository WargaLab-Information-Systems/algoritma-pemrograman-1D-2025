
# Program menampilkan dua piramida angka yang saling berhadapan

jumlah_baris = int(input("Masukkan jumlah baris piramida: "))  
lebar_angka = len(str(jumlah_baris)) + 1

for baris in range(1, jumlah_baris + 1):

    # untuk sisi kiri piramida
    for i in range(1, baris + 1):
        print(f"{i:>{lebar_angka}}", end="")

    # untuk spasi di tengah 
    jumlah_spasi = (jumlah_baris - baris) * 2 * lebar_angka
    for j in range(jumlah_spasi):
        print(" ", end="")

    # untuk sisi kanan piramida
    for k in range(baris, 0, -1):
        print(f"{k:>{lebar_angka}}", end="")
    print()
