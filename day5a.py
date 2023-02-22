with open(r'day5_input.txt') as f:
    file = f.read()
    f.close()

crates = file.split('\n\n')[0].split('\n')
crates.pop()
moves = file.split('\n\n')[1].split('\n')
moves.pop()

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []

l = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

for row in crates:
    items = [row[j:j+4] for j in range(0, len(row), 4)]

    for i, item in enumerate(items):
        if item != '    ':
            l[i].append(item)

for i in range(len(l)):
    l[i].reverse()

for move in moves:
    moveNums = [int(s) for s in move.split() if s.isdigit()]

    amt = moveNums[0]
    src = moveNums[1] - 1
    dst = moveNums[2] - 1

    for i in range(amt):
        item = l[src].pop()
        l[dst].append(item)

for i in range(len(l)):
    print(f'{l[i][-1][1]}', sep='', end='')