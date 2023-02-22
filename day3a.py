from math import floor

ORDLOWER = 96
ORDUPPER = 38

with open('day3_input.txt') as f:
    file = f.read()
    f.close()

sacks = file.split('\n')
sacks.pop()

prio = 0

for sack in sacks:
    l = len(sack)

    first = sack[:floor(l/2)]
    first = [*set(first)]
    second = sack[floor(l/2):]

    for letter in first:
        if second.find(letter) != -1:
            if letter.isupper():
                prio += ord(letter) - ORDUPPER
            else:
                prio += ord(letter) - ORDLOWER

print(f"Sum of priorities: {prio}")