tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dls(node, depth, limit, visited):
    if depth > limit:
        return
    visited.append(node)
    for neighbor in tree[node]:
        dls(neighbor, depth + 1, limit, visited)

# Run DLS for different depth limits
for limit in range(3):
    visited = []
    dls(1, 0, limit, visited)
    print(f"For Depth {limit}:", *visited)
