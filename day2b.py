with open('day2_input.txt') as f:
    file = f.read()
    f.close()

rounds = file.split('\n')
rounds.pop()

score = 0
for round in rounds:
    op = round.split(' ')[0]
    play = round.split(' ')[1]

    # lose
    if play == 'X':

        if op == 'A':
            score += 3
        elif op == 'B':
            score += 1
        elif op == 'C':
            score += 2

    # draw
    elif play == 'Y':

        if op == 'A':
            score += 1
            score += 3
        elif op == 'B':
            score += 2
            score += 3
        elif op == 'C':
            score += 3
            score += 3

    # win
    elif play == 'Z':

        if op == 'A':
            score += 2
            score += 6
        elif op == 'B':
            score += 3
            score += 6
        elif op == 'C':
            score += 1
            score += 6

print(f'Score: {score}\n')