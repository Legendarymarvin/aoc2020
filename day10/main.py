def day_10():
    with open('input', 'r') as f:
        joltages = [int(joltage) for joltage in f.readlines()]

    joltages.sort()
    part_1(joltages)
    part_2(joltages)


def part_1(joltages):
    single_joltage_differences = 1 if joltages[0] == 1 else 0
    three_joltage_differences = 3 if joltages[0] == 3 else 0

    for idx, joltage in enumerate(joltages):
        if idx >= len(joltages) - 1:
            break

        joltage_difference = joltages[idx + 1] - joltage

        if joltage_difference == 1:
            single_joltage_differences += 1
        elif joltage_difference == 3:
            three_joltage_differences += 1
        else:
            print('something went horribly wrong ', joltage, joltage[idx+1], joltage_difference)

    # jump to device seems to count as well
    three_joltage_differences += 1
    print(single_joltage_differences * three_joltage_differences)


def part_2(joltages):
    arrangements_per_joltage = {}
    print(search_for_arrangements(0, arrangements_per_joltage, joltages[-1], joltages))


def search_for_arrangements(joltage, arrangements_per_joltage, end, joltages):
    if joltage in arrangements_per_joltage:
        return arrangements_per_joltage[joltage]
    if joltage == end:
        return 1

    new_arrangements = 0
    for i in [1, 2, 3]:
        if joltage + i in joltages:
            new_arrangements += search_for_arrangements(joltage + i, arrangements_per_joltage, end, joltages)

    arrangements_per_joltage[joltage] = new_arrangements
    return new_arrangements


if __name__ == '__main__':
    day_10()