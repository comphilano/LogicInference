import csv
from formula import Formula
from knowledge_base import KnowledgeBase


def read_file(filename):
    with open(filename, 'r') as kb_file:
        data = kb_file.read()
    data = data.replace('\n', '')
    kb_str = data.split('.')
    kb_str.pop()
    kb = KnowledgeBase()
    for formula_str in kb_str:
        kb.tell(Formula(formula_str))
    return kb


kb = read_file('test.pl')
kb.ask('?- child("Prince Charles", "Queen Elizabeth II").')


