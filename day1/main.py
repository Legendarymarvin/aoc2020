#AOC Day 1
import itertools


def main():
    lines = open('input').readlines()
    numbers = list(map(int, lines))
    for number in numbers:
        if 2020 - number in numbers:
            print("Part 1 " + str(number * (2020-number)))

    for triple in itertools.combinations(numbers, 3):
        if sum(triple) == 2020:
            print("Part 2 " + str(triple[0] * triple[1] * triple[2]))


if __name__ == '__main__':
    main()

