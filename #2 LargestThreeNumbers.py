a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = (input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Angka terbesar adalah:", largest)