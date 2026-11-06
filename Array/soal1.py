'''Dhea F // 2602997 // Soal 1 Numpy'''

import numpy as np

SuhuCelcius = np.array([22.5, 21.8, 20.5, 20.8, 23.5, 20.7, 19.5, 18.9, 19.2, 18.2])

SuhuFarenheit = (SuhuCelcius * 9/5)+32
print(f'Suhu Singapura (Celcius) adalah { SuhuCelcius }')
print(f'Suhu SIngapura (Farenheit) adalah { SuhuFarenheit }')