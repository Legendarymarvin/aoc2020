def guess_we_are_bruteforcing_this(instructions):
    all_the_inputs = create_all_possible_changed_inputs(instructions)

    for changed_input in all_the_inputs:
        run(changed_input, False)


def create_all_possible_changed_inputs(instructions):
    all_the_inputs = []
    for idx, instruction in enumerate(instructions):
        new_input = instructions[:]
        is_negative, op_code, value = deconstruct_instruction(instruction)
        changed = False

        if op_code == 'jmp':
            changed = True
            new_input[idx] = 'nop ' + ('-' if is_negative else '+') + str(value)

        elif op_code == 'nop':
            changed = True
            new_input[idx] = ('jmp ' + ('-' if is_negative else '+') + str(value))

        if changed:
            all_the_inputs.append(new_input)
    return all_the_inputs


def run(instructions, is_first_part: bool):
    cache = 0
    idx = 0
    executed_ops = []
    not_done = True
    while not_done:
        if idx in executed_ops:
            if is_first_part:
                print(cache)
            not_done = False
            continue

        if idx >= len(instructions):
            print("Finished " + str(cache))
            not_done = False
            continue

        executed_ops.append(idx)

        instruction = instructions[idx].strip()
        is_negative, op_code, value = deconstruct_instruction(instruction)

        if op_code == 'nop':
            idx += 1
        elif op_code == 'acc':
            idx += 1
            if is_negative:
                cache -= value
            else:
                cache += value
        elif op_code == 'jmp':
            if is_negative:
                idx -= value
            else:
                idx += value
        else:
            print('something somewhere went somehow terribly wrong')


def deconstruct_instruction(instruction):
    op_code = instruction[:3].strip()
    is_negative = True if '-' in instruction else False
    value = int(instruction[5:].strip())
    return is_negative, op_code, value


def day_8():
    with open('input', 'r') as f:
        instructions = f.readlines()

    print("Part 1: ")
    run(instructions, True)

    print("Part 2: ")
    guess_we_are_bruteforcing_this(instructions)


if __name__ == '__main__':
    day_8()