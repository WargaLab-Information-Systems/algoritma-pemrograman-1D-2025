# saol no 1
contact_book = {}

def validasi_nama(nama):
    if nama.strip() == "":
        return False
    return all(ch.isalpha() or ch == " " for ch in nama)

def validasi_telp(telp):
    if telp == "":
        return False
    if len(telp) < 12 or len(telp) > 13:
        return False
    return all('0' <= ch <= '9' for ch in telp)

def validasi_email(email):
    if email == "":
        return False
    
    ada_at = False
    ada_titik = False

    i = 0
    while i < len(email):
        if email[i] == '@':
            ada_at = True
        if email[i] == '.':
            ada_titik = True
        i += 1
    
    return ada_at and ada_titik


while True:
    print("===== CONTACT BOOK =====")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        if not contact_book:
            print("Belum ada kontak.")
        else:
            for telp, data in contact_book.items():
                print(f"Nama  : {data['nama']}")
                print(f"Telp  : {telp}")
                print(f"Email : {data['email']}")

   
    elif pilih == "2":
        nama_cari = input("Nama yang dicari: ").strip()
        if not validasi_nama(nama_cari):
            print("Nama tidak valid!")
            continue
        
        ditemukan = False
        for telp, data in contact_book.items():
            if data['nama'].lower() == nama_cari.lower():
                print("Kontak ditemukan:")
                print("Nama  :", data["nama"])
                print("Telp  :", telp)
                print("Email :", data["email"])
                ditemukan = True
        
        if not ditemukan:
            print("Kontak tidak ditemukan.")

 
    elif pilih == "3":
        nama = input("Masukkan nama: ").strip()
        if not validasi_nama(nama):
            print("Nama tidak valid!")
            continue
        
        telp = input("Masukkan nomor telepon: ").strip()
        if not validasi_telp(telp):
            print("Nomor telepon tidak valid!")
            continue


        if telp in contact_book:
            print("Nomor telepon sudah digunakan!")
            continue
        
        email = input("Masukkan email: ").strip()
        if not validasi_email(email):
            print("Email tidak valid!")
            continue


        email_dipakai = False
        for data in contact_book.values():
            if data["email"] == email:
                email_dipakai = True
                break
        if email_dipakai:
            print("Email sudah digunakan kontak lain!")
            continue

        contact_book[telp] = {"nama": nama, "email": email}
        print("Kontak berhasil ditambahkan!")


    elif pilih == "4":
        telp = input("Masukkan nomor telepon kontak yang ingin diupdate: ").strip()
        if telp not in contact_book:
            print("Kontak tidak ditemukan!")
            continue

        email_baru = input("Masukkan email baru: ").strip()
        if not validasi_email(email_baru):
            print("Email tidak valid!")
            continue

     
        email_dipakai = False
        for t, data in contact_book.items():
            if t != telp and data["email"] == email_baru:
                email_dipakai = True
                break

        if email_dipakai:
            print("Email tersebut sudah digunakan kontak lain!")
            continue

        contact_book[telp]["email"] = email_baru
        print("Email berhasil diperbarui!")


    elif pilih == "5":
        telp = input("Nomor telepon kontak yang ingin dihapus: ").strip()
        if telp in contact_book:
            del contact_book[telp]
            print("Kontak berhasil dihapus!")
        else:
            print("Kontak tidak ditemukan.")


    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")





#soal no 2
inventaris = {}
next_id = 1   

