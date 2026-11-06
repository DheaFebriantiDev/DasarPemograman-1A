'''Dhea Febrianti // 2602997 // 1A'''

nilai = int(input('Masukkan nilai user : '))

if (nilai > 100 or nilai < 0):
    print('Error')
elif (nilai > 90):
    print('Nilai A')
elif (nilai > 85):
    print('Nilai B+')
elif (nilai > 80):
    print('Nilai B')
elif (nilai > 70):
    print('Nilai C')
elif (nilai > 60):
    print('Nilai D')
else :
    print('Nilai E')