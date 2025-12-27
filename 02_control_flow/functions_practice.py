def sum(x,y):
  return x+y

def checkEvenOdd(x):
  if(x%2 == 0):
    print(f"{x} is an Even number.")
  else:
    print(f"{x} is an Odd number.")

print(sum(5,4))
checkEvenOdd(5)
checkEvenOdd(4)

def findEven(n):
  for i in range(n+1):
    if(i%2 == 0):
      print(i, end = " ")

findEven(10)

def sum_series(n):
  ans = 0
  for i in range(1,n+1):
    ans += i
  return ans

print(sum_series(10))

  

  
    
