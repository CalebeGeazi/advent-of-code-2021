with open('input.txt') as file:
    commands = file.readlines()
    commands = [line.rstrip() for line in commands]

horizontal = 0
depth = 0
aim = 0

for command in commands:
    if command.startswith('forward'):
        value = int(command.split(' ')[1])
        horizontal += value
        depth += aim * value
    if command.startswith('down'):
        aim += int(command.split(' ')[1])
    if command.startswith('up'):
        aim -= int(command.split(' ')[1])

print(horizontal * depth)