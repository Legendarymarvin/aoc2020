directions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}


def day_12():
    with open('input', 'r') as f:
        instructions = f.readlines()

    part_1(instructions)
    part_2(instructions)


def move_in_direction(north, east, instruction, value):
    if instruction == 'N':
        north += int(value)
    elif instruction == 'S':
        north -= int(value)
    elif instruction == 'E':
        east += value
    elif instruction == 'W':
        east -= value
    return north, east


def determine_direction_from_facing(facing):
    return directions[facing % 4]


def part_1(instructions):
    facing = 0
    north = 0
    east = 0
    for line in instructions:
        instruction, value = line.strip()[:1], int(line.strip()[1:])

        if instruction in directions.values():
            north, east = move_in_direction(north, east, instruction, value)
        elif instruction == 'F':
            forward_direction = determine_direction_from_facing(facing)
            north, east = move_in_direction(north, east, forward_direction, value)
        elif instruction == 'R':
            facing += value / 90
        elif instruction == 'L':
            facing -= value / 90

    print(abs(north), abs(east), abs(east) + abs(north))


def part_2(instructions):
    waypoint_north = 1
    waypoint_east = 10
    north = 0
    east = 0
    for line in instructions:
        instruction, value = line.strip()[:1], int(line.strip()[1:])

        if instruction in directions.values():
            waypoint_north, waypoint_east = move_in_direction(waypoint_north, waypoint_east, instruction, value)
        elif instruction == 'F':
            east += waypoint_east * value
            north += waypoint_north * value
        elif instruction == 'L':
            for i in range(value // 90):
                waypoint_east, waypoint_north = -waypoint_north, waypoint_east
        elif instruction == 'R':
            for i in range(value // 90):
                waypoint_east, waypoint_north = waypoint_north, -waypoint_east
    print(abs(north), abs(east), abs(east) + abs(north))


if __name__ == '__main__':
    day_12()
    