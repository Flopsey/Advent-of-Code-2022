def calc_score(opponent, response):
    return (response + 1) + (((response - opponent + 1) % 3) * 3)


score1 = score2 = 0
with open('input', 'r') as f:
    for line in f:
        opponent, col2 = line.split()
        opponent = ord(opponent) - ord('A')
        col2 = ord(col2) - ord('X')
        score1 += calc_score(opponent, col2)
        score2 += calc_score(opponent, (opponent + (col2 - 1)) % 3)
print(score1)
print(score2)
