'''
Nama : Dhea Febrianti 
NIM : 2602997
'''

TagihanListrik = {
    'AC' : [1, 900, 8],
    'Kulkas' : [1, 100, 24],
    'TV' : [1, 50, 5],
    'Lampu' : [6, 15, 15]
}

TotalAC = TagihanListrik['AC'][0]*TagihanListrik['AC'][1]*TagihanListrik['AC'][2]
TotalKulkas = TagihanListrik['Kulkas'][0]*TagihanListrik['Kulkas'][1]*TagihanListrik['Kulkas'][2]
TotalTV = TagihanListrik['TV'][0]*TagihanListrik['TV'][1]*TagihanListrik['TV'][2]
TotalLampu = TagihanListrik['Lampu'][0]*TagihanListrik['Lampu'][1]*TagihanListrik['Lampu'][2]

TotalListrikdalamKwH = (TotalAC+TotalKulkas+TotalLampu+TotalTV)/1000
TotalTagihan = TotalListrikdalamKwH*1444

print (f'Estimasi total tagihan listrik Ibu Diana adalah Rp. {TotalTagihan}')