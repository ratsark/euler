#! /usr/local/bin/python3.4

num_txt = open('prob13.nums')
num_list = []
for line in num_txt.readlines():
  num_list.append(int(line))

total = 0
for number in num_list:
  total += number

print('Sum: %s' % total)
