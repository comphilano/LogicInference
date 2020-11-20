from atom import Atom


class HornClause:
    """
    Horn clauses are represented in implication form. Each horn
    clauses can have zero or one conclusion and a positive amount
    of premises.\n
    Conclusion and premises are atomic formula.\n
    Horn clauses can be facts, rules, goals and queries.\n
    Facts have one conclusion with no free variable and no premise.\n
    Goals have no conclusion and all premises are ground.\n
    Queries have no conclusion and one or more premises that contain
    free variables.
    """
    premises: list
    conclusion: Atom

    def __init__(self, conclusion, premises):
        self.conclusion = conclusion
        self.premises = premises

    def __str__(self):
        if self.conclusion:
            s = str(self.conclusion)
            if self.premises:
                s += ' :- '
        else:
            s = '?- '
        s += ', '.join([str(x) for x in self.premises]) + '.'
        return s

    @classmethod
    def from_str(cls, clause_str):
        """
        Creates a Horn clause from a Horn clause string.

        :param clause_str:
        :return: HornClause
        """
        if clause_str[-1] != '.' or clause_str.find(';') != -1:
            raise ValueError('Invalid clause.')
        conclusion_str, premises_str = split_clause(clause_str)
        premises = []
        conclusion = None
        if conclusion_str:
            conclusion = Atom.from_str(conclusion_str)
        for p in premises_str:
            premises.append(Atom.from_str(p))
        return cls(conclusion, premises)

    @staticmethod
    def parse(clause_str):
        """
        Parse a clause string into clauses

        :param clause_str:
        :return: list - List of clauses
        """
        if clause_str[-1] != '.':
            raise ValueError('Invalid clause.')
        clauses = []
        if clause_str.find('%') == -1:
            new_clause_str = split_or_clause(clause_str)
            for for_str in new_clause_str:
                clauses.append(HornClause.from_str(for_str))
        return clauses

    def get_variables(self):
        var = set({})
        if self.conclusion:
            var = self.conclusion.get_variables()
        for premise in self.premises:
            var = var.union(premise.get_variables())
        return var

    def is_fact(self):
        return self.conclusion is not None and not self.premises

    def is_rule(self):
        return self.conclusion is not None and self.premises

    #def is_goal(self):
    #    return self.conclusion is None and self.premises and not self.get_variables()

    def is_query(self):
        return self.conclusion is None and self.premises

    def is_nothing(self):
        return self.conclusion is None and not self.premises

    def substitute(self, subs_dict):
        """
        Substitute variables in clauses with their values in dictionary

        :param subs_dict: A map from old variables to new values
        :return: HornClause - A clause with their variables substituted
        """
        premises = []
        conclusion = None
        if self.conclusion is not None:
            conclusion = self.conclusion.substitute(subs_dict)
        for premise in self.premises:
            premises.append(premise.substitute(subs_dict))
        return HornClause(conclusion, premises)


def split_or_clause(or_clause_str):
    """
    Split a clause that has disjunctive premises into clauses
    that has only conjunctive premises (Horn clauses).

    :param or_clause_str:
    :return: list of Horn
    """
    horn_clauses_str = or_clause_str
    if or_clause_str.find(';'):
        arrow_index = or_clause_str.find(':-')
        horn_clauses_str = or_clause_str.replace(';', '.' + or_clause_str[:arrow_index + 2])
    horn_clauses = [x + '.' for x in horn_clauses_str.split('.') if x]
    return horn_clauses


def split_clause(clause_str: str):
    """
    Split clause into atoms

    :param clause_str:
    :return: tuple - conclusion and list of premises
    """
    skip_comma = False
    x = clause_str.split(':-')
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


def get_clauses_from_file(filename):
    """
    Get clauses from file.\n
    Clauses are written in Prolog syntax.
    Clauses can be facts, rules, goals or queries.
    Queries should be written as rules with empty conclusion.

    :param filename: str - Name of the file
    :return: list - A list of clauses
    """
    with open(filename, 'r', encoding='utf8') as kb_file:
        data = kb_file.read()
    data = data.replace('\n', '')
    clause_str = [x + '.' for x in data.split('.')]
    clause_str.pop()
    clauses = []
    for s in clause_str:
        clauses.extend(HornClause.parse(s))
    return clauses

