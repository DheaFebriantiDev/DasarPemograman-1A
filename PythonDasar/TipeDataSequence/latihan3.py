'''Dhea Febrianti // 2602997 // 1A'''

import math

x1 = int(input('Masukkan titik x1 : '))
y1 = int(input('Masukkan titik y1 : '))
x2 = int(input('Masukkan titik x2 : '))
y2 = int(input('Masukkan titik y2 : '))

titikA = (x1, y1)
titikB = (x2, y2)

d = int(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))

print (f'Titik A : {titikA} \n Titik B : {titikB} \n Jarak garis lurus kedua titik tersebut adalah {d}')