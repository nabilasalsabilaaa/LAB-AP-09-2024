import os
import time

# Folder utama 
folder_utama = 'Praktikum Asistensi 7'

# Menyimpan data film dan tiket dalam sub-folder
DIRECTORY = os.path.join(folder_utama, 'DataBioskop')
FILM_FILE = os.path.join(DIRECTORY, 'DaftarFilm.txt')
TIKET_FOLDER = os.path.join(DIRECTORY, 'tiket')
# Buat Sub Folder
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
if not os.path.exists(TIKET_FOLDER):
    os.makedirs(TIKET_FOLDER)

# Menu Utama
def menu_utama():
    while True:
        print('--- Sistem Pemesanan Tiket Bioskop ---')
        print('1. Admin')
        print('2. Pengunjung')
        print('3. Keluar')
        
        pilihan = input('Pilih peran (1/2/3): ')
        
        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        elif pilihan == '3':
            print('Terima kasih telah menggunakan sistem ini.')
            break
        else:
            print('Pilihan tidak valid.\n')

# Menu Admin
def menu_admin():
    while True:
        print('\n--- Menu Admin ---')
        print('1. Tambah Film')
        print('2. Hapus Film')
        print('3. Daftar Tiket')
        print('4. Kembali')
        
        pilihan = input('Pilih opsi (1/2/3/4): ')
        
        if pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            hapus_film()
        elif pilihan == '3':
            tampilkan_film()
            print('\n--- Daftar Tiket ---')
            print('1. Lihat Daftar Tiket')
            print('2. Lihat Detail Tiket')
            print('3. Hapus Tiket')
            print('4. Kembali')
            opsi = input('Pilih opsi (1/2/3/4): ')
            if opsi == '1':
                tampilkan_daftar_tiket()
            elif opsi == '2':
                tampilkan_detail_tiket()
            elif opsi == '3':
                hapus_tiket()
            elif opsi == '4':
                print('Kembali ke Menu Admin\n')
                break
            else:
                print('Pilihan tidak tersedia\n')
        elif pilihan == '4':
            print('Kembali ke Menu Utama\n')
            break
        else:
            print('Pilihan tidak tersedia\n')

# Fungsi menu Pengunjung
def menu_pengunjung():
    while True:
        print('\n--- Menu Pengunjung ---')
        print('1. Tampilkan Daftar Film')
        print('2. Beli Tiket')
        print('3. Keluar')
        
        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':
            tampilkan_film()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            print('Kembali ke Menu Utama\n')
            break
        else:
            print('Pilihan tidak valid!\n')

# Admin - Tambah Film
def tambah_film():
    print('\n--- Tambah Film ---')
    judul_film = input('Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ')
    if judul_film:
        with open(FILM_FILE, 'a') as file:
            file.write(judul_film + '\n')
        print(f"Film '{judul_film}' berhasil ditambahkan!\n")
    input()
    print('Kembali ke Menu Admin.\n')

# Admin - Hapus Film
def hapus_film():
    print('\n--- Hapus Film ---')
    daftar_film = baca_film_dari_file()
    tampilkan_film()
    pilihan = int(input('Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ')) - 1
    if 0 <= pilihan < len(daftar_film):
        film_dihapus = daftar_film.pop(pilihan)
        simpan_film_ke_file(daftar_film)
        print(f"Film '{film_dihapus}' berhasil dihapus.\n")
    elif pilihan == -1:
        print('Kembali ke Menu Admin.\n')
    else:
        print('Pilihan tidak valid!\n')

# Daftar film
def tampilkan_film():
    daftar_film = baca_film_dari_file()
    if daftar_film:
        print('\nDaftar Film:')
        for i, film in enumerate(daftar_film):
            print(f"{i+1}. {film}")
    else:
        print('Tidak ada film yang tersedia.\n')

