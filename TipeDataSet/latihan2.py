'''Nama : Dhea Febrianti
NIM : 2602997'''

kelas = {'andi', 'budi', 'citra', 'gita', 'doni', 'eka'}
sirkel = {'citra', 'doni', 'eka'}

kel1 = kelas.intersection(sirkel)
print (f'Kelompok 1 : {kel1}')

kelas.add('hani')
kel2 = sirkel.symmetric_difference(kelas)

print(f'Kelompok 2 : {kel2}')