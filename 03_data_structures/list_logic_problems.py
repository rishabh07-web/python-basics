# Find second smallest number

l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    ele = int(input("Enter element: "))
    l.append(ele)

smallest = l[0]

for i in l:
    if i < smallest:
        smallest = i

second = None

for i in l:
    if i != smallest:
        if second == None or i < second:
            second = i

print("Smallest =", smallest)
print("Second smallest =", second)       


# Sum of only positive numbers

l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    ele = int(input("Enter element: "))
    l.append(ele)

sum = 0

for i in l:
    if i > 0 :
        sum += i

print(f"Sum of positive numbers = {sum}") 
  
  


