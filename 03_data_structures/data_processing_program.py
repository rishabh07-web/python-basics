# Marks Categorizer

marks = []
n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input("Enter mark: "))
    marks.append(m)

pass_count = 0
fail_count = 0
total_marks = 0

for m in marks:
    total_marks = total_marks + m
    
    if m >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

average_marks = total_marks / n

print("\n----- RESULT SUMMARY -----")
print("Total Students :", n)
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)
print("Total Marks    :", total_marks)
print("Average Marks  :", average_marks)
