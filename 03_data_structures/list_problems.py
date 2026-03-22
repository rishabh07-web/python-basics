# Count even numbers

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

count = 0

for i in lst:
  if i%2 == 0:
    count += 1

print(f"Count = {count}")

# Find second largest number

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

largest = lst[0]

for i in lst:
  if i > largest:
    largest = i

second = None

for i in lst:
  if i != largest:
    if second is None or i > second:
      second = i

if second is None:
  print("Second largest does not exist")
else:
  print("Second largest=", second) 
      
      
    

