marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input("Enter mark: "))
    marks.append(m)

freq = {}

for m in marks:
    if m in freq:
        freq[m] = freq[m] + 1
    else:
        freq[m] = 1

print("\nFrequency of each mark:")
for key in freq:
    print(key, "→", freq[key], "times")


max_freq = 0

for key in freq:
    if freq[key] > max_freq:
        max_freq = freq[key]

print("Highest Mark Frequency =", max_freq)


total = 0

for m in marks:
    total = total + m

avg = total / n


above_avg = 0

for m in marks:
    if m > avg:
        above_avg = above_avg + 1

print("Average Marks =", avg)
print("Students Above Average =", above_avg)