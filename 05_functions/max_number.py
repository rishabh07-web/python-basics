def max_number(list):
    largest = list[0]

    for i in list:
        if i > largest:
            largest = i

    return largest

lst = []

n = int(input("Enter the size of list here: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

result = max_number(lst)
print(f"Maximum numer = {result}")    