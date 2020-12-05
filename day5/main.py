def binary_search_id(partition):
    partition = partition.replace('F', '0')
    partition = partition.replace('L', '0')
    partition = partition.replace('B', '1')
    partition = partition.replace('R', '1')
    return int(partition, 2)


def calculate_id(boardingpass):
    row_part = boardingpass[:7]
    column_part = boardingpass[-4:]
    row = binary_search_id(row_part)
    column = binary_search_id(column_part)
    return row * 8 + column


def day_5():
    with open('input', 'r') as f:
        boardingpasses = f.readlines()

    max_id = 0

    for boardingpass in boardingpasses:
        seat_id = calculate_id(boardingpass)
        if seat_id > max_id:
            max_id = seat_id

    print(max_id)


if __name__ == '__main__':
    day_5()
