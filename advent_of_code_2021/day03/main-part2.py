with open("input.txt") as file:
    inputs = file.readlines()
    inputs = [line.strip() for line in inputs]

def process_binaries(binaries, check_oxy=True):
    for i in range(0, len(binaries[0])):
        sub_0 = []
        sub_1 = []
        for binary in binaries:
            if binary[i] == '0':
                sub_0.append(binary)
            elif binary[i] == '1':
                sub_1.append(binary)
        
        if check_oxy:
            binaries = sub_1 if len(sub_1) >= len(sub_0) else sub_0
        else:
            binaries = sub_0 if len(sub_0) <= len(sub_1) else sub_1

        if len(binaries) == 1:
            break
    
    return binaries[0]

oxy_binary = process_binaries(inputs)
co2_binary = process_binaries(inputs, check_oxy=False)

print(int(oxy_binary, 2) * int(co2_binary, 2))