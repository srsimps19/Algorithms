#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# C(3): 4 results
# C(2): 2 results
# C(1): 1 result
# C(0): 1 result
# 4 = 2 + 1 + 1

def eating_cookies(n, cache={0: 0, 1: 1, 2: 2}):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif n in cache:
    return cache[n]
  else:
    cookies = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    cache[n] = cookies
    return cookies
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')