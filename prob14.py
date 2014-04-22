#! /usr/local/bin/python3.4

max_length = 0
max_number = 0

def sequence_length(x):
  length = 0
  while x != 1:
    length += 1
    if x % 2 == 0:
      x = x / 2
    else:
      x = x * 3 + 1
  return length

for i in range(1, 1000000):
  length = sequence_length(i)
  if length > max_length:
    print('Found a new contender: %s with sequence length %s' % (max_number, max_length))
    max_length = length
    max_number = i

print('Number %s has sequence length %s' % (max_number, max_length))
