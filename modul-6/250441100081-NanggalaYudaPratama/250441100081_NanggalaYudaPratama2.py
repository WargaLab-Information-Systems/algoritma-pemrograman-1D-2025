while True:
    print("Masukkan Hanya Angka (contoh: 3,1,4)")
    while True:
        t1 = input("Masukkan angka tuple pertama yang dipisahkan oleh koma: ")
        if t1.isalpha():
            print("Tidak boleh berupa huruf!")
            continue
        else:
            break

    while True:
        t2 = input("Masukkan angka tuple kedua yang dipisahkan oleh koma: ")
        if t2.isalpha():
            print("Tidak boleh berupa huruf!")
            continue
        else:
            break

    t1 = t1.replace("(","").replace(")","").replace(" ","").split(",")
    t2 = t2.replace("(","").replace(")","").replace(" ","").split(",")

    t1 = tuple(int(i) for i in t1)
    t2 = tuple(int(i) for i in t2)

    gabung = t1 + t2

    unik = []
    for x in gabung:
        if x not in unik:
            unik.append(x)

    for i in range(len(unik)):
        for j in range(i + 1, len(unik)):
            if unik[i] < unik[j]:
                unik[i], unik[j] = unik[j], unik[i]

    hasil = tuple(unik)

    print(hasil)

    lanjut = input("Apakah ingin lanjut (y/n): ")
    if lanjut == "n":
        break
    elif lanjut == "y":
        continue
    else:
        print("pilihan tidak valid!")
        continue
