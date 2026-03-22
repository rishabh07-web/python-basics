# Count words in a sentence

snt = input("Enter your sentence here: ")
count = 1

for ch in snt:
  if ch == ' ':
    count += 1

print(f"Number of words = {count}")


# Find longest word

snt = input("Enter a sentence: ")
words = snt.split()
max_word = words[0]

for w in words:
  if len(w) > len(max_word):
    max_word = w

print("Word with maximum length =", max_word)

