import re

MAXIMUM = {'red': 12, 'green': 13, 'blue': 14}

with open('Day2/Day2.txt') as input_file:
        data = input_file.read()
        data = data.split("\n")

total = 0

for line in data:
    line = re.split(';|:', line)
    line_list = []

    for i, part in enumerate(line):
        if i == 0:
            part = part.split()
            line_list.append(int(part[1]))
        else:
            cubes_dict = {}
            part = part.strip().split(',')
            for cubes in part:
                cubes = cubes.split()
                cubes_dict[cubes[1]] = int(cubes[0])
            line_list.append(cubes_dict)

    max_reached = False

    for game in line_list[1:]:
        for color, amount in game.items():
            if amount > MAXIMUM[color]:
                max_reached = True
                break

    if not max_reached:
        total += line_list[0]

print(f"Total: {total}")
