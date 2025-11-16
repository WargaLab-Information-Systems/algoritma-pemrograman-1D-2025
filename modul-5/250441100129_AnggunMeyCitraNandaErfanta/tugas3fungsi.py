def hitung_gaji_bersih(nama, jabatan,gaji_pokok):

    pajak = 0.05*gaji_pokok


    if jabatan.lower() == "manager":
        tunjangan = 0.10* gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05* gaji_pokok
    else:
        tunjangan = 0 

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print ("\n=== hasil perhitungan gaji ===")
    print ("nama karyawan :",nama)
    print ("jabatan        :", jabatan)
    print ("gaji pokok    :",gaji_pokok)
    print ("pajak(5%)     :",pajak)
    print ("tunjangan     :", tunjangan)
    print ("----------------------------")
    print ("gaji bersih   :",gaji_bersih)

print("=== program menghitung gaji bersih karyawan===")
print()
    
nama = input("masukkan nama karyawan: ")
jabatan = input("masukan(manager/staff): ")
gaji_pokok = float (input("masukan gaji pokok: "))


hitung_gaji_bersih(nama,jabatan,gaji_pokok)