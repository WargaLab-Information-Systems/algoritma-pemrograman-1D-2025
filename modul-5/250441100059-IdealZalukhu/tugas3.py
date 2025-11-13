def menghitung_gaji_karyawan(nama_karyawan,jabatan,gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n\tRINCIAN GAJI BULANAN KARYAWAN")
    print(f"Nama karyawan        :", nama_karyawan)
    print(f"Jabatan karyawan     :", jabatan)
    print(f"gaji pokok           : Rp{gaji_pokok:,.0f}")
    print(f"pajak                : Rp{pajak:,.0f}")
    print(f"tunjangan karyawan   : Rp{tunjangan:,.0f}")
    print(f"gaji bersih karyawan : Rp{gaji_bersih:,.0f}")
    
nama_karyawan = input("Masukkan nama karyawan : ")
if any(char.isdigit() for char in nama_karyawan):
    print("Nama karyawan tidak boleh mengandung angka!")
else:
    jabatan = input("Masukkan jabatan karyawan (manager, staff, dan lainnya): ")
    if any(char.isdigit() for char in jabatan):
        print("Jabatan karyawan tidak boleh mengandung angka!")
    else:
        try:
            gaji_pokok = float(input("Masukkan gaji pokok : "))
            menghitung_gaji_karyawan(nama_karyawan, jabatan, gaji_pokok)
        except ValueError:
            print("Gaji pokok harus berupa angka!")

