#! /usr/local/bin/python3.4

grid_txt = open('prob11.grid')
grid = []
for line in grid_txt.readlines():
  this_line = []
  for number in line.split(' '):
    this_line.append(int(number))
  grid.append(this_line)

max_value = 0
max_x = len(grid)
max_y = len(grid[0])
line_length = 4

def compute(values):
  global max_value
  product = 1
  for value in values:
    product *= value
  if product > max_value:
    max_value = product

for x in range(0, max_x):
  for y in range(0, max_y):
    if x + line_length <= max_x:
      # Search horizontally
      compute([grid[x + j][y] for j in range(0, line_length)])
      # Search down and right
      if y + line_length <= max_y:
        compute([grid[x + j][y + j] for j in range(0, line_length)])
      # Search up and right
      if y + 1 >= line_length:
        compute([grid[x + j][y - j] for j in range(0, line_length)])
    # Search vertically
    if y + line_length <= max_y:
      compute([grid[x][y + j] for j in range(0, line_length)])
       

print('Highest product: %s' % max_value)
