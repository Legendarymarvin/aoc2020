import re

necessary_fields = ['byr', 'eyr', 'iyr', 'hgt', 'pid', 'hcl', 'ecl']


def process_to_dict(passport) -> dict:
    dict_passport = {}
    for field in passport:
        if not field.strip() == '':
            dict_passport[field.split(':')[0]] = field.split(':')[1]
    return dict_passport


def is_valid_year_within(year, min_year, max_year):
    return re.compile(r'^\d{4}$').match(year) and min_year <= int(year) <= max_year


def is_valid_birth_year(param):
    return is_valid_year_within(param, 1920, 2002)


def is_valid_issue_year(param):
    return is_valid_year_within(param, 2010, 2020)


def is_valid_expiration_year(param):
    return is_valid_year_within(param, 2020, 2030)


def is_valid_height(param):
    valid_format = re.compile(r'^\d+(in|cm)$').match(param.strip())
    if valid_format is None:
        return False
    height = param[:-2]
    unit = param[-2:]
    if unit == 'cm':
        return 150 <= int(height) <= 193
    if unit == 'in':
        return 59 <= int(height) <= 76


def is_valid_hair_color(param):
    return re.compile(r'^#[a-f0-9]{6}$').match(param) is not None


def is_valid_eye_color(param):
    return param in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_password_id(param):
    return re.compile(r'^\d{9}$').match(param) is not None


def fields_are_valid(passport: dict) -> bool:
    return is_valid_birth_year(passport.get('byr')) and is_valid_issue_year(passport.get('iyr')) and is_valid_expiration_year(passport.get('eyr')) and is_valid_height(passport.get('hgt')) and is_valid_hair_color(passport.get('hcl')) and is_valid_eye_color(passport.get('ecl')) and is_valid_password_id(passport.get('pid'))


def count_more_strict_validation_valid_passports(passports) -> int:
    valid_passports = 0
    for passport in passports:
        if has_all_necessary_fields(passport) and fields_are_valid(passport):
            valid_passports += 1
    return valid_passports


def has_all_necessary_fields(passport: dict) -> bool:
    return all(field in passport for field in necessary_fields)


def weaken_airport_security():
    passports = read_passports_from_input()
    valid_passports = sum (1 for passport in passports if has_all_necessary_fields(passport))

    print("Part 1: " + str(valid_passports))

    valid_passports = count_more_strict_validation_valid_passports(passports)

    print("Part 2: " + str(valid_passports))


def read_passports_from_input():
    with open('input', 'r') as f:
        passports_lines = f.readlines()
    passports_string_list = ''.join(passports_lines).split('\n\n')
    passports_field_list = [re.split(' |\n', passport) for passport in passports_string_list]
    passports = [process_to_dict(passport) for passport in passports_field_list]
    return passports


if __name__ == '__main__':
    weaken_airport_security()
