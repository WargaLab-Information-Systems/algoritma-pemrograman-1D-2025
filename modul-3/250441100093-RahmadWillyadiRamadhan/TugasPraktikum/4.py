while True:
    # Meminta nama pembeli (hanya huruf dan spasi)
    while True:
        nama = input("Masukkan nama pembeli: ")
        if nama.replace(" ", "").isalpha():
            break
        else:
            print("Nama hanya boleh huruf! Silakan coba lagi.")

    barang_list = []
    harga_list = []

    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
        if barang.lower() == "selesai":
            break

        # Pastikan nama barang dimulai huruf dan hanya huruf/angka
        if not (barang[0].isalpha() and barang.replace(" ", "").isalnum()):
            print("Nama barang harus dimulai dengan huruf dan setelah itu bisa diahiri angka!")
            continue

        try:
            harga = float(input(f"Masukkan harga {barang}: "))
        except ValueError:
            print("Harga harus berupa angka! Silakan ulangi.")
            continue

        barang_list.append(barang)
        harga_list.append(harga)

    total = sum(harga_list)

    print("\n====== STRUK PEMBELIAN ======")
    print(f"Nama Pembeli : {nama}")
    print("-----------------------------")
    for i in range(len(barang_list)):
        print(f"{i+1}. {barang_list[i]} \t Rp{harga_list[i]:,.0f}")
    print("-----------------------------")
    print(f"Total Harga  : Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("=============================\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != "y":
        print("Program selesai. Sampai jumpa!")
        break
    print()


# append()	Menambahkan data ke akhir list	barang_list.append("Sabun")
# sum()	Menjumlahkan semua angka dalam list	sum([3000, 5000]) → 8000
# lower()	Mengubah huruf besar jadi kecil semua	"YA".lower() → "ya"
# break	Menghentikan perulangan (loop)	keluar dari while
# f-string (f"…")	Menampilkan teks dengan nilai variabel	f"Nama: {nama}"
# \t
# Itu adalah tab (spasi lebar), seperti tombol Tab di keyboard.
# Gunanya untuk merapikan jarak antara nama barang dan harga agar struk terlihat sejajar.
# Fungsi len() menghitung berapa banyak kata di dalam daftar tersebut.
# Jadi kata = 3