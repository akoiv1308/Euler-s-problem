'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Alex and Mohammad - Period 6
'''

start = int(input("start: "))
initial = start
if start < 2:
  initial = 2
amount = 105000
primeCount = 0
for i in range(initial, amount+1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    primeCount += 1
    if primeCount == 10001:
      print(i)
print(primeCount)


