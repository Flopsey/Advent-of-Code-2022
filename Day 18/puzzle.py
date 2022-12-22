voxels = set()
with open('input', 'r') as f:
    for line in f:
        voxels.add((*map(int, line.split(',')),))

area = 0
for x, y, z in voxels:
    neighbors = (
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    )
    for neighbor in neighbors:
        if neighbor not in voxels:
            area += 1
print(area)
