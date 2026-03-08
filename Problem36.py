#Project Euler Problem 36
#Name: Liam Gillispie
#Date: 3/8/2026
#Assignment: Lab 7 
#Purpose: Find the sum of all numbers, less than one million, which are palindomic in base 10 and base 2

import NumberTests

def binaryPalindromic(n):
  s=str(n)
  return s==s[::-1]
def baseTenPalindromic(n):
  b=bin(n)[2:]
  return b==b[::-1]
def main():
  total=0
  for n in range(1, 1000000):
    if baseTenPalindromic(n) and binaryPalindromic(n):
      total+=n
  print("This is the sum of all numbers less than 1,000,000 palindromic in base 10 and base 2:")
  print(total)

if __name__ == '__main__':
  main()
