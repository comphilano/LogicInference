from atom import is_variable, is_query_variable, unify
from horn_clause import HornClause, get_clauses_from_file
from atom import Atom


class KnowledgeBase:
    """
    A knowledge-base contains facts, rules and can be queries.
    """
    clauses: list
    # Dictionary of predicates, contains first index and count
    pred_dict: dict

    def __init__(self, clauses):
        self.clauses = []
        self.pred_dict = {}
        self.tell_clauses(clauses)

    def __getitem__(self, key):
        return self.clauses[key]

    def get_clauses(self, p):
        """
        Find all clauses that have predicate p.

        :param p: predicate
        :return: list - List of clauses
        """
        if p not in self.pred_dict:
            clauses = []
        else:
            clause_indexes = self.pred_dict[p]
            clauses = [self.clauses[i] for i in clause_indexes]
        return clauses

    def tell(self, clause):
        """
        Put a clause into knowledge-base

        :param clause:
        :return:
        """
        key = clause.conclusion.predicate
        if key in self.pred_dict:
            self.pred_dict[key].append(len(self.clauses))
        else:
            self.pred_dict[key] = [len(self.clauses)]
        self.clauses.append(clause)

    def tell_clauses(self, clauses):
        """
        Put clauses in the list into knowledge-base

        :param clauses:
        :return:
        """
        for clause in clauses:
            self.tell(clause)

    def __ask_recursive(self, query, find_all=False):
        """
        Recursively querying a clause.\n
        Idea: A clause with n premises is satisfied if the first premise of clause
        is in knowledge-base and a clause contains n - 1 premises (not included first one)
        is satisfied.

        :param query:
        :param find_all: find all solutions if True
        :return: tuple - found is True if found a solution, solutions is a list of satisfied variables
        """
        # Initialise
        solutions = []
        found = False

        # Put all comparison premises to the back of premise list.
        # Because comparison only works when all variables are
        # instantiated.
        for i in range(len(query.premises)):
            if query.premises[i].is_cmp_atom():
                query.premises.append(query.premises.pop(0))
            else:
                break

        first_premise = query.premises[0]
        remain_query = HornClause(None, query.premises[1:])

        # Evaluate comparison premise.
        if first_premise.is_cmp_atom():
            try:
                found = first_premise.eval_cmp()
            except TypeError:
                found = False

        known_clauses = self.get_clauses(first_premise.predicate)

        for known_clause in known_clauses:
            if known_clause.is_fact() and first_premise.is_ground():
                if known_clause.conclusion.terms == first_premise.terms:
                    found = True
                    break
            # Known clause is a rule, we now replace first premise with premises
            # of known clause.
            else:
                # Change variables if necessary to avoid collision of variable names
                if not known_clause.is_fact() and not first_premise.is_ground():
                    new_var = get_new_var(query)
                    substituted_query = query.substitute(new_var)
                else:
                    substituted_query = query

                var_dict = unify(known_clause.conclusion, substituted_query.premises[0])
                # Constructs new query clause with variables substituted and ask that clause.
                if var_dict:
                    substituted_query = substituted_query.substitute(var_dict)
                    new_premises = known_clause.substitute(var_dict).premises
                    new_premises.extend(substituted_query.premises[1:])
                    new_query = HornClause(None, new_premises)
                    flag, solution = True, []
                    if new_query.is_query():
                        flag, solution = self.__ask_recursive(new_query, find_all)
                    if flag:
                        found = True
                        solutions.extend(combine_solutions(solution, var_dict))
                        if not find_all:
                            break
        if first_premise.negation:
            found = not found
        if found and first_premise.is_ground() and not remain_query.is_nothing():
            found, solutions = self.__ask_recursive(remain_query, find_all)
        return found, solutions

    def ask(self, clause: HornClause):
        found = False
        solutions = []
        var = clause.get_variables()
        if var:
            find_all = True
        else:
            find_all = False
        # Change variables name to get solution according to those variables
        subs_dict = {v: v + '?' for v in var}
        clause = clause.substitute(subs_dict)
        found, solutions = self.__ask_recursive(clause, find_all=find_all)
        if found:
            # Change back variables name
            solutions = change_solution_var(solutions, subs_dict)
        return found, solutions

    def make_argument(self, conclusion: Atom):
        """
        Constructs an argument that leads to conclusion.

        :param conclusion: Atom - conclusion
        :return: str - string that describes argument
        """
        if not (conclusion.is_ground()):
            raise ValueError('Invalid conclusion')
        else:
            query_conclusion_str = ':-' + str(conclusion) + '.'
            if self.ask(HornClause.from_str(query_conclusion_str))[0]:
                s = ''
                known_clauses = self.get_clauses(conclusion.predicate)
                for known_clause in known_clauses:
                    subs_dict = unify(known_clause.conclusion, conclusion)
                    if subs_dict:
                        substituted_clause = known_clause.substitute(subs_dict)
                        query = HornClause(None, substituted_clause.premises)
                        found, solutions = self.ask(query)
                        if found:
                            if solutions:
                                substituted_query = query.substitute(solutions[0])
                            else:
                                substituted_query = query
                            for p in substituted_query.premises:
                                s += str(p) + '.\n'
                            s += str(known_clause) + '\n'
                            s += '\u2234 ' + str(conclusion)
                            break
            else:
                s = 'Argument does not exist.'
        return s


def get_new_var(query):
    new_var_dict = dict()
    for atom in query.premises:
        for term in atom.terms:
            if not is_query_variable(term) and is_variable(term):
                if term not in new_var_dict:
                    new_var_dict[term] = term + term[0]
    return new_var_dict


def change_solution_var(solutions, subs_dict):
    new_solutions = []
    for answer in solutions:
        d = dict()
        for key in subs_dict:
            d[key] = answer[subs_dict[key]]
        new_solutions.append(d)
    return new_solutions


def combine_solutions(sol, sub_dict):
    res_dict = {key: sub_dict[key] for key in sub_dict if is_query_variable(key)}
    solutions = []
    if res_dict:
        if sol:
            for i in range(len(sol)):
                sol[i].update(res_dict)
                solutions.append(sol[i])
        else:
            solutions.append(res_dict)
    else:
        if sol:
            solutions.extend(sol)
    return solutions


def to_str(solutions):
    s = ''
    if not solutions[1]:
        s = str(solutions[0])
    else:
        for solution in solutions[1]:
            if type(solution) == dict:
                first = True
                for key in solution:
                    if not first:
                        s += ', '
                    first = False
                    s += str(key) + ' = ' + str(solution[key])
            elif type(solution) == Atom:
                s += str(solution)
            s += '\n'
        s = s.strip('\n')
    return s


def create_kb(filename):
    clauses = get_clauses_from_file(filename)
    kb = KnowledgeBase(clauses)
    return kb
