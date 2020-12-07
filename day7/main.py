class Rule:
    def __init__(self, color: str, can_contain: dict):
        self.color: str = color
        self.can_contain: dict = can_contain

    def __str__(self):
        return "Color: " + str(self.color) + " Can Contain: " + str(self.can_contain)

    def __repr__(self):
        return "Color: " + str(self.color) + " Can Contain: " + str(self.can_contain)


def create_rule(rule):
    color, rules = rule.split(' bags contain ')
    rules = rules.split(', ')
    can_contain = {}
    if rules[0].strip() == 'no other bags.':
        return Rule(color, can_contain)
    for rule in rules:
        rule = rule.replace('bags', '').replace('bag', '').replace('.', '')
        can_contain[(rule[1:]).strip()] = rule[:1]
    return Rule(color, can_contain)


def calculate_bags(color: str, rules: dict):
    cost = 0
    rule = rules[color]
    cost += sum([int(value) if value is not None else 0 for value in rule.can_contain.values()])
    if len(rule.can_contain.keys()) == 0:
        return 0
    for color in rule.can_contain.keys():
        cost += int(rule.can_contain[color]) * calculate_bags(color, rules)
    return cost


def day_7():
    with open('input', 'r') as f:
        rule_lines = f.readlines()

    can_contain_gold = ['shiny gold']
    rules = [create_rule(rule) for rule in rule_lines]
    not_done = True
    while not_done:
        length_before_run = len(set(can_contain_gold))
        for rule in rules:
            if any(color in can_contain_gold for color in rule.can_contain.keys()):
                can_contain_gold.append(rule.color)
        if len(set(can_contain_gold)) == length_before_run:
            not_done = False

    print(len(set(can_contain_gold)) - 1)

    rules_dict = {rule.color: rule for rule in rules}
    print(calculate_bags('shiny gold', rules_dict))


if __name__ == '__main__':
    day_7()
