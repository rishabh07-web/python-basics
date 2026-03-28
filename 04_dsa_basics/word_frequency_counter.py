sentence = input("Enter sentence: ")

words = sentence.split()

freq = {}

for word in words:
    
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

for key in freq:
    print(key, "→", freq[key])