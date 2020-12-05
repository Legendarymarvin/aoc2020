def convert_to_binary_and_int(partition):
    partition = partition.replace('F', '0')
    partition = partition.replace('L', '0')
    partition = partition.replace('B', '1')
    partition = partition.replace('R', '1')
    return int(partition, 2)


def calculate_id(boardingpass):
    row_part = boardingpass[:7]
    column_part = boardingpass[-4:]
    row = convert_to_binary_and_int(row_part)
    column = convert_to_binary_and_int(column_part)
    return row * 8 + column


def create_seat_ids(boarding_passes):
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_id = calculate_id(boarding_pass)
        seat_ids.append(seat_id)

    seat_ids.sort()
    return seat_ids


def get_your_id(seat_ids_sorted):
    id = 0
    for seat_id, idx in enumerate(seat_ids_sorted):
        if seat_ids_sorted[idx] + 1 < seat_ids_sorted[idx + 1]:
            id = seat_ids_sorted[idx] + 1
            break
    return id


def day_5():
    with open('input', 'r') as f:
        boarding_passes = f.readlines()

    seat_ids_sorted = create_seat_ids(boarding_passes)
    print("Part 1: " + str(seat_ids_sorted[-1]))

    your_id = get_your_id(seat_ids_sorted)
    print("Part 2: " + str(your_id))


if __name__ == '__main__':
    day_5()