while True:
    print("===== INVENTARIS GUDANG =====")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        if len(inventaris) == 0:
            print("Belum ada data barang.")
        else:
            print("--- Daftar Barang ---")
            for id_barang, data in inventaris.items():
                print(f"ID: {id_barang} | Nama: {data[0]} | Harga: {data[1]} | Stok: {data[2]}")

    elif pilihan == "2":
        cari = input("Masukkan ID barang: ")
        if cari in inventaris:
            barang = inventaris[cari]
            print(f"Nama: {barang[0]}, Harga: {barang[1]}, Stok: {barang[2]}")
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")

    elif pilihan == "3":
    
        id_baru = str(next_id)
        next_id += 1

        nama = input("Masukkan nama barang: ")
        harga = input("Masukkan harga barang: ")
        stok = input("Masukkan stok barang: ")

        try:
            harga = int(harga)
            stok = int(stok)
        except:
            print("Harga dan stok harus berupa angka!")
            continue

        if stok < 0 or harga < 0:
            print("Harga dan stok tidak boleh negatif!")
        else:
            inventaris[id_baru] = [nama, harga, stok]
            print(f"Barang berhasil ditambahkan dengan ID {id_baru}!")

    elif pilihan == "4":
        id_update = input("Masukkan ID barang yang ingin diupdate stoknya: ")

        if id_update in inventaris:
            try:
                stok_baru = int(input("Masukkan stok baru: "))
            except:
                print("Stok harus berupa angka!")
                continue

            if stok_baru < 0:
                print("Stok tidak boleh negatif!")
                continue

            inventaris[id_update][2] = stok_baru
            print("Stok berhasil diperbarui!")
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")

    elif pilihan == "5":
        id_hapus = input("Masukkan ID barang yang ingin dihapus: ")

        if id_hapus in inventaris:
            del inventaris[id_hapus]
            print("Barang berhasil dihapus!")

            inventaris_baru = {}
            id_baru = 1

            for key in inventaris:
                inventaris_baru[str(id_baru)] = inventaris[key]
                id_baru +=1

            inventaris = inventaris_baru
            next_id = id_baru
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")



# # soal no 3
kupon = {} 

def tampilkan_semua_kupon():
    if not kupon:
        print("Tidak ada kupon.")
    else:
        print("--- Daftar Kupon ---")
        for code, disc in kupon.items():
            print(f"Kode Kupon : {code}")
            print(f"Diskon     : {disc}%")
            print("-----------------------")

def tambah_kupon():
    code = input("Masukkan kode kupon baru: ")
    if code in kupon:
        print("Kode kupon sudah ada.")
        return

    disc = int(input("Masukkan persentase diskon: "))
    if disc <= 0 or disc >= 100:
        print("Diskon harus 1-99%.")
        return

    kupon[code] = disc
    print("Kupon berhasil ditambahkan.")

def hapus_kupon():
    code = input("Masukkan kode kupon yang ingin dihapus: ")
    if code in kupon:
        del kupon[code]
        print("Kupon berhasil dihapus.")
    else:
        print("Kupon tidak ditemukan.")

def proses_transaksi():
    items = []
    while True:
        name = input("Masukkan nama barang (atau 'selesai'): ")
        if name.lower() == "selesai":
            break
        price = int(input(f"Masukkan harga barang '{name}': "))
        items.append((name, price))
    
    if not items:
        print("Tidak ada barang.")
        return

    total = sum(price for _, price in items)
    print("\n--- Daftar Barang ---")
    for name, price in items:
        print(f"{name}: Rp {price}")
    print(f"Total Belanja: Rp {total}")

    
    pakai_kupon = input("Apakah ingin menggunakan kupon? (y/n): ").lower()
    if pakai_kupon == "y":
        code = input("Masukkan kode kupon: ")
        if code not in kupon:
            print("Kupon tidak valid.")
        else:
            discount_percent = kupon[code]
            discount_amount = total * (discount_percent / 100)
            total -= discount_amount
            del kupon[code]
            print(f"Diskon {discount_percent}% diterapkan. Potongan: Rp {discount_amount:.2f}")
            print("Kupon dihapus setelah penggunaan.")
    
    print(f"Total Akhir: Rp {total:.2f}")

while True:
    print("\n====== SISTEM KUPON & KASIR ======")
    print("1. Tampilkan semua kupon")
    print("2. Tambah kupon")
    print("3. Hapus kupon")
    print("4. Mode kasir (transaksi)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_semua_kupon()
    elif pilihan == "2":
        tambah_kupon()
    elif pilihan == "3":
        hapus_kupon()
    elif pilihan == "4":
        proses_transaksi()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")