jumlah_perulangan = 3

for index in range(jumlah_perulangan):
    print(f"Print ke-{index}")

for i in "Python":
    print(f"Huruf: {i}")

# Rentang dengan batas awal dan akhir
for i in range(1, 6):
    print(i)

# Rentang standar (dimulai dari 0 hingga n-1)
for i in range(6):
    print(i)

# Rentang dengan kenaikan/step tertentu (misal step 2)
for i in range(0, 10, 2):
    print(i)

# Rentang menurun (decremental)
for i in range(10, 0, -1):
    print(i)

angka = 0
while(angka < 8):
    print(f"Angka sekarang: {angka}")
    angka += 1

# Contoh 1: break diletakkan sebelum print
angka = [1-3, 16, 17]
for i in angka:
    if i == 3:
        break
    print(i)

# Contoh 2: break diletakkan setelah print
angka = [1-3, 16, 17]
for i in angka:
    print(i)
    if i == 3:
        break

# Continue pada List
angka = [1-3, 16, 17]
for i in angka:
    if i == 3:
        continue
    print(i)

# Continue pada String
string = "Python"
for karakter in string:
    if karakter == "y":
        continue
    print(f"Huruf: {karakter}")

buah = ["apel", "belimbing", "ceri"]
angka = [1, 16]

for i in buah:
    for j in angka:
        print(i)
        print(j)

baris = 0
bintang = 0

while baris < 10:
    if (bintang >= baris + 1):
        print()
        baris += 1
        bintang = 0
        continue
    print("*", end="")
    bintang += 1

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print(f"Nilai i sudah tidak memenuhi kondisi karena i = {i}")

list = ["apel", "anggur", "mangga", "jeruk", "melon"]

# Tanpa range
for item in list:
    print(item)

# Dengan range() dan len()
for item in range(len(list)):
    print(list[item])

# Mengubah karakter elemen menjadi kapital
listBaru = []
for i in list:
    listBaru.append(i.upper())
print(listBaru)

tuple = ("apel", "anggur", "mangga", "jeruk", "melon")

# Menggunakan range()
for item in range(len(tuple)):
    print(tuple[item])

# Mengakses langsung
for item in tuple:
    print(item)

set = {"apel", "anggur", "mangga", "jeruk", "melon"}

for item in set:
    print(item)

kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
}

# Mengakses nilai (value) berdasarkan kunci
for i in kucing:
    print(kucing[i])

# Mengakses kunci (key) langsung
for kunci in kucing:
    print(kunci)

# Mengakses nilai (value) dengan .values()
for x in kucing.values():
    print(x)

# Mengakses kunci (key) dengan .keys()
for x in kucing.keys():
    print(x)

# Mengakses pasangan key dan value dengan .items()
for x, y in kucing.items():
    print(x, y)