jumlah_baris = int(input("Masukkan jumlah baris:"))
jumlah_lampu_perbaris = int(input("Masukkan jumlah lampu per baris:"))

for baris  in range(1, jumlah_baris + 1):
    for lampu in range(1, jumlah_lampu_perbaris + 1):
        if lampu % 3 == 0:
            print("lampu ke:",lampu, "pada baris ke:", baris, "rusak.Periksa sambungan daya utama")
        else:
            print("lampu ke:",lampu, "pada baris ke:", baris, "menyala", )