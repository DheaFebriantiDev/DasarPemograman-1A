'''Dhea F // 2602997 // Soal 2 Numpy'''

import numpy as np

NilaiSiswa = np.random.randint(50, 101, size=30)

SortNilai = np.sort(NilaiSiswa)[::-1]
Nilai5Besar = SortNilai[:5]

print(f'Data nilai acak \t: \t{NilaiSiswa}')
print(f'Data nilai terurut \t: \t{SortNilai}')
print(f'5 Nilai terbesar \t: \t{Nilai5Besar}')