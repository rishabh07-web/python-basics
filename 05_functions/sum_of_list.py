def sum_of_list(list):
    total = 0 
    for i in list:
        total += i
    return total

lst = []

n = int(input("Enter the size of list here: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

result = sum_of_list(lst)
print(f"Total sum = {result}")    