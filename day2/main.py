# AOC Day 2
import re


def main():
    valid_password_count = 0
    valid_password_count_old_policy = 0

    with open('input', 'r') as f:
        for line in f:
            min_count, max_count, search_char, _, password = re.split('[- :]', line.strip())

            if int(min_count) <= password.count(search_char) <= int(max_count):
                valid_password_count += 1

            if (password[int(min_count) - 1] is search_char) ^ (password[int(max_count) - 1] is search_char):
                valid_password_count_old_policy += 1

        print("Part 1: " + str(valid_password_count))
        print("Part 2: " + str(valid_password_count_old_policy))


if __name__ == '__main__':
    main()
