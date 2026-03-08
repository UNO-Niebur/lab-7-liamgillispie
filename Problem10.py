#Project Euler problem 10
#Name: Liam Gillispie
#Date: 3/7/2026
#Assignment: Lab 7
#Purpose: Find the sum of all primes below two million.

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

def main():
  limit=2000000
  total=0
  for n in range(2, limit):
    if isPrime(n):
      total+=n
  print(f"The sum of all prime numbers below two million is {total}!")

if __name__ == '__main__':
  main()
