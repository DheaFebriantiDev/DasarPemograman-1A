'''Dhea Febrianti // 2602997 // 1A'''

umur = int(input('Umur Anda : (Tahun)'))
jeniskelamin = input('Jenis Kelamin : (Pria/Wanita)')
TB = int(input('Tinggi Badan Anda: (CM)'))
IQ = int(input('IQ Anda : '))

if (umur >= 18 and umur <= 25 and IQ >= 130):
    if (jeniskelamin == 'Wanita' and TB >= 170):
        print('Selamat, Anda menjadi model wanita catwalk')
    elif (jeniskelamin == 'Pria' and TB >= 175):
        print('Selamat, Anda menjadi model pria catwalk')
    else:
        print('Tinggi anda kurang')
else :
    print('Anda tidak cocok menjadi model catwalk')