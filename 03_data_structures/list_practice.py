# Marks Analyzer

marks = []

# Taking input
for i in range(5):
    x = int(input("Enter mark: "))
    marks.append(x)

# Total
total = 0
for m in marks:
    total = total + m

# Average
avg = total / 5

# Highest and Lowest
highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

# Printing Results
print("Total Marks =", total)
print("Average =", avg)
print("Highest Mark =", highest)
print("Lowest Mark =", lowest)