# Baca film dari file
def baca_film_dari_file():
    if os.path.exists(FILM_FILE):
        with open(FILM_FILE, 'r') as file:
            daftar_film = [line.strip() for line in file.readlines()]
        return daftar_film
    else:
        return []

# Simpan daftar film ke file
def simpan_film_ke_file(daftar_film):
    with open(FILM_FILE, 'w') as file:
        for film in daftar_film:
            file.write(f'{film}\n')

# Admin - Daftar tiket
def tampilkan_daftar_tiket():
    daftar_tiket = os.listdir(TIKET_FOLDER)
    if daftar_tiket:
        print('\nDaftar Tiket:')
        for i, tiket in enumerate(daftar_tiket):
            print(f"{i+1}. {tiket}")
    else:
        print('Tidak ada tiket yang telah dibeli.\n')

# Admin - Detail Tiket
def tampilkan_detail_tiket():
    print('\n--- Detail Tiket ---')
    tampilkan_daftar_tiket()

    pilihan = int(input('Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ')) - 1
    daftar_tiket = os.listdir(TIKET_FOLDER)
    if 0 <= pilihan < len(daftar_tiket):
        tiket = daftar_tiket[pilihan]
        with open(os.path.join(TIKET_FOLDER, tiket), 'r') as file:
            print(file.read())
    elif pilihan == 0:
        print('Kembali ke Menu Admin.\n')
    else:
        print("Pilihan tidak valid!\n")

# Admin - Hapus Tiket
def hapus_tiket():
    print('\n--- Hapus Tiket ---')
    tampilkan_daftar_tiket()
    pilihan = int(input('Pilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): ')) - 1
    daftar_tiket = os.listdir(TIKET_FOLDER)
    if 0 <= pilihan < len(daftar_tiket):
        tiket_dihapus = daftar_tiket[pilihan]
        os.remove(os.path.join(TIKET_FOLDER, tiket_dihapus))
        print(f"Tiket '{tiket_dihapus}' berhasil dihapus.\n")
    else:
        print("Pilihan tidak valid!\n")

# Pengunjung - Beli Tiket
def beli_tiket():
    daftar_film = baca_film_dari_file()
    tampilkan_film()
    pilihan = int(input('Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ')) - 1
    if 0 <= pilihan < len(daftar_film):
        judul_film = daftar_film[pilihan]
        id_tiket = hasilkan_id_tiket()
        simpan_bentuk_tiket_ke_file(id_tiket, judul_film)
        print(f"Tiket berhasil dibeli. ID tiket Anda: {id_tiket}\n")
        tampilkan_daftar_tiket()
        print(f"File tiket telah dibuat: {TIKET_FOLDER}/{id_tiket}.txt")
    elif pilihan == -1:
        print('Kembali ke Menu Pengunjung.\n')
    else:
        print('Pilihan tidak valid!\n')

# Tiket dalam bentuk file
def simpan_bentuk_tiket_ke_file(id_tiket, judul_film):
    tiket_file = os.path.join(TIKET_FOLDER, f"{id_tiket}.txt")
    with open(tiket_file, "w") as file:
        file.write("+--------------------------------+\n")
        file.write("|          TIKET BIOSKOP         |\n")
        file.write("+--------------------------------+\n")
        file.write(f"|ID Tiket   : {id_tiket}        |\n")      
        file.write(f"|Film       : {judul_film}      |\n")
        file.write(f"|Tanggal    : {time.strftime('%d-%m-%Y')}, {time.strftime('%H:%M:%S')}|\n")
        file.write("+--------------------------------+\n")
        file.write("|   Terima kasih telah membeli   |\n")
        file.write("|           tiket Anda!          |\n")
        file.write("+--------------------------------+\n")

# ID tiket berdasarkan waktu
def hasilkan_id_tiket():
    waktu_sekarang = time.strftime("%d%m%Y%H%M%S")
    return f"TICK{waktu_sekarang}"

# Menjalankan menu utama
menu_utama()