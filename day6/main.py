def day_6():
    with open('input', 'r') as f:
        answers = f.readlines()

    answer_groups = ''.join(answers).split('\n\n')
    answer_counts = []

    for group in answer_groups:
        group = group.replace('\n', '')
        answer_counts.append(len(set(group)))

    print("Part 1: " + str(sum(answer_counts)))

    answer_for_everyone_counts = []
    count = 0

    for group in answer_groups:
        people_answers = group.split()
        answers_for_everyone = list(set.intersection(*map(set, people_answers)))
        answer_for_everyone_counts.append(len(answers_for_everyone))

    print("Part 2: " + str(sum(answer_for_everyone_counts)))


if __name__ == '__main__':
    day_6()
