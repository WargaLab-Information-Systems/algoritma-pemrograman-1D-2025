print ("\n" + "="*60)
print ("Program pemeriksaan angka ")
print ("="*60)

angka = []

def tambah_angka():
    n = (input("Masukkan angka: "))
    for i in n :
        angka.append(int(i))

def tampilkan_angka():
    print("Daftar angka:", angka)

def ubah_angka():
    if not angka :
        print("tidak boleh selain angka harus angka!\n")
        return
    
    tampilkan_angka()
    urut = int(input("Masukkan indeks angka yang ingin diubah: "))
    if 0 <= urut < len(angka):
        angka[urut] = int(input("Masukkan angka baru: "))
    else:
        print("Indeks tidak valid.")

def hapus_angka():
    if not angka :
        print("tidak boleh selain angak! harus angka!\n")
        return
    
    tampilkan_angka()
    urut = int(input("Masukkan indeks angka yang ingin dihapus: "))
    if 0 <= urut < len(angka):
        del angka[urut]
    else:
        print("Indeks tidak valid.")

def cek_bisa_dibagi():
    if not angka :
        print("tidak boleh selain angka! harus angka!\n")
        return
    
    total = 0
    for i in angka:
        total += i

    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi sama)")
        return

    setengah = total // 2
    bagian_kiri = 0
    for i in angka:
        bagian_kiri += i
        if bagian_kiri == setengah:
            print("True (dapat dibagi menjadi dua bagian sama besar)")
            return
    print("False (tidak dapat dibagi dua bagian sama besar)")

while True:
    print("\n=== PROGRAM PEMERIKSAAN ANGKA ===")
    print("1. Tambah angka (create)")
    print("2. Tampilkan angka (read)")
    print("3. Ubah angka (update)")
    print("4. Hapus angka(delete)")
    print("5. Cek pembagian sama besar")
    print("6. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_angka()
    elif menu == "2":
        tampilkan_angka()
    elif menu == "3":
        ubah_angka()
    elif menu == "4":
        hapus_angka()
    elif menu == "5":
        cek_bisa_dibagi()
    elif menu == "6":
        break
    else:
        print("Pilihan tidak valid.")