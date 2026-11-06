'''Dhea Febrianti // 2602997 // 1A'''
mahasiswa = {
    'Andi' : {'Nama' : 'Andi Sawargi', 'Kelas' : 'XI RPL 1', 'Kesukaan' : ['Anggur', 'Jeruk', 'Buku']},
    'Budi' : {'Nama' : 'Budi Setiawan', 'Kelas' : 'XI RPL 2', 'Kesukaan' : ['Gaming', 'Musik', 'Film']},
    'Citra' : {'Nama' : 'Citra Lestari', 'Kelas' : 'XI RPL 1', 'Kesukaan' : ['Membaca', 'Kucing', 'Musik']}
}

namapanggilan = input('Masukkan nama panggilan : ')
nomorkesukaan = int(input('Masukkan nomor kesukaan : '))

print(f'Nama \t : { mahasiswa[namapanggilan]['Nama']} \nKelas \t : {mahasiswa[namapanggilan]['Kelas']} \nKesukaan : {mahasiswa[namapanggilan]['Kesukaan'][nomorkesukaan-1]}')