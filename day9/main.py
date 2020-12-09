import itertools
import time


def part_2(number, numbers, input_size):
    numbers = [int(number) for number in numbers]
    for operand_count in range(2, input_size - 1):
        for i in range(0, input_size):
            operands = numbers[i:i + operand_count]
            if sum(operands) == number:
                return min(operands) + max(operands)


def exists_pair(idx, number, numbers, input_size):
    for i in range(idx-25, idx):
        for j in range(idx-25, idx):
            if i != j and numbers[i] + numbers[j] == number:
                return True
    return False


def part_1(numbers, input_size):
    for i in range(25, input_size):
        number = numbers[i]
        if not any(number == a + b for a, b in itertools.permutations(numbers[i - 25:i], 2)):
            return number

        # solution without itertools, little slower 0.0130 vs 0.0155
        # if not exists_pair(i, number, numbers, input_size):
        #     return number


def day_9():
    start = time.time()
    with open('input', 'r') as f:
        numbers = [int(number) for number in f.readlines()]

    input_size = len(numbers)

    part_1_solution = part_1(numbers, input_size)
    print(part_1_solution)
    part_2_solution = part_2(part_1_solution, numbers, input_size)
    print(part_2_solution)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    day_9()