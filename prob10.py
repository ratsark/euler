#! /usr/bin/python
import math

def isPrime(i):
  j = 3
  while j <= math.sqrt(i):
    if i % j == 0:
      return False
    j += 2
  return True

i = 3
sum = 2
while i < 2000000:
  if isPrime(i):
    sum += i
  i += 2
  if i % 10000 == 1:
    print i, " : ", sum
print sum
