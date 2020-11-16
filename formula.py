from atom import Atom


class Formula:
    premises: list
    conclusion: Atom

    def __init__(self, conclusion, premises):
        self.conclusion = conclusion
        self.premises = premises

    @classmethod
    def from_str(cls, formula_str):
        if formula_str[-1] != '.':
            raise ValueError('Invalid formula.')
        conclusion_str, premises_str = split_formula(formula_str)
        premises = []
        conclusion = None
        if conclusion_str:
            conclusion = Atom.from_str(conclusion_str)
        for p in premises_str:
            premises.append(Atom.from_str(p))
        return cls(conclusion, premises)

    @staticmethod
    def parse(formula_str):
        if formula_str[-1] != '.':
            raise ValueError('Invalid formula.')
        formula_str.strip()
        formulas = []
        if formula_str[0] != '%':
            new_formula_str = split_or_formula(formula_str)
            for for_str in new_formula_str:
                formulas.append(Formula.from_str(for_str))
        return formulas

    def __str__(self):
        if self.premises:
            if self.conclusion is not None:
                s = self.conclusion.__str__() + ' :- ' + ', '.join([x.__str__() for x in self.premises]) + '.'
            else:
                s = '?- ' + ', '.join([x.__str__() for x in self.premises]) + '.'
        else:
            if self.conclusion is not None:
                s = self.conclusion.__str__() + '.'
            else:
                s = '?-.'
        return s

    def is_question(self):
        return self.conclusion is None

    def is_nothing(self):
        return self.conclusion is None and not self.premises

    def is_fact(self):
        return not self.premises

    def substitute(self, subs_dict):
        premises = []
        conclusion = None
        if self.conclusion is not None:
            conclusion = self.conclusion.substitute(subs_dict)
        for premise in self.premises:
            premises.append(premise.substitute(subs_dict))
        return Formula(conclusion, premises)


def split_or_formula(or_formula_str):
    if or_formula_str.find(';'):
        arrow_index = or_formula_str.find(':-')
        or_formula_str = or_formula_str.replace(';', '.' + or_formula_str[:arrow_index + 2])
    or_formula_str = [x + '.' for x in or_formula_str.split('.') if x]
    return or_formula_str


def split_formula(formula_str: str):
    skip_comma = False
    x = formula_str.split(':-')
    if len(x) > 1:
        conclusion = x[0]
        origin_premises = x[1]
    else:
        conclusion = x[0][:-1]
        origin_premises = []
    premises = []
    split_index = 0
    for i in range(len(origin_premises)):
        if origin_premises[i] == '(':
            skip_comma = True
        elif origin_premises[i] == ')':
            skip_comma = False
        elif (origin_premises[i] == ',' and not skip_comma) or origin_premises[i] == '.':
            premises.append(origin_premises[split_index:i])
            split_index = i + 1
    return conclusion, premises


def get_formulas_from_file(filename):
    """
    Get formulas from file.\n
    Formulas are written in Prolog syntax.
    Formulas can be facts, rules, goals or queries.
    Queries should be written as rules with empty conclusion.

    :param filename: str - Name of the file
    :return: list - A list of formulas
    """
    with open(filename, 'r') as kb_file:
        data = kb_file.read()
    data = data.replace('\n', '')
    for_str = [x + '.' for x in data.split('.')]
    for_str.pop()
    formulas = []
    for s in for_str:
        formulas.extend(Formula.parse(s))
    return formulas

