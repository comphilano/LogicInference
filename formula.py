from copy import deepcopy
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
        if formula_str.find('?-') == -1:
            conclusion = Atom.from_str(for_str[0])
            for premises_str in for_str[1:]:
                premises.append(Atom.from_str(premises_str))
        else:
            conclusion = None
            for premises_str in for_str:
                premises.append(Atom.from_str(premises_str))
        return cls(conclusion, premises)

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
        f = deepcopy(self)
        if f.conclusion is not None:
            f.conclusion = f.conclusion.substitute(subs_dict)
        for i in range(len(f.premises)):
            f.premises[i] = f.premises[i].substitute(subs_dict)
        return f