a = float(input('Masukkan harga saham kemarin: '))
b = 105.0

# Perubahan persentase (x)
x = (b - a) / a * 100

# Kondisi
Beli = x > 5
Tahan = -3 <= x <= 5
Jual = x < -3

rekomendasi = Beli * 'Beli' + Tahan * 'Tahan' + Jual * 'Jual'

print(f'Perubahan persentase harga saham: {x:.02f}%')
print(f'Rekomendasi investasi: {rekomendasi}')
