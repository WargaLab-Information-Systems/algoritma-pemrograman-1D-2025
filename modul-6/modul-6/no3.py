angka_list = []

def create():
    n = int(input("Masukkan jumlah angka yang ingin ditambahkan: "))
    for i in range(n):
        angka = int(input(f"Masukkan angka ke-{i+1}: "))
        angka_list.append(angka)
    print("Data berhasil ditambahkan!")

def read():
    print("Daftar angka saat ini:", angka_list)

def update():
    read()
    index = int(input("Masukkan indeks angka yang ingin diubah: "))
    if 0 <= index < len(angka_list):
        nilai_baru = int(input("Masukkan nilai baru: "))
        angka_list[index] = nilai_baru
        print("Data berhasil diubah!")
    else:
        print("Indeks tidak valid!")

def delete():
    read()
    index = int(input("Masukkan indeks angka yang ingin dihapus: "))
    if 0 <= index < len(angka_list):
        del angka_list[index]
        print("Data berhasil dihapus!")
    else:
        print("Indeks tidak valid!")
 
def cek_pembagian_sama():
    total = sum(angka_list)
    if total % 2 != 0:
        print("False — jumlah total ganjil, tidak bisa dibagi dua sama besar.")
        return False
    
    setengah = total // 2
    temp = 0
    for i in range(len(angka_list)):
        temp += angka_list[i]
        if temp == setengah:
            print("True — bisa dibagi dua bagian dengan jumlah sama besar.")
            return True
    print("False — tidak bisa dibagi dua bagian dengan jumlah sama besar.")
    return False

while True:
    print("\n=== MENU CRUD & CEK PEMBAGIAN ===")
    print("1. Tambah data (Create)")
    print("2. Tampilkan data (Read)")
    print("3. Ubah data (Update)")
    print("4. Hapus data (Delete)")
    print("5. Cek pembagian dua bagian sama jumlah")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
        update()
    elif pilihan == "4":
        delete()
    elif pilihan == "5":
        cek_pembagian_sama()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")