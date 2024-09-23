total_harga = int(input('Masukkan total harga: '))
uang_diberikan = int(input('Masukkan uang yang diberikan: '))
kembalian = uang_diberikan - total_harga

lembar_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

if kembalian > 0 :
    for i in lembar_uang:
        lembar = kembalian // i
        if lembar > 0:
            print(f'{lembar} Rp.{i:,}')
        kembalian = kembalian % i
else :
    print('Uang anda tidak cukup')