score = 0
with open('input', 'r') as f:
    for line in f:
        opponent, response = line.split()
        match response:
            case 'X':
                score += 1
            case 'Y':
                score += 2
            case 'Z':
                score += 3
            case _:
                raise ValueError
        opponent = ord(opponent) - ord('A')
        response = ord(response) - ord('X')
        match (response - opponent) % 3:
            case 2:
                score += 0
            case 0:
                score += 3
            case 1:
                score += 6
            case _:
                raise ValueError 
print(score)

score = 0
with open('input', 'r') as f:
    for line in f:
        opponent, outcome = line.split()
        opponent = ord(opponent) - ord('A')
        outcome = ord(outcome) - ord('X')
        response = (opponent - -(outcome - 1)) % 3
        match response:
            case 0:
                score += 1
            case 1:
                score += 2
            case 2:
                score += 3
            case _:
                raise ValueError
        match (response - opponent) % 3:
            case 2:
                score += 0
            case 0:
                score += 3
            case 1:
                score += 6
            case _:
                raise ValueError 
print(score)
