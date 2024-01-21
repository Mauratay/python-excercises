"""
I have a range of # numbers
I divide the last number  between one before
if % == 0
is not a prime
if % != 0
I divide the last between 2 before
if % == 0
is not a prime,, so on
"""

def is_prime(num):
    dividers = [i for i in reversed(range(1,num)) if num % i == 0]
    if len(dividers) > 1: return False
    else: return True

for i in range(1, 20):
	if is_prime(i + 1):
          print(i + 1, end=" ")
