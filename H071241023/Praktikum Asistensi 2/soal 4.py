penggunaan_data = float(input("Masukkan penggunaan data (GB): "))
waktu_penggunaan = input("Masukkan waktu penggunaan (Peak/Off-peak): ")
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ")

if penggunaan_data < 10:
    if waktu_penggunaan == 'off-peak' and jenis_pengguna == 'personal':
        print('Paket yang sesuai : Paket A')
    else:
        print('Tidak ada paket yang cocok')
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == 'peak' and jenis_pengguna == 'personal':
        print('Paket yang sesuai : Paket B')
    else:
        print('Tidak ada paket yang cocok')
else:
    if waktu_penggunaan == 'peak' and (jenis_pengguna == 'personal' or jenis_pengguna == 'bisnis'):
        print('Paket yang sesuai : Paket C')
    elif waktu_penggunaan == 'off-peak' and jenis_pengguna == 'bisnis':
        print('Paket yang sesuai : Paket D')
    else:
        print('Tidak ada paket yang cocok')