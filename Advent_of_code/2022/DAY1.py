# This list represents the Calories of the food carried by five Elves:

# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
# The second Elf is carrying one food item with 4000 Calories.
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
# The fifth Elf is carrying one food item with 10000 Calories.

# In case the Elves get hungry and need extra snacks,
# they need to know which Elf to ask: they'd like to know how many Calories are being carried
# by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

from itertools import groupby


def split_at_zero(input_list):
    input_list_groups = groupby(input_list, lambda x: x == 0)
    output_list = [sum(group) for key, group in input_list_groups if not key]
    return output_list

def main():
  with open("./DAY1.txt", "r") as file:
    test = [int(line.strip()) if line.strip() != "" else 0 for line in file] 

  result = split_at_zero(test)
  result.sort()
  print(max(result))
  print(sum(result[-3:]))

main()
