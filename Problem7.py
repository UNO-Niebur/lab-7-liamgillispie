#Project Euler Problem 7
#Name: Liam Gillispie
#Date: 3/8/2026
#Assignment: Lab 7 
#Purpose: Find the 10001st prime number

import NumberTests

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p <=1:
    return False
  if p==2:
    return True
  if p%2==0:
    return False
  for i in range(3, int(p**0.5)+1,2):
    if i%2==0:
      continue
    if p%i==0:
      return False
  return True

def isEven(n):
  """Returns boolean about given value being even."""
  if n % 2 == 0:
    return True
  else:
    return False

def main():

if __name__ == '__main__':
  main()
