# Remove duplicates

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("Unique list =", unique)


# Linear search

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

key = int(input("Enter number to search: "))
found = False

for i in range(len(lst)):
    if lst[i] == key:
        print("Number found at position", i)
        found = True
        break

if found == False:
    print("Not Found")

