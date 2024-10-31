inventory = {}

def TambahBarang() :
    kode = input('Masukkan kode barang: ')
    nama = input('Masukkan nama barang: ')
    jumlah = int(input('Masukkan jumlah barang: '))
    harga = float(input('Masukkan harga per unit barang: '))
    inventory[kode] = {'nama': nama, 'jumlah' : jumlah, 'harga' : harga}
    print(f'Barang berhasil ditambahkan.')

def HapusBarang() :
    kode = input('Masukkan kode barang yang akan dihapus: ')
    hapus = inventory.pop(kode)

    if hapus :    
        print('Barang berhasil dihapus.')
    else :
        print('Barang tidak ditemukan dalam inventory.')

def MenampilkanBarang() :
    if inventory :
        for kode, data in inventory.items():
            print(f'Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}')
    else:
        print('Inventory kosong.')

def CariBarang():
    cari = input('Cari berdasarkan (1) Kode atau (2) Nama: ')

    if cari == '1':
        CariKode = input('Masukkan kode barang: ')
        if CariKode in inventory:
            data = inventory[CariKode]
            print(f"Kode: {CariKode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
        else:
            print('Barang tidak ditemukan dalam inventory.')

    elif cari == '2':
        CariNama = input('Masukkan nama barang: ')
        for kode, data in inventory.items():
            if CariNama.lower() == data['nama'].lower():
                print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
                return 
        print('Barang tidak ditemukan dalam inventory.') 

    else:
        print('Pilihan tidak tersedia.')



def UpdateBarang() :
    kode = input('Masukkan kode barang yang ingin diupdate: ')
    if kode in inventory:
        JumlahBaru = int(input('Masukkan jumlah baru: '))
        inventory[kode]['jumlah'] = JumlahBaru

        HargaBaru = float(input('Masukkan harga per unit baru: '))
        inventory[kode]['harga'] = HargaBaru
        
        print('Data barang berhasil diperbarui')
    else :
        print('Barang tidak ditemukan.')

def menu() :
    while True :
        print('===Menu Inventori Barang===')
        print('1. Tambah Barang')
        print('2. Hapus Barang')
        print('3. Tampilkan Barang')
        print('4. Cari Barang')
        print('5. Update Barang')
        print('6. Keluar')

        pilihan = input('Pilih opsi (1-6): ')

        if pilihan == '1':
            TambahBarang()
        elif pilihan == '2':
            HapusBarang()
        elif pilihan == '3':
            MenampilkanBarang()
        elif pilihan == '4':
            CariBarang()
        elif pilihan == '5':
            UpdateBarang()
        elif pilihan == '6':
            print('Terima kasih telah menggunakan program inventori.')
            break
        else :
            print('Input tidak valid')

menu()