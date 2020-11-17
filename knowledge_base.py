from atom import is_variable, is_query_variable, unify
from hornclause import HornClause, get_clauses_from_file


class KnowledgeBase:
    """
    A knowledge-base contains facts, rules and can be queries.
    """
    clauses: list
    # Dictionary of predicates, contains first index and count
    pred_dict: dict

    def __init__(self):
        self.clauses = []
        self.pred_dict = dict()

    def __getitem__(self, key):
        return self.clauses[key]

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

    def __ask_recursive(self, clause, clause_type):
        """
        Recursively querying a clause.\n
        Idea: A clause with n premises is satisfied if the first premise of clause
        is in knowledge-base and a clause contains n - 1 premises (not included first one)
        is satisfied.

        :param clause:
        :param clause_type: goal or query
        :return: tuple - found is True if found a solution, solutions is a list of satisfied variables
        """
        # Initialise
        solutions = []
        known_clauses = []
        found = False

        # Put all comparison premises to the back of premise list.
        # Because comparison only works when all variables are
        # instantiated.
        for i in range(len(clause.premises)):
            if clause.premises[i].is_cmp_atom():
                clause.premises.append(clause.premises.pop(0))
            else:
                break

        first_premise = clause.premises[0]
        remain_goal_query = HornClause(None, clause.premises[1:])

        # Evaluate comparison premise.
        if first_premise.is_cmp_atom():
            try:
                found = first_premise.eval_cmp()
            except TypeError:
                found = False

        # Find all the known clauses that have same the predicate as the first premise.
        if first_premise.predicate in self.pred_dict:
            known_clause_indexes = self.pred_dict[first_premise.predicate]
            known_clauses = [self.clauses[i] for i in known_clause_indexes]

        for known_clause in known_clauses:
            if known_clause.is_fact() and first_premise.is_ground():
                if known_clause.conclusion.terms == first_premise.terms:
                    found = True
                    break
            # Known clause is a rule, we now replace first premise with premises
            # of known clause.
            else:
                new_var = {}
                # Change variables if necessary to avoid collision of variable names
                if not known_clause.is_fact() and not first_premise.is_ground():
                    new_var = get_new_var(clause)
                substituted_query = clause.substitute(new_var)

                sub_dict = unify(known_clause.conclusion, substituted_query.premises[0])
                substituted_query = substituted_query.substitute(sub_dict)
                # Constructs new clause with variables substituted and ask that clause.
                if sub_dict:
                    new_premises = known_clause.substitute(sub_dict).premises
                    new_premises.extend(substituted_query.premises[1:])
                    new_goal_query = HornClause(None, new_premises)
                    flag, answer = True, []
                    if new_goal_query.is_query() or new_goal_query.is_goal():
                        flag, answer = self.__ask_recursive(new_goal_query, type)
                    if flag:
                        found = True
                        solutions.extend(combine_solutions(answer, sub_dict))
                        if clause_type == 'goal':
                            break
        if first_premise.negation:
            found = not found
        if found and first_premise.is_ground() and not remain_goal_query.is_nothing():
            found, solutions = self.__ask_recursive(remain_goal_query, type)
        return found, solutions

    def ask(self, clause: HornClause):
        if clause.is_goal():
            found, solutions = self.__ask_recursive(clause, 'goal')
            return found
        elif clause.is_query():
            var = clause.get_variables()
            # Change variables name to get solution according to those variables
            subs_dict = {v: v + '?' for v in var}
            clause = clause.substitute(subs_dict)
            found, solutions = self.__ask_recursive(clause, 'query')
            if found:
                # Change back variables name
                solutions = change_solution_var(solutions, subs_dict)
                return solutions
            else:
                return False


def get_new_var(query):
    new_var_dict = dict()
    for atom in query.premises:
        for term in atom.terms:
            if not is_query_variable(term) and is_variable(term):
                if term not in new_var_dict:
                    new_var_dict[term] = term + '$'
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


def str_solutions(solutions):
    if type(solutions) == bool:
        s = str(solutions) + '\n'
    else:
        s = ''
        for solution in solutions:
            first = True
            for key in solution:
                if not first:
                    s += ', '
                first = False
                s += str(key) + ' = ' + str(solution[key])
            s += '\n'
    return s


def create_kb(filename):
    formulas = get_clauses_from_file(filename)
    kb = KnowledgeBase()
    kb.tell_clauses(formulas)
    return kb
