# Repository praktikum Algoritma Pemrograman 1A-2025

**Repository Praktikum ALPRO-1A-2025.**

Kumpulkan Tugas di folder ini yang sudah dibuat, penamaan folder dengan **format NIM-NamaLengkap-NamaLengkapAsprak**, dan untuk nama tidak menggunakan spasi, namun diganti dengan huruf kapital di setiap nama atau awal kalimat
contoh: **230441100026-Ar'raffiAbqoriNurAzizi-AsprakKakRapi**

Kumpulkan tugas yang sudah dibuat di folder yang sudah disediakan dan kumpulkan tugas ketika sudah melakukan asistensi kepada Asisten Praktikum.

penjelasan program :

Pendefinisian Variabel
motor_matic = "50000"
motor_trail = "1000000"
motor_sport = "75000"

asuransi = "15000"
lama_sewa = "3"
Pada bagian ini, terdapat tiga jenis motor dengan harga yang berbeda, yaitu:

- Motor matic: 50.000
- Motor trail: 1.000.000
- Motor sport: 75.000

Selain itu ada juga biaya asuransi dan lama sewa.
Namun, semua nilai tersebut masih dalam bentuk string (teks) karena menggunakan tanda kutip " ".
Artinya, nilai ini belum bisa digunakan untuk operasi matematika seperti penjumlahan atau perkalian.

Variabel `value`

value = ("pilih jenis motor yang mau di sewa (matic/trail/spor)")

Bagian ini hanya menyimpan teks ke dalam variabel value.
Kode ini tidak meminta input dari pengguna, karena tidak memakai fungsi input().
Jadi program hanya menampilkan tulisan, bukan meminta pilihan dari user.

Struktur Perulangan while

while motor_matic > 3:
total = asuransi + "jenis"
print(total)

Percabangan if

if total > 50000:
diskon = 0.10

Baris ini bertujuan untuk memberikan diskon 10% jika total lebih dari 50.000.
Namun, karena `total` belum didefinisikan dengan benar, kondisi ini tidak akan berjalan seperti yang diharapkan.

Kode Kupon

kupon ="AconkGG"
diskon = 0.5

Bagian ini mendefinisikan kode kupon “AconkGG” dan memberi nilai diskon 50%.
Namun belum ada logika if yang memeriksa apakah kupon tersebut dimasukkan oleh pengguna atau tidak, jadi nilai ini hanya disimpan tanpa fungsi tertentu.
