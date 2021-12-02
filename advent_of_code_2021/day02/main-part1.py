horizontal = 0
depth = 0

with open('input.txt') as commands:
    for command in commands:
        command = command.strip()
        if command.startswith('forward'):
            horizontal += int(command.split(' ')[1])
        if command.startswith('down'):
            depth += int(command.split(' ')[1])
        if command.startswith('up'):
            depth -= int(command.split(' ')[1])

print(horizontal * depth)