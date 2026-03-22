# Count vowels

str = input("Enter your string here: ")
count = 0

for ch in str:
  if ch in 'aeiouAEIOU':
    count += 1

print("Total vowels =", count)

# Reverse a string

str = input("Enter your string here: ")
rev = ''

for ch in str:
  rev = ch + rev

print(Reversed string: ", rev)
