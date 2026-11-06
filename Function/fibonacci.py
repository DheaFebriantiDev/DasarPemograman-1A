'''Dhea Febrianti // 2602997 // 1A'''

def fibonacci(n):
    deret = [0, 1]

    if (n <= 1):
        return [0]
    else :
        for i in range(2, n):
            angka = deret[-1] + deret[-2]

            deret.append(angka)

        return deret

print(fibonacci(5))