def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("=====================================")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp",gaji_pokok)
    print("Tunjangan     : Rp",tunjangan)
    print("Pajak (5%)    : Rp",pajak)
    print("-------------------------------------")
    print("Gaji Bersih   : Rp",gaji_bersih)
    print("=====================================")

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji)