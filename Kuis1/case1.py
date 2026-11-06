'''
Nama : Dhea Febrianti 
NIM : 2602997
'''

menu = {
    'Nasi Uduk' : 14000,
    'Teh Lemon' : 9000,
    'Susu Coklat' : 12000,
    'Risol' : 6000
}

print (menu.items(),f'\n')

HargaPesananNasiUduk = menu['Nasi Uduk']*2
HargaPesananTehLemon = menu['Teh Lemon']*1
HargaPesananSusuCoklat = menu['Susu Coklat']*1
HargaPesananRisol = menu['Risol']*3
TotalPesanan = HargaPesananNasiUduk+HargaPesananRisol+HargaPesananSusuCoklat+HargaPesananTehLemon

print (f'Total Biaya yang harus dibayar Fajar : Rp. {TotalPesanan}')