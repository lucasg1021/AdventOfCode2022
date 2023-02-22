
with open(r'day4_input.txt') as f:
    file = f.read()
    f.close()

file = file.split('\n')
file.pop()

pairs = 0
for pair in file:
    r = pair.split(',')

    r1 = [*range(int(r[0].split('-')[0]), int(r[0].split('-')[1]) + 1)]
    r2 = [*range(int(r[1].split('-')[0]), int(r[1].split('-')[1]) + 1)]

    if any(item in r1 for item in r2):
        pairs += 1
        continue

    elif any(item in r2 for item in r1):
        pairs += 1
        continue

print(f'Number of pairs: {pairs}')
