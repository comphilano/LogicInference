import re
from formula import Formula
from atom import Atom

class KnowledgeBase:
    formulas: list
    pred_dict: dict

    def __init__(self):
        self.formulas = []
        self.pred_dict = dict()

    def __getitem__(self, key):
        return self.formulas[key]

    def tell(self, formula: Formula):
        key = formula.conclusion.predicate
        if key in self.pred_dict:
            self.pred_dict[key].append(len(self.formulas))
        else:
            self.pred_dict[key] = len(self.formulas)
        self.formulas.append(formula)

    def ask(self, question_str: str):
        questions = get_question(question_str)
        for question in questions:
            if question.predicate not in self.pred_dict:
                return False
            else:
                rules_index = self.pred_dict[question.predicate]
                #for term in question.terms:



def is_variable(term: str):
    flag = False
    if term[0] == '_':
        flag = True
    elif term[0].isalpha() and term[0] == term[0].upper():
        flag = True
    return flag

def get_question(question_str: str):
        question_strs = re.findall(r'[\w\s]+\(+[^\)]+\)', question_str)
        questions = []
        for q in question_strs:
            questions.append(Atom(q))
        return questions