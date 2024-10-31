usia = int(input('Masukkan usia :'))
keanggotaan = input('Apakah anda anggota (ya/tidak) : ').lower()

if usia < 5 :
    harga_tiket = 0
elif 5 <= usia <= 12 :
    harga_tiket = 50000
elif 13 <= usia <= 59 :
    harga_tiket = 100000
elif usia >= 60 : 
    harga_tiket = 70000

if keanggotaan == 'ya':
    diskon = harga_tiket * (20/100)
    harga_tiket = harga_tiket - diskon

print(f"Harga tiket yang harus dibayar: Rp.{harga_tiket:.00f}")
