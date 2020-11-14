from copy import deepcopy


class Atom:
    negation: bool
    predicate: str
    terms: list

    def __init__(self, negation, predicate, terms):
        self.negation = negation
        self.predicate = predicate
        self.terms = terms

    @classmethod
    def from_str(cls, atom_str):
        negation = False
        predicate = None
        terms = []
        atom_str = atom_str.replace("'", '"')
        open_prt_index = atom_str.find('(')
        close_prt_index = atom_str.find(')')
        if open_prt_index != -1 and close_prt_index != -1:
            head = atom_str[:open_prt_index]
            negation_index = head.find('\\+')
            if negation_index == -1:
                negation = False
                predicate = head.strip()
            else:
                negation = True
                predicate = head[negation_index + 2:].strip()
            terms_str = atom_str[open_prt_index + 1:close_prt_index].split(',')
            terms = [x.strip() for x in terms_str]
        return cls(negation, predicate, terms)

    def __eq__(self, other):
        return self.negation == other.negation \
               and self.predicate == other.predicate \
               and self.terms == other.terms

    def __str__(self):
        s = ''
        if self.negation:
            s = '\\+ '
        return s + self.predicate + '(' + ', '.join(self.terms) + ')'

    def is_ground(self):
        ground_flag = True
        for term in self.terms:
            if is_variable(term):
                ground_flag = False
                break
        return ground_flag

    def substitute(self, subs_dict):
        atom = deepcopy(self)
        for i in range(len(atom.terms)):
            if atom.terms[i] in subs_dict:
                atom.terms[i] = subs_dict[atom.terms[i]]
        return atom

    def unify(self, other):
        subs_dict = dict()
        for i in range(len(self.terms)):
            if is_variable(self.terms[i]):
                subs_dict[self.terms[i]] = other.terms[i]
            elif not is_variable(other.terms[i]) and self.terms[i] != other.terms[i]:
                subs_dict.clear()
                break
        return subs_dict


def is_variable(term: str):
    flag = False
    if term[-1] == '?' or (term[0].isalpha() and term[0] == term[0].upper()):
        flag = True
    return flag


def is_question_variable(term: str):
    return term[-1] == '?'
