from queue import PriorityQueue

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Node:
    def __init__(self, state, parent, move, g, h):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def generate_children(node):
    children = []
    x, y = find_blank(node.state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in node.state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y],
            )

            h = heuristic(new_state)

            child = Node(
                new_state,
                node,
                (nx, ny),
                node.g + 1,
                h
            )

            children.append(child)

    return children


def print_path(node):
    path = []

    while node:
        path.append(node.state)
        node = node.parent

    path.reverse()

    for step in path:
        for row in step:
            print(row)
        print()


def a_star(start_state):
    open_list = PriorityQueue()
    closed_set = set()

    start_node = Node(
        start_state,
        None,
        None,
        0,
        heuristic(start_state)
    )

    open_list.put(start_node)

    while not open_list.empty():
        current = open_list.get()

        if current.state == goal_state:
            print("Goal State Reached!\n")
            print_path(current)
            return

        closed_set.add(state_to_tuple(current.state))

        children = generate_children(current)

        for child in children:
            if state_to_tuple(child.state) not in closed_set:
                open_list.put(child)

    print("No Solution Found")


start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

a_star(start_state)
