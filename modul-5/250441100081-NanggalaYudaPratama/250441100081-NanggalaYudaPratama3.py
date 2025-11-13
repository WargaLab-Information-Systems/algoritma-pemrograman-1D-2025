while True:
    while True:
        nama = input("Masukkan nama karyawan: ")
        if'0' in nama or '1' in nama or '2' in nama or '3' in nama or '4' in nama or '5' in nama or '6' in nama or '7' in nama or '8' in nama or '9' in nama:
            print("Peringatan: Nama mengandung angka, kemungkinan typo.")
            continue
        elif nama.isupper():
            print("Catatan: Nama semuanya huruf besar.")
            continue
        elif nama.islower():
            print("Catatan: Nama semuanya huruf kecil.")
            continue
        else:
            break
        

    while True:
        jab = input("Masukkan jabatan (Manager/Staff): ")
        if'0' in jab or '1' in jab or '2' in jab or '3' in jab or '4' in jab or '5' in jab or '6' in jab or '7' in jab or '8' in jab or '9' in jab:
            print("Peringatan: Jabatan mengandung angka, kemungkinan typo.")
            continue
        elif jab.isupper():
            print("Catatan: Jabatan semuanya huruf besar.")
            continue
        elif jab.islower():
            print("Catatan: Jabatan semuanya huruf kecil.")
            continue
        elif jab != "Manager" or jab != "Staff":
            print("Tidak sesuai dengan pilihan jabatan karyawan!")
            continue
        else:
            break

    while True:
        gaji_pokok = int(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji tidak boleh minus!")
            continue
        else:
            break  
        

    def gaji(gaji_pokok, jabatan):
        pajak = 0.05
        jab = jabatan.strip().lower()
        if jab == "manager":
            tunj = 0.1
        elif jab == "staff":
            tunj = 0.05

        tunjangan = tunj * gaji_pokok
        bruto = gaji_pokok + tunjangan
        neto = bruto - (pajak * bruto)
        return neto

    gaji_bersih = gaji(gaji_pokok, jab)
    print(f"karyawan atas nama {nama} dengan jabatan {jab} menerima gaji bersih sebesar {gaji_bersih:,.2f}")
    

    lanjut = input("Apakah ingin lanjut (y/n): ")
    if lanjut == "n":
        break
