from formula import Formula
from knowledge_base import KnowledgeBase


def get_formulas_from_file(filename):
    """
    Get formulas from file.\n
    Formulas are written in Prolog syntax and should not
    include any comparision operators like ==, \\\==, ...
    Those operators should be represent as

    :param filename:
    :return:
    """
    with open(filename, 'r') as kb_file:
        data = kb_file.read()
    data = data.replace('\n', '')
    for_str = data.split('.')
    for_str.pop()
    formulas = []
    for s in for_str:
        formulas.extend(Formula.parse(s))
    return formulas


def print_answers(answers):
    if type(answers) == bool:
        print(answers)
    else:
        for answer in answers:
            first = True
            for key in answer:
                if not first:
                    print(', ', end='')
                first = False
                print(key + ' = ' + answer[key], end='')
            print()


formulas = get_formulas_from_file('kb2.pl')
questions = get_formulas_from_file('question2.pl')
kb = KnowledgeBase()
kb.tell_formulas(formulas)

for question in questions:
    print(question)
    print_answers(kb.ask(question))
    print()
