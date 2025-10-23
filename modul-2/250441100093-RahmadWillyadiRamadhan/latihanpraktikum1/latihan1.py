nomor_acak = 7
print ('tebak nomor acak dari 1 - 10')
tebakan = int(input('tebakan anda (bil bulat): '))
if tebakan == nomor_acak:
    print ('selamat! tebakan anda benar')
    print ('tapi tidak ada hadiah untuk anda :(')
elif tebakan < nomor_acak:
    print ('tebakan anda terlalu kecil')
else:
    print ('tebakan anda terlalu besar')
    print ('selesai')