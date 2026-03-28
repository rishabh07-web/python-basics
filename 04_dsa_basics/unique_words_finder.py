sentence = input("Enter sentence here: ")

words = sentence.split()

unique = set(words)

for i in unique:
    print(i)
