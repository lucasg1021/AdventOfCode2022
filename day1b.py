
with open('day1_input.txt') as f:
    file = f.read()
    f.close()

a = file.split('\n\n')

max = 0
number = -1
calList = []
for elfNum, elf in enumerate(a):
    cals = elf.split('\n')

    if cals[-1] == '':
        cals.pop()
    cals = [int(num) for num in cals]

    calList.append(sum(cals))

calList.sort(reverse=True)
print(f'Top 3 total calories: {calList[0] + calList[1] + calList[2]}')
pass