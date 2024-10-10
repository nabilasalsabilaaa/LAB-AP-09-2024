def acronym () :
    kalimat = input('Masukkan kalimat: ')
    acronym = ''
    for karakter in kalimat.split(): 
        acronym = acronym + karakter[0]
    print(acronym.upper(), end='')
acronym()