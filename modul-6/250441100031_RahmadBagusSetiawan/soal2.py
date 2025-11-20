def gabung_tuple(t1, t2):
    gabung = t1 + t2
    tanpa_duplikat = []

    for x in gabung:
        if x not in tanpa_duplikat:
            tanpa_duplikat.append(x)


    for i in range(len(tanpa_duplikat)):
        for j in range(i + 1, len(tanpa_duplikat)):
            if tanpa_duplikat[i] < tanpa_duplikat[j]:
                temp = tanpa_duplikat[i]
                tanpa_duplikat[i] = tanpa_duplikat[j]
                tanpa_duplikat[j] = temp

    return tuple(tanpa_duplikat)

def input_tuple():
    data = []
    n = int(input("Masukkan jumlah angka: "))
    for i in range(n):
        angka = int(input(f"Angka ke-{i+1}: "))
        data.append(angka)
    return tuple(data)

def main():
    print("=== Program Tuple ===")
    print("Input tuple pertama:")
    t1 = input_tuple()
    print("Input tuple kedua:")
    t2 = input_tuple()

    hasil = gabung_tuple(t1, t2)
    print("Hasil akhir:", hasil)

main()