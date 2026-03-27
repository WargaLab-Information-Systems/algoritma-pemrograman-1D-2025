def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = gaji_pokok * 0.05

    if jabatan == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan  :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    :", gaji_pokok)
    print("Pajak (5%)    :", pajak)
    print("Tunjangan     :", tunjangan)
    print("Gaji Bersih   :", gaji_bersih)

nama = input("siapa nama karyawan: ")
jabatan = str(input("apa jabatan (manager/staff): "))
gaji_pokok = float(input("berapa gaji pokok: "))

# hitung_gaji(nama, jabatan,gaji_pokok)

