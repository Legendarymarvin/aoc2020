class Position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return "X: " + str(self.x) + ", Y: " + str(self.y)


def count_trees_for_movement_pattern(field, step_x, step_y):
    base_length = len(field[0])
    finish_y = len(field)
    trees = 0
    position = Position(0, 0)

    while position.y < finish_y:
        if field[position.y][position.x % base_length] == '#':
            trees += 1
        position.move(step_x, step_y)

    return trees


def count_tree_hits():
    with open('input', 'r') as f:
        field = [x.strip() for x in f.readlines()]

    trees = count_trees_for_movement_pattern(field, 3, 1)
    print("Part 1: " + str(trees))

    all_tree_hits = [count_trees_for_movement_pattern(field, x, y) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    all_tree_count = 1
    for hits in all_tree_hits:
        all_tree_count *= hits
    print("Part 2: " + str(all_tree_count))


if __name__ == '__main__':
    count_tree_hits()
