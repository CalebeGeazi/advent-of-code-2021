with open("input.txt") as file:
    inputs = file.readlines()
    inputs = [int(line.rstrip()) for line in inputs]

count = 0
prev_sum = None

for i, input in enumerate(inputs, 0):
    if len(inputs) - 2 >= i + 1:
        group = inputs[slice(i, i + 3)]
        group_sum = sum(group)
        if not prev_sum:
            prev_sum = group_sum
            continue

        if prev_sum < group_sum:
            count = count + 1
        prev_sum = group_sum

print(count)