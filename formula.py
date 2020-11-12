import re
from atom import Atom


class Formula:
    premises: list
    conclusion: Atom

    def __init__(self, formula_str: str):
        formula_strs = re.findall(r'[\w\s]+\(+[^\)]+\)', formula_str)
        self.premises = []
        self.conclusion = Atom(formula_strs[0])
        for premises_str in formula_strs[1:]:
            self.premises.append(Atom(premises_str))

    def __str__(self):
        if self.premises:
            s = self.conclusion.__str__() + ' :- ' + ', '.join([x.__str__() for x in self.premises])
        else:
            s = s = self.conclusion.__str__()
        return s
