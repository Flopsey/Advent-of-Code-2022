count1 = count2 = 0
with open('input', 'r') as f:
    for line in f:
        pair = line.strip().split(',')
        assignment1, assignment2 = (assignment.split('-') for assignment in pair)
        assignment1 = range(int(assignment1[0]), int(assignment1[1]) + 1)
        assignment2 = range(int(assignment2[0]), int(assignment2[1]) + 1)
        if all(x in assignment1 for x in assignment2) or all(x in assignment2 for x in assignment1):
            count1 += 1
        if any(x in assignment1 for x in assignment2) or any(x in assignment2 for x in assignment1):
            count2 += 1
print(count1)
print(count2)
