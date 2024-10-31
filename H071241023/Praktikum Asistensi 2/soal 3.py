nilai = int(input('Masukkan nilai akhir :'))
kehadiran = int(input('Masukkan persentase kehadiran :'))

# if 85 <= nilai <= 100 :
#     if kehadiran >= 75 :
#         print('Lulus dengan predikat A')
#     elif 70 <= nilai <= 84 :
#         if kehadiran >= 75 :
#             print('Lulus dengan predikat B') 
#     elif 60 <= nilai <= 69 :
#         if kehadiran >= 75 :
#             print('Lulus dengan predikat C')
#     elif nilai < 60 :
#         if kehadiran >= 75 :
#             print('Lulus dengan predikat C')

if kehadiran >= 75 :
    if nilai >= 85 : 
        predikat = 'Lulus dengan predikat A'
    elif nilai >= 75 :
        predikat = 'Lulus dengan predikat B'
    elif nilai >= 60 :
        predikat = 'Lulus dengan predikat C'
    else : 
        nilai = int(input('Masukkan nilai tugas tambahan :'))
        if nilai > 70 :
            predikat = "Lulus dengan predikat C"
        else :
            predikat = "tidak lulus"
else :
    predikat = 'Tidak lulus'
print(predikat)
