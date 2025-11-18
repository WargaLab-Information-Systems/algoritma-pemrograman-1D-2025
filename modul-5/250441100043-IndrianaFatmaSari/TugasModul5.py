#soal no 1
def faktorial(n):
    hasil = 1
    print(f"Perhitungan faktorial dari {n}: ", end="")
    for i in range(n, 0, -1):
        print(i, end=" x " if i > 1 else "")
        hasil *= i
    print()
    return hasil

n = int(input("Masukkan bilangan: "))
print("Hasil faktorial dari", n, "adalah", faktorial(n))


#soal no 2
def anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False

    cocok = 0
    for huruf in kata1:
        for huruf2 in kata2:
            if huruf == huruf2:
                cocok += 1
                break
    return cocok == len(kata1)

def huruf_saja(teks):
    for c in teks:
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
            return False
    return True

k1 = input("Masukkan kata pertama: ")
k2 = input("Masukkan kata kedua: ")

if not (huruf_saja(k1) and huruf_saja(k2)):
    print("Input hanya boleh huruf tanpa angka atau spasi!")
elif anagram(k1, k2):
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")




# #soal no 3
def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = (gaji_pokok + tunjangan) - pajak

    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp{gaji_pokok}")
    print(f"Tunjangan     : Rp{tunjangan}")
    print(f"Pajak (5%)    : Rp{pajak}")
    print(f"Gaji Bersih   : Rp{gaji_bersih}")


nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)


