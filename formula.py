import re
from atom import Atom


class Formula:
    premises: list
    conclusion: Atom

    def __init__(self, conclusion, premises):
        self.conclusion = conclusion
        self.premises = premises

    @classmethod
    def from_str(cls, formula_str):
        for_str = re.findall(r'(?:\\\+)?[\w\s]+\([^)]+\)', formula_str)
        premises = []
        conclusion = None
        if for_str:
            if formula_str.find('?-') == -1:
                conclusion = Atom.from_str(for_str[0])
                for premises_str in for_str[1:]:
                    premises.append(Atom.from_str(premises_str))
            else:
                conclusion = None
                for premises_str in for_str:
                    premises.append(Atom.from_str(premises_str))
        return cls(conclusion, premises)

    @staticmethod
    def parse(formula_str):
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
    or_formula_str = or_formula_str.split('.')
    return or_formula_str
