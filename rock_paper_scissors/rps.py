#!/usr/bin/python
# RPS(n): 3 ** n
# RPS(0): 0 possibilities
# RPS(1): 3 possibilities
# RPS(2): 9 possibilities
# RPS(3): 27 possibilities
# RPS(4): 81 possibilities
# RPS(5): 243 possibilities

import sys



def rock_paper_scissors(n):
  rps = [['rock'], ['paper'], ['scissors']]
  results = []
  if n <= 0:
    return [[]]
  if n == 1:
    return rps
  for i in rock_paper_scissors(n-1):
    for j in rps:
      results += [i+j]
  return results




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')