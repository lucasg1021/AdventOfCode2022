with open('day2_input.txt') as f:
    file = f.read()
    f.close()

rounds = file.split('\n')
rounds.pop()

score = 0
for round in rounds:
    op = round.split(' ')[0]
    play = round.split(' ')[1]

    if play == 'X':
        score += 1

        if op == 'C':
            score += 6
        elif op == 'A':
            score += 3

    elif play == 'Y':
        score += 2

        if op == 'A':
            score += 6
        elif op == 'B':
            score += 3

    elif play == 'Z':
        score += 3

        if op == 'B':
            score += 6
        elif op == 'C':
            score += 3

print(f'Score: {score}\n')