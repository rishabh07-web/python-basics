# Rotate list by one position

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

last = lst[n-1]

for i in range(n-1, 0, -1):
    lst[i] = lst[i-1]

lst[0] = last
print("Rotated list:", lst)


# Frequency Count

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

visited = []

for i in range(n):    
    if lst[i] in visited:
        continue
    count = 0
    
    for j in range(n):
        if lst[i] == lst[j]:
            count = count + 1
    
    print(lst[i], "→", count, "times")
    
    visited.append(lst[i])
