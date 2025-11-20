def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = int(gaji_pokok * 0.05)

    if jabatan == "manager":
        tunjangan = int(gaji_pokok * 0.10)
    elif jabatan == "staff":
        tunjangan = int(gaji_pokok * 0.05)
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    :", gaji_pokok)
    print("Pajak (5%)    :", pajak)
    print("Tunjangan     :", tunjangan)
    print("Gaji Bersih   :", gaji_bersih)

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)