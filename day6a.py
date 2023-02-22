with open(r'day6_input.txt') as f:
    file = f.read()
    f.close()

buffer = []

for ind, char in enumerate(file):
    if len(buffer) < 4:
        buffer.append(char)

    else:
        buffer.pop(0)
        buffer.append(char)

        for i, item in enumerate(buffer):
            if any([item == val for j, val in enumerate(buffer) if j != i]):
                break
        else:
            break


print(f'Index: {ind+1}')
