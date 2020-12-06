def day_6():
    with open('input', 'r') as f:
        answers = f.readlines()

    answer_groups = ''.join(answers).split('\n\n')
    answer_counts_anyone = []
    answer_counts_everyone = []

    for group in answer_groups:
        answer_counts_anyone.append(count_unique_answers(group))
        answer_counts_everyone.append(count_intersection_answers(group))

    print("Part 1: " + str(sum(answer_counts_anyone)))
    print("Part 2: " + str(sum(answer_counts_everyone)))

    # just for fun, do it in one line
    print([sum(x) for x in zip(*[(len(set(group.replace('\n', ''))), len(set.intersection(*map(set, group.split())))) for group in ''.join(open('input', 'r').readlines()).split('\n\n')])])


def count_intersection_answers(group) -> int:
    return len(set.intersection(*map(set, group.split())))


def count_unique_answers(group) -> int:
    return len(set(group.replace('\n', '')))


if __name__ == '__main__':
    day_6()
