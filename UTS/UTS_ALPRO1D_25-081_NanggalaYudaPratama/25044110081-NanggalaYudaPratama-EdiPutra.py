MotorMatic = 50000
MotorTrail = 100000
MotorSport = 75000
harga = 0

while True: 
    print("Rental Motor Aconk :")
    print("1. Motor Matic")
    print("2. Motor Trail")
    print("1. Motor Sport")
    print("="*30)

    jmotor = int(input("Masukkan 3 pilihan jenis motor (1-3): "))
    lamaSewa = int(input("Masukkan lama sewa: "))


    if jmotor == 1:
        harga = MotorMatic
    elif jmotor == 2:
        harga = MotorTrail
    else:
        harga = MotorSport

    total = harga
    print(f"Harga total: {harga:,}")
    if total > 150000:
        subtotal = total + (total*0.10)
    # for i in range(lamaSewa):

    kupon = input("Masukkan Kode Promo (n jika tidak ada): ")
    if kupon == "n":
        total = harga + (harga*0.5)
    elif kupon == "AconkGG":
        total = harga + (harga*0.5)

lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
if lanjut != 'y':
    print("\nProgram selesai. Semua transaksi telah diproses.")
    break
