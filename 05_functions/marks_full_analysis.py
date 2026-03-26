# Function to take marks input
def take_input():
    marks = []
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        m = int(input("Enter mark: "))
        marks.append(m)
        
    return marks


# Function to calculate average (without using in-built sum function)
def calculate_average(marks):
    total = 0
    
    for m in marks:
        total = total + m
        
    avg = total / len(marks)
    return avg


# Function to count students above average
def count_above_average(marks, avg):
    count = 0
    
    for m in marks:
        if m > avg:
            count = count + 1
            
    return count


# Function to find highest & lowest
def find_high_low(marks):
    highest = marks[0]
    lowest = marks[0]
    
    for m in marks:
        if m > highest:
            highest = m
            
        if m < lowest:
            lowest = m
            
    return highest, lowest


# Function to print final report
def print_report(avg, above_avg, highest, lowest):
    print("\n----- FINAL REPORT -----")
    print("Average Marks →", avg)
    print("Students Above Average →", above_avg)
    print("Highest Marks →", highest)
    print("Lowest Marks →", lowest)


# MAIN PROGRAM FLOW
marks = take_input()

avg = calculate_average(marks)

above_avg = count_above_average(marks, avg)

highest, lowest = find_high_low(marks)

print_report(avg, above_avg, highest, lowest)