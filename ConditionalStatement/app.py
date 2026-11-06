x = 100
y = 85

if ( x < 0 or y < 0):
    print("Error")
elif ( x <= 75 or y <= 80):
    print("Met remed")
elif (x <= 100 and y<=100): 
    print("Met lulus")
else :
    print("Error")

if (x < 0 or y < 0):
    print('Error')
elif (x <= 75):
    print('Remedial')
    if (y>=80):
        print('Kurang kehadiran')
else :
    print('Males ngetik kode')

a = 1
b = 4

if a>b:print('Nilai a lebih besar daripada b')

print('Nilai a lebih besar daripada b') if a > b else print('Nilai b lebih besar')