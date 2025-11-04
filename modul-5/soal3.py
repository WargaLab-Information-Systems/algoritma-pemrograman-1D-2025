print ("\n" + "="*60)
print ("program menghitung gaji bersih bulanan karyawan")
print ("="*60)

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = int(0.05 * gaji_pokok)

    if jabatan == "manager" :
        tunjangan = int(0.10 * gaji_pokok)
    elif jabatan == "staff" :
        tunjangan = int(0.05 * gaji_pokok)
    else :
        tunjangan = 0

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("===== HASIL PERHITUNGAN GAJI =====")
    print("Nama Karyawan : ", nama)
    print("Jabatan       : ", jabatan)
    print("Gaji Pokok    : ", gaji_pokok)
    print("Tunjangan     : ", tunjangan)
    print("Pajak (5%)    : ", pajak)
    print("Gaji Bersih   : ", gaji_bersih)

nama = input ("masukkan nama karyawan: ")
jabatan = input ("masukkan jabatan: ")
gaji_pokok = int(input("masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)

     


