def viewing_distance(tree_house_height: int, line_of_sight: list[int]) -> int:
    distance = 0
    for tree in line_of_sight:
        if tree >= tree_house_height:
            distance += 1
            break
        distance += 1
    return distance


trees: list[list[int]] = []
with open('input', 'r') as f:
    for line in f:
        trees.append(list(map(int, line.strip())))
trees_inv = tuple(zip(*trees))
m = len(trees)
n = len(trees_inv)

visible_count = 2 * (m + n - 2)
max_visibility = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        tree = trees[i][j]
        visible = (
            tree > max(trees[i][:j]) or
            tree > max(trees[i][j+1:]) or
            tree > max(trees_inv[j][:i]) or
            tree > max(trees_inv[j][i+1:])
        )
        if visible:
            visible_count += 1
        
        visibility_score = (
            viewing_distance(tree, trees[i][j-1::-1])
            * viewing_distance(tree, trees[i][j+1:])
            * viewing_distance(tree, trees_inv[j][i-1::-1])
            * viewing_distance(tree, trees_inv[j][i+1:])
        )
        max_visibility = max(max_visibility, visibility_score)
print(visible_count)
print(max_visibility)
