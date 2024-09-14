a = int(input('Masukkan panjang sisi pertama :'))
b = int(input('Masukkan panjang sisi kedua :'))
c = int(input('Masukkan panjang sisi ketiga :'))

if a == 0 or b == 0 or c == 0 or a + b <= c or a + c <= b or b + c <= a :
    print('Tidak dapat membentuk segitiga valid')
elif a == b == c :
    print('Segitiga sama sisi')
elif a == b or b == c or a == c :
    print('Segitiga sama kaki')
elif a != b != c :
    print('Segitiga sembarang')
