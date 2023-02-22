from math import floor

ORDLOWER = 96
ORDUPPER = 38

with open('day3_input.txt') as f:
    file = f.read()
    f.close()

sacks = file.split('\n')
sacks.pop()

prio = 0

for i in range(0, len(sacks), 3):
    sack1 = sacks[i]
    sack2 = sacks[i+1]
    sack3 = sacks[i+2]

    sack1 = [*set(sack1)]

    match1 = []
    for letter in sack1:
        if sack2.find(letter) != -1:
            match1.append(letter)

    for letter in match1:
        if sack3.find(letter) != -1:
            if letter.isupper():
                prio += ord(letter) - ORDUPPER
            else:
                prio += ord(letter) - ORDLOWER

print(f"Sum of priorities: {prio}")