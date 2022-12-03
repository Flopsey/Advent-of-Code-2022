score1 = 0
score2 = 0
with open('input', 'r') as f:
    for line in f:
        opponent, col2 = line.split()
        opponent = ord(opponent) - ord('A')
        col2 = ord(col2) - ord('X')
        response1 = col2
        response2 = (opponent + (col2 - 1)) % 3
        score1 += response1 + 1
        score2 += response2 + 1
        score1 += ((response1 - opponent + 1) % 3) * 3
        score2 += ((response2 - opponent + 1) % 3) * 3
print(score1)
print(score2)
