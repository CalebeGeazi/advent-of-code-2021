horizontal = depth = aim = 0

with open('input.txt') as commands:
    for command in commands:
        command = command.strip()
        if command.startswith('forward'):
            value = int(command.split()[1])
            horizontal += value
            depth += aim * value
        if command.startswith('down'):
            aim += int(command.split()[1])
        if command.startswith('up'):
            aim -= int(command.split()[1])

print(horizontal * depth)