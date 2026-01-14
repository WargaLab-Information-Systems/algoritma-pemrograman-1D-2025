# Seorang pelatih ingin mencatat waktu lari 100 meter dari dua kelompok atlet berbeda,
#  yaitu Kelompok Pagi dan Kelompok Sore.
# Data waktu (dalam detik) disimpan dalam bentuk list. Pelatih ingin:
# Menggabungkan waktu dari kedua kelompok menggunakan operasi concatenation (+).
# Mengetahui jumlah total data waktu yang digabung menggunakan len().
# Memeriksa apakah ada waktu 10 detik dalam data gabungan (menggunakan membership in).
# Menyimpan hasil akhir dalam bentuk tuple berisi (jumlah_data, ada_waktu_10).

# kelompok_atlet = ("klompok1 ,kelompok2")
# data_gabungan = kelompok_pagi+ kelompok_sore

kelompok_pagi =[6.30,8.10,9.00,10.10]
kelompok_sore = [2.20,3.10,4.00,5.40]

data_gabungan = kelompok_pagi+ kelompok_sore

jumlah_data =len(data_gabungan)

ada_waktu_10= 10 in data_gabungan
hasil_akhir=(jumlah_data,ada_waktu_10)

print(f"data pagi:{kelompok_pagi}")
print(f"data sore: {kelompok_sore}")
print(f"hasil gabungan: {data_gabungan}")

print(f"jumlah data:{jumlah_data}")

print(f"hasil :{hasil_akhir}")







    