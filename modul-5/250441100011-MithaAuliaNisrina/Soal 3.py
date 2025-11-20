print("Program Menghitung Gaji Bersih Bulanan Karyawan\n")

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = int(0.05 * gaji_pokok)
    if jabatan.lower() == "manager":
        tunjangan = int(0.10 * gaji_pokok)
    elif jabatan.lower() == "staff":
        tunjangan = int(0.05 * gaji_pokok)
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\nHasil Perhitungan Gaji Karyawan")
    print("Nama Karyawan              :", nama)
    print("Jabatan                    :", jabatan)
    print("Gaji Pokok                 : Rp", gaji_pokok)
    print("Tunjangan                  : Rp", tunjangan)
    print("Pajak (5%) dari gaji pokok : Rp", pajak)
    print("Gaji Bersih                : Rp", gaji_bersih)

while True:
    nama = input("Masukkan nama karyawan: ")
    if nama.replace(" ", "").isalpha():
        break
    else:
        print("Input tidak valid! Harap masukkan nama hanya berupa huruf tanpa angka atau simbol.\n")

jabatan = input("Masukkan jabatan (Manager/Staff): ")

while True:
    try:
        gaji_pokok = int(input("Masukkan gaji pokok: "))
        break
    except:
        print("Input tidak valid! Harap masukkan angka untuk gaji pokok.\n")

hitung_gaji(nama, jabatan, gaji_pokok)