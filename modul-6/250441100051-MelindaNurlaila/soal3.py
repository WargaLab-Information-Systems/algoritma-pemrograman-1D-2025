angka = []

def tambah():
    n = int(input("Masukkan angka: "))
    angka.append(n)

def tampilkan():
    print("Daftar angka:", angka)

def ubah():
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin diubah: "))
    if 0 <= idx < len(angka):
        angka[idx] = int(input("Masukkan angka baru: "))
    else:
        print("Indeks tidak valid.")

def hapus():
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin dihapus: "))
    if 0 <= idx < len(angka):
        del angka[idx]
    else:
        print("Indeks tidak valid.")

def cek_bisa_dibagi():
    total = 0
    for i in angka:
        total = total + i

    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi sama)")
        return

    setengah = total // 2
    sum_kiri = 0
    for i in angka:
        sum_kiri += i
        if sum_kiri == setengah:
            print("True (dapat dibagi menjadi dua bagian sama besar)")
            return
    print("False (tidak dapat dibagi dua bagian sama besar)")

while True:
    print("\n=== PROGRAM PEMERIKSAAN ANGKA ===")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek pembagian sama besar")
    print("6. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        tambah()
    elif menu == "2":
        tampilkan()
    elif menu == "3":
        ubah()
    elif menu == "4":
        hapus()
    elif menu == "5":
        cek_bisa_dibagi()
    elif menu == "6":
        print("Terimakasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid.")