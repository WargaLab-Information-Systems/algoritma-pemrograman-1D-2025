def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0
    
    gaji_kotor = gaji_pokok + tunjangan
    pajak = 0.05 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    return gaji_bersih, tunjangan, pajak

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff/Lainnya): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

gaji_bersih, tunjangan, pajak = hitung_gaji_bersih(nama, jabatan, gaji_pokok)

print(f"Jabatan       : {jabatan}")
print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
print(f"Tunjangan     : Rp {tunjangan:,.2f}")
print(f"Pajak (5%)    : Rp {pajak:,.2f}")
print(f"Gaji Bersih   : Rp {gaji_bersih:,.2f}")