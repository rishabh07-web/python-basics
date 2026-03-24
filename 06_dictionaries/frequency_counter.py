lst = []
n = int(input("Enter the size of list: "))

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1   

print("\nFrequency Count:")

for key in freq:
    print(key , "->", freq[key], "times")