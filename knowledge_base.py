import re
from atom import Atom
from atom import is_variable, is_question_variable, unify
from formula import Formula


class KnowledgeBase:
    formulas: list
    # Dictionary of predicates, contains first index and count
    pred_dict: dict

    def __init__(self):
        self.formulas = []
        self.pred_dict = dict()

    def __getitem__(self, key):
        return self.formulas[key]

    def tell(self, formula):
        key = formula.conclusion.predicate
        if key in self.pred_dict:
            self.pred_dict[key].append(len(self.formulas))
        else:
            self.pred_dict[key] = [len(self.formulas)]
        self.formulas.append(formula)

    def tell_formulas(self, formulas):
        for formula in formulas:
            self.tell(formula)

    def __ask_questions(self, questions):
        # Initialise
        answers = []
        rules = []
        found = False

        if questions[0].predicate == 'equal':
            questions.append(questions.pop(0))
        first_question = questions[0]
        remain_questions = questions[1:]

        if first_question.predicate == 'equal':
            if is_all_equal(first_question.terms):
                found = True
        if first_question.predicate in self.pred_dict:
            # Get all the rules that have same the predicate as the first question
            rule_indexes = self.pred_dict[first_question.predicate]
            rules = [self.formulas[i] for i in rule_indexes]
        for rule in rules:
            if rule.is_fact() and first_question.is_ground():
                if rule.conclusion.terms == first_question.terms:
                    found = True
                    break
            else:
                new_var = {}
                if not rule.is_fact() and not first_question.is_ground():
                    new_var = get_new_var(questions)
                sub_questions = substitute(questions, new_var)
                sub_dict = unify(rule.conclusion, sub_questions[0])
                sub_questions = substitute(sub_questions, sub_dict)
                if sub_dict:
                    new_questions = rule.substitute(sub_dict).premises
                    new_questions.extend(sub_questions[1:])
                    flag, answer = True, []
                    if new_questions:
                        flag, answer = self.__ask_questions(new_questions)
                    if flag:
                        found = True
                        answers.extend(combine_answers(answer, sub_dict))
        if first_question.negation:
            found = not found
        if found and remain_questions and first_question.is_ground():
            found, answers = self.__ask_questions(remain_questions)
        return found, answers

    def ask(self, formula):
        questions = formula.premises
        subs = get_question_var(questions)
        questions = substitute(questions, subs)
        flag, answers = self.__ask_questions(questions)
        if is_ground_questions(questions):
            return flag
        else:
            new_answers = change_answer_var(answers, subs)
            return new_answers


def is_all_equal(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] != l[j]:
                return False
    return True


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
    if subs_dict:
        for question in questions:
            new_quests.append(question.substitute(subs_dict))
    else:
        new_quests = questions
    return new_quests
