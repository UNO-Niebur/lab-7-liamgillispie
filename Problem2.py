#Project Euler problem 2
#Name: Liam Gillispie
#Date: 3/7/2026
#Assignment: Lab 7
#Purpose:


def main():
  nums = fibonacciSequence(4000001)
  print (nums)
  total = 0
  for fib in nums:
    if isEven(fib):
      total = total + fib
  
  print(total) # final answer

if __name__ == '__main__':
  main()
