def count_even(list):
    count = 0

    for i in list:
        if i % 2 == 0:
            count += 1

    return count

lst = []

n = int(input("Enter size of the list here: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

result = count_even(lst)
print(f"Number of even numbers = {result}")    
