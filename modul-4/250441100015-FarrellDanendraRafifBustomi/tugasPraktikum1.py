jumlah_baris = int(input("Masukkan jumlah baris lampu: "))  

# input manual untuk menentukan lampu yang mati
# baris_mati = int(input("Lampu mati ada di baris ke berapa? "))
# lampu_mati = int(input("Lampu ke berapa yang mati di baris tersebut? "))
# end input manual untuk menentukan lampu yang mati

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{baris}: "))

#     # perulangan untuk setiap lampu dalam baris dan ada yang mati
#     for lampu in range(1, jumlah_lampu + 1):
#         if baris == baris_mati and lampu == lampu_mati:
#             print(f"Lampu ke-{lampu} pada baris {baris} mati.")
#         elif lampu % 3 == 0:
#             print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
#         else:
#             print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
#     # end perulangan untuk setiap lampu dalam baris dan ada yang mati

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        #kondisi jika lampu mati, jika kelipatan kelima
        # elif lampu % 5 == 0:                      
        #     print(f"Lampu ke-{lampu} pada baris {baris} mati.")
        # end kondisi jika lampu mati, jika kelipatan kelima
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.\n")
    else:
        print("")  