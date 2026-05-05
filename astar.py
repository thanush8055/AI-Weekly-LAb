from queue import PriorityQueue

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}


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


def generate_children(node):

    children = []

    x, y = find_blank(node.state)

    for move_name, (dx, dy) in moves.items():

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in node.state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            child = Node(
                new_state,
                node,
                move_name,
                node.g + 1,
                heuristic(new_state)
            )

            children.append(child)

    return children


def print_solution(node):

    path = []
    moves_list = []

    while node:

        path.append(node.state)

        if node.move:
            moves_list.append(node.move)
 
        node = node.parent

    path.reverse()
    moves_list.reverse()

    print("Sequence of Moves:\n")

    for i, move in enumerate(moves_list, start=1):
        print("Move", i, ":", move)

    print("\nPuzzle States:\n")

    for state in path:

        for row in state:
            print(row)

        print()


def a_star(start_state):

    open_list = PriorityQueue()
    visited = set()

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

            print_solution(current)

            return

        visited.add(str(current.state))

        for child in generate_children(current):

            if str(child.state) not in visited:
                open_list.put(child)

    print("No Solution Found")


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

a_star(initial_state)
