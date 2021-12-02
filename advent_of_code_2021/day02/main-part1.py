with open('input.txt') as file:
    commands = file.readlines()
    commands = [line.rstrip() for line in commands]

horizontal = 0
depth = 0

for command in commands:
    if command.startswith('forward'):
        horizontal += int(command.split(' ')[1])
    if command.startswith('down'):
        depth += int(command.split(' ')[1])
    if command.startswith('up'):
        depth -= int(command.split(' ')[1])

print(horizontal * depth)