def calculate_total(list):
    total = 0 
    for i in list:
        total += i
    return total

def calculate_average(list):
    if not list:
        return 0.0
    return calculate_total(list)/len(list)

def count_pass(list):
    count = 0
    for i in list:
        if i >= 33:
            count += 1
    return count

def count_fail(list):
    count = 0
    for i in list:
        if i < 33:
            count += 1
    return count

def main():
    marks = []

    print("Enter marks( -1 to stop): ")
    while True:
        try:
            value = int(input("Enter marks: "))
            if value == -1:
                break
        
            if value < 0:
                print("Please enter non-negative mark or -1 to stop.")
                continue

            marks.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    total = calculate_total(marks)
    average = calculate_average(marks)
    pass_count = count_pass(marks)
    fail_count = count_fail(marks)

    print("\n--- Results ---")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Pass Students: {pass_count}")
    print(f"Fail Students: {fail_count}")       

main()    