a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a > b and a > c: ##and dua kondisi harus terpenuhi
    largest = a
    print("Angka terbesar adalah:", largest)
elif b > a and b > c:
    largest = b
    print("Angka terbesar adalah:", largest)
elif c > a and c > b:
    largest = c
    print("Angka terbesar adalah:", largest)

else:
    print("Tidak Ada Mas")