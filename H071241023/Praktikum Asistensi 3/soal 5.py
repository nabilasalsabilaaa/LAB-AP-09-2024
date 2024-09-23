serangga_A = float(input("Masukkan populasi awal Serangga A : "))
serangga_B = float(input("Masukkan populasi awal Serangga B : "))
hari = int(input("Masukkan jumlah hari : "))

for hari in range(1, hari + 1) :
    if hari % 2 == 1 :
        serangga_A = int(serangga_A * 1.3)
        serangga_B = int(serangga_B * 1.5)
    else: 
        serangga_A = int(serangga_A * 0.8)
        serangga_B = int(serangga_B * 0.6)

    if hari % 5 == 0:
        serangga_A = int(serangga_A * 0.9)
        serangga_B = int(serangga_B * 0.9)
        print(f'Hari {hari} : Predator memakan 10% populasi. ')
    print(f'Hari {hari} : Serangga A = {serangga_A}, Serangga B = {serangga_B}')

# pembulatan bermasalah

