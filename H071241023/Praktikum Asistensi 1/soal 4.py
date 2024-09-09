celcius = float(input('Masukkan suhu dalam celcius: '))

kelvin = celcius + 273.15
reamur = celcius * 4/5
fahrenheit = (celcius * 9/5) + 32

print(f'Hasil konversi suhu dari {celcius} derajat Celcius ke Kelvin adalah: {kelvin:.02f}K')
print(f'Hasil konversi suhu dari {celcius} derajat Celcius ke Reamur adalah: {reamur:.02f}R')
print(f'Hasil konversi suhu dari {celcius} derajat Celcius ke Fahrenheit adalah: {fahrenheit:.02f}F')