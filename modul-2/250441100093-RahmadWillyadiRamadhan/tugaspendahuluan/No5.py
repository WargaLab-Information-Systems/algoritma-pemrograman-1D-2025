# Program Tarif Jalan Tol

print("=== PROGRAM TARIF JALAN TOL ===")
print("Pilih jenis kendaraan:")
print("1. Mobil Pribadi (Rp15.000)")
print("2. Truk Kecil    (Rp25.000)")
print("3. Truk Besar    (Rp40.000)")

# --- Input Jenis Kendaraan ---
pilih = int(input("Masukkan pilihan (1/2/3): "))

if pilih == 1:
    tarif = 15000
    kendaraan = "Mobil Pribadi"
elif pilih == 2:
    tarif = 25000
    kendaraan = "Truk Kecil"
elif pilih == 3:
    tarif = 40000
    kendaraan = "Truk Besar"
else:
    print("Pilihan salah!")
    exit()

# --- Input Metode Pembayaran ---
bayar = input("Bayar pakai apa? (e-money/tunai): ").lower()

# --- Input Jam Pembayaran ---
jam = int(input("Masukkan jam (0-23): "))

# --- Tentukan Diskon ---
if bayar == "e-money":
    if jam >= 23 or jam < 5:   # Jam sepi (23.00 - 05.00)
        diskon = 20
    else:
        diskon = 10
elif bayar == "tunai":
    diskon = 0
else:
    print("Metode pembayaran salah!")
    exit()

# --- Hitung Total Bayar ---
potongan = tarif * (diskon / 100)
total = tarif - potongan

# --- Tampilkan Hasil ---
print("=== RINCIAN PEMBAYARAN ===")
print("Jenis Kendaraan :", kendaraan)
print("Tarif Dasar     : Rp", tarif)
print("Metode Bayar    :", bayar)
print("Jam Pembayaran  :", jam, ":00")
print("Diskon          :", diskon, "%")
print("Total Bayar     : Rp", int(total))
