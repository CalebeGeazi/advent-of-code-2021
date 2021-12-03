with open("input.txt") as file:
    inputs = file.readlines()
    inputs = [line.strip() for line in inputs]

# keep track of count for only 0 since 1 will be the inverse
most_common_bits_counts_0 = [0] * len(inputs[0])
gamma = epsilon = ""

for binary in inputs:
    binary_parts = list(binary)
    for i, digit in enumerate(binary_parts, 0):
        # only increment for 0
        if digit == '0':
            most_common_bits_counts_0[i] += 1

for count in most_common_bits_counts_0:
    # if more than half the length of binaries then it's the majority
    if count > len(inputs) / 2:
        gamma += "0"
        epsilon += "1"
    # otherwise do the opposite
    else:
        gamma += "1"
        epsilon += "0"

# convert to base10 and multiply
print(int(gamma, 2) * int(epsilon, 2))