def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("========== RINCIAN GAJI ==========")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,}")
    print(f"Pajak (5%)    : Rp {pajak:,}")
    print(f"Tunjangan     : Rp {tunjangan:,}")
    print(f"Gaji Bersih   : Rp {gaji_bersih:,}")
    print("===================================")


nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan : ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)