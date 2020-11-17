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
        Find all clauses that have same the predicate as p.

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

    def __ask_recursive(self, goal_query, find_all=False):
        """
        Recursively querying a clause.\n
        Idea: A clause with n premises is satisfied if the first premise of clause
        is in knowledge-base and a clause contains n - 1 premises (not included first one)
        is satisfied.

        :param goal_query:
        :param find_all: goal or query
        :return: tuple - found is True if found a solution, solutions is a list of satisfied variables
        """
        # Initialise
        solutions = []
        known_clauses = []
        found = False

        # Put all comparison premises to the back of premise list.
        # Because comparison only works when all variables are
        # instantiated.
        for i in range(len(goal_query.premises)):
            if goal_query.premises[i].is_cmp_atom():
                goal_query.premises.append(goal_query.premises.pop(0))
            else:
                break

        first_premise = goal_query.premises[0]
        remain_goal_query = HornClause(None, goal_query.premises[1:])

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
                    new_var = get_new_var(goal_query)
                    substituted_goal_query = goal_query.substitute(new_var)
                else:
                    substituted_goal_query = goal_query

                sub_dict = unify(known_clause.conclusion, substituted_goal_query.premises[0])
                substituted_goal_query = substituted_goal_query.substitute(sub_dict)
                # Constructs new goal_query clause with variables substituted and ask that clause.
                if sub_dict:
                    new_premises = known_clause.substitute(sub_dict).premises
                    new_premises.extend(substituted_goal_query.premises[1:])
                    new_goal_query = HornClause(None, new_premises)
                    flag, solution = True, []
                    if new_goal_query.is_query() or new_goal_query.is_goal():
                        flag, solution = self.__ask_recursive(new_goal_query, find_all)
                    if flag:
                        found = True
                        solutions.extend(combine_solutions(solution, sub_dict))
                        if not find_all:
                            break
        if first_premise.negation:
            found = not found
        if found and first_premise.is_ground() and not remain_goal_query.is_nothing():
            found, solutions = self.__ask_recursive(remain_goal_query, find_all)
        return found, solutions

    def ask(self, clause: HornClause, find_all=False):
        found = False
        solutions = []
        if clause.is_goal():
            found, solutions = self.__ask_recursive(clause)
        elif clause.is_query():
            var = clause.get_variables()
            # Change variables name to get solution according to those variables
            subs_dict = {v: v + '?' for v in var}
            clause = clause.substitute(subs_dict)
            found, solutions = self.__ask_recursive(clause, find_all=find_all)
            if found:
                # Change back variables name
                solutions = change_solution_var(solutions, subs_dict)
        return found, solutions

    def make_argument(self, clause: HornClause):
        s = ''
        if not (clause.is_goal() and len(clause.premises) == 1):
            raise ValueError('Invalid conclusion')
        else:
            if self.ask(clause)[0]:
                premise = clause.premises[0]
                known_clauses = self.get_clauses(premise.predicate)
                for known_clause in known_clauses:
                    subs_dict = unify(known_clause.conclusion, premise)
                    if subs_dict:
                        x = known_clause.substitute(subs_dict)
                        query = HornClause(None, x.premises)
                        found, solutions = self.ask(query)
                        if found:
                            if solutions:
                                substituted_query = query.substitute(solutions[0])
                            else:
                                substituted_query = query
                            for p in substituted_query.premises:
                                s += str(p) + '.\n'
                            s += str(known_clause) + '\n'
                            s += '\u2234 ' + str(premise)
                            break
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
