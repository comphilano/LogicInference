import re


class Atom:
    """
    Atomic formula (atom) is a formula with
    no deeper propositional structure, that is, a formula that
    contains no logical connectives or equivalently a formula
    that has no strict sub-formulas.\n
    E.g. parent(X, Y), child(a, b)
    """
    negation: bool
    predicate: str
    terms: list

    def __init__(self, negation, predicate, terms):
        self.negation = negation
        self.predicate = predicate
        self.terms = terms

    def __str__(self):
        s = ''
        if self.negation:
            s = '\\+ '
        return s + self.predicate + '(' + ', '.join(self.terms) + ')'

    def __eq__(self, other):
        return self.negation == other.negation \
               and self.predicate == other.predicate \
               and self.terms == other.terms

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_str(cls, atom_str: str):
        """
        Creates an atom from string, the atom string should be
        written in Prolog syntax.

        :param atom_str: str - an atom string
        :return: Atom
        """
        atom_str = atom_str.strip()
        atom_str = atom_str.replace("'", '"')
        negation = False
        operator = is_cmp_str(atom_str)
        if operator is not None:
            predicate = operator
            terms = [x.strip() for x in atom_str.split(operator)]
        else:
            atom = re.findall(r'(\\\+)?([\w\s]+)\(([^)]+)\)', atom_str)
            if not atom:
                raise ValueError('Invalid atom: ' + atom_str)
            negation = atom[0][0].strip() == '\\+'
            predicate = atom[0][1].strip()
            terms = [x.strip() for x in atom[0][2].split(',')]
        return cls(negation, predicate, terms)

    def eval_cmp(self):
        """
        Evaluates comparison of two terms if the atom is relational formula.

        :return: bool - Results of the comparison
        """
        if not self.is_cmp_atom():
            raise ValueError('This is not a comparison atom.')
        if not self.is_ground():
            raise TypeError('Arguments are not sufficiently instantiated.')
        if self.predicate == '\\==':
            op = '!='
        else:
            op = self.predicate
        try:
            res = eval('float(self.terms[0])' + op + 'float(self.terms[1])')
        except ValueError:
            res = eval('self.terms[0]' + op + 'self.terms[1]')
        return res

    def get_variables(self):
        var = set({})
        for term in self.terms:
            if is_variable(term):
                var.add(term)
        return var

    def is_cmp_atom(self):
        return is_cmp_str(self.predicate)

    def is_ground(self):
        """
        Check if atom is ground, a ground atom is an atom without
        free variables. In other words, its terms are instantiated.

        :return: bool - True if the atom is ground
        """
        ground_flag = True
        for term in self.terms:
            if is_variable(term):
                ground_flag = False
                break
        return ground_flag

    def substitute(self, subs_dict):
        """
        Substitute variables with their values in dictionary

        :param subs_dict: dict - A map from old variables to new values
        :return: Atom - An atom with their variables substituted
        """
        terms = []
        for term in self.terms:
            if term in subs_dict:
                terms.append(subs_dict[term])
            else:
                terms.append(term)
        return Atom(self.negation, self.predicate, terms)


def unify(atom_1: Atom, atom_2: Atom):
    """
    Returns a dict that maps variables of two atoms so that they become identical.

    :param atom_1: Atom - first_atom
    :param atom_2: Atom - second_atom
    :return: dict
    """
    subs_dict = dict()
    for i in range(len(atom_1.terms)):
        if is_variable(atom_1.terms[i]):
            subs_dict[atom_1.terms[i]] = atom_2.terms[i]
        elif is_variable(atom_2.terms[i]):
            subs_dict[atom_2.terms[i]] = atom_1.terms[i]
        else:
            if atom_1.terms[i] != atom_2.terms[i]:
                subs_dict.clear()
                break
    return subs_dict


def is_variable(term: str):
    flag = False
    if term[0] == '_' or term[-1] == '?' or (term[0].isalpha() and term[0] == term[0].upper()):
        flag = True
    return flag


def is_query_variable(term: str):
    return term[-1] == '?'


def is_cmp_str(s: str):
    res = None
    cmp_op = ['\\==', '==', '>=', '>', '<=', '<']
    for op in cmp_op:
        if s.find(op) != -1:
            res = op
            break
    return res