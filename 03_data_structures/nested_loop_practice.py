# Simple star pattern

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print() 


# Multiplication table list

l = [2,4,5]

for i in l:
    print(f"Table of {i}")
    for j in range(1,6):
        print( i, "x", j, "=", i*j)
    print()
