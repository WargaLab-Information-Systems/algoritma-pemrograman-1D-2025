print("====Perhitungan Bola yang Diambil====")

banyak_bola_merah= 8
banyak_bola_biru= 6 
diambil_bola= 3

total_bola_dikotak= banyak_bola_merah + banyak_bola_biru
total_bola_yang_diambil= diambil_bola

import math
kombinasi_bola = math.comb(total_bola_dikotak, total_bola_yang_diambil)
print("Total kombinasi bola yang diambil adalah:", kombinasi_bola)
