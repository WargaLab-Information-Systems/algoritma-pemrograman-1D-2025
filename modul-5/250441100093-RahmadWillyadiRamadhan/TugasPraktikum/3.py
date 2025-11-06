while True: 
    def hitung_gaji(nama, jabatan, gaji_pokok):
        pajak = 0.05 * gaji_pokok

        if jabatan.lower() == "manager":
            tunjangan = 0.10 * gaji_pokok
        elif jabatan.lower() == "staff":
            tunjangan = 0.05 * gaji_pokok
        else:
            tunjangan = 0

        gaji_bersih = gaji_pokok - pajak + tunjangan

        print("\n=== HASIL PERHITUNGAN GAJI ===")
        print(f"Nama Karyawan : {nama}")
        print(f"Jabatan       : {jabatan}")
        print(f"Gaji Pokok    : Rp{gaji_pokok:,.0f}")
        print(f"Tunjangan     : Rp{tunjangan:,.0f}")
        print(f"Pajak (5%)    : Rp{pajak:,.0f}")
        print(f"Gaji Bersih   : Rp{gaji_bersih:,.0f}")


    while True:
        nama = input("Masukkan nama karyawan: ")
        if nama.replace(" ", "").isalpha():
            break
        else:
            print("Nama hanya boleh berisi huruf. Silakan coba lagi.")

    while True:
        jabatan = input("Masukkan jabatan (Manager/Staff): ")
        if jabatan.isalpha():
            break
        else:
            print("Jabatan harus huruf. Silakan coba lagi.")

    while True:
            gaji = float(input("Masukkan gaji pokok: "))
            if gaji > 0:
                break
            else:
                print("Gaji harus lebih dari 0.")


    hitung_gaji(nama, jabatan, gaji)
    if input("Apa ada perhitungan lagi? (y/n): ") != "y":
        break