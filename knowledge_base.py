import re
from formula import Formula
from atom import Atom
from atom import is_variable, is_question_variable


class KnowledgeBase:
    formulas: list
    # Dictionary of predicates, contains first index and count
    pred_dict: dict

    def __init__(self):
        self.formulas = []
        self.pred_dict = dict()

    def __getitem__(self, key):
        return self.formulas[key]

    def tell(self, formula_str: str):
        # Split an OR formula into Horn formulas
        arrow_index = formula_str.find(':-')
        or_formula_str = formula_str.replace(';', '.' + formula_str[:arrow_index + 2])
        or_formula_str = or_formula_str.split('.')
        for x in or_formula_str:
            formula = Formula.from_str(x)
            key = formula.conclusion.predicate
            # If predicate already in dictionary, increase count
            if key in self.pred_dict:
                self.pred_dict[key][1] += 1
            # Else insert first index to dictionary
            else:
                self.pred_dict[key] = [len(self.formulas), 1]
            self.formulas.append(formula)

    def __ask_questions(self, questions):
        # Initialise
        answers = []
        first_question = questions[0]
        remain_questions = questions[1:]
        rule_index = self.pred_dict[first_question.predicate]
        # Get all the rules that have same the predicate as the first question
        rules = self.formulas[rule_index[0]:rule_index[0] + rule_index[1]]
        found = False

        for rule in rules:
            if rule.is_fact():
                if first_question.is_ground():
                    # If rule is a fact and the question is ground, check if they are identical
                    if rule.conclusion.terms == first_question.terms:
                        if not remain_questions:
                            found = True
                            break
                        # If there are questions left, recursively ask them
                        else:
                            found, answers = self.__ask_questions(remain_questions)
                            break
                else:
                    # Find substitute values for question
                    sub_dict = first_question.unify(rule.conclusion)
                    if sub_dict:
                        new_questions = substitute(questions, sub_dict)
                        flag, answer = self.__ask_questions(new_questions)
                        if flag:
                            found = True
                            answers.extend(combine_answers(answer, sub_dict))
            else:
                if first_question.is_ground():
                    sub_questions = questions
                else:
                    # Change variables of question to avoid collision with rule variables
                    new_var = get_new_var(questions)
                    sub_questions = substitute(questions, new_var)
                # Find substitute variables or values for rule
                sub_dict = rule.conclusion.unify(sub_questions[0])
                if sub_dict:
                    new_rule = rule.substitute(sub_dict)
                    new_questions = []
                    new_questions.extend(new_rule.premises)
                    new_questions.extend(sub_questions[1:])
                    flag, answer = self.__ask_questions(new_questions)
                    if flag:
                        found = True
                        answers.extend(combine_answers(answer, sub_dict))
        if first_question.negation:
            found = not found
        return found, answers

    def ask(self, question_str: str):
        questions = get_questions(question_str)
        subs = get_question_var(questions)
        questions = substitute(questions, subs)
        flag, answers = self.__ask_questions(questions)
        if is_ground_questions(questions):
            return flag
        else:
            new_answers = change_answer_var(answers, subs)
            return new_answers


def is_ground_questions(questions):
    for question in questions:
        if not question.is_ground():
            return False
    return True


def get_questions(question_str: str):
    quests_str = re.findall(r'(?:\\\+)?[\w\s]+\([^)]+\)', question_str)
    questions = []
    for q in quests_str:
        questions.append(Atom.from_str(q))
    return questions


def get_question_var(questions):
    new_var_dict = dict()
    for question in questions:
        for term in question.terms:
            if is_variable(term):
                if term not in new_var_dict:
                    new_var_dict[term] = term + '?'
    return new_var_dict


def get_new_var(questions):
    new_var_dict = dict()
    for question in questions:
        for term in question.terms:
            if not is_question_variable(term) and is_variable(term):
                if term not in new_var_dict:
                    new_var_dict[term] = term + '$'
    return new_var_dict


def change_answer_var(answers, subs_dict):
    new_answer = []
    for answer in answers:
        d = dict()
        for key in subs_dict:
            d[key] = answer[subs_dict[key]]
        new_answer.append(d)
    return new_answer


def combine_answers(ans, sub_dict):
    res_dict = {key: sub_dict[key] for key in sub_dict if is_question_variable(key)}
    answer = []
    if res_dict:
        if ans:
            for i in range(len(ans)):
                ans[i].update(res_dict)
                answer.append(ans[i])
        else:
            answer.append(res_dict)
    else:
        if ans:
            answer.extend(ans)
    return answer


def substitute(questions, subs_dict):
    new_quests = []
    for question in questions:
        new_quests.append(question.substitute(subs_dict))
    return new_quests
