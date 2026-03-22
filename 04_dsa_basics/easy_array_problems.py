# Check if list is sorted

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

sorted_flag = True

for i in range(n-1):
    if lst[i] > lst[i+1]:
        sorted_flag = False
        break

if sorted_flag:
    print("Sorted")
else:
    print("Not Sorted")


# Reverse list manually

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

start = 0
end = n - 1

while start < end:
    temp = lst[start]
    lst[start] = lst[end]
    lst[end] = temp
    
    start = start + 1
    end = end - 1

print("Reversed List:", lst)
