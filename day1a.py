
with open('day1_input.txt') as f:
    file = f.read()
    f.close()

a = file.split('\n\n')

max = 0
number = -1
for elfNum, elf in enumerate(a):
    cals = elf.split('\n')

    if cals[-1] == '':
        cals.pop()
    cals = [int(num) for num in cals]

    if sum(cals) > max:
        max = sum(cals)
        number = elfNum

print(f'Elf {number} had {max} calories!')
pass