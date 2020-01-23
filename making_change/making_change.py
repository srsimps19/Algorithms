#!/usr/bin/python

import sys

def making_change(amount, denominations):
  results = 0
  if amount < 0:
    return 0
  if amount == 0 or 1:
    return 1
  if amount > 2:
    for i in denominations:
      results += amount - i
    return results

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")