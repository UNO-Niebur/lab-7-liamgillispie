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
    if p%i==0:
      return False
  return True


def main():
  count=0
  n=1
  while count < 10001:
    n+=1
    if isPrime(n):
      count+=1
  print(f"The 10,001st prime number is {n}!")

if __name__ == '__main__':
  main()
