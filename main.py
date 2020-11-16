from formula import get_formulas_from_file
from knowledge_base import KnowledgeBase, print_answers


formulas = get_formulas_from_file('kb2.pl')
questions = get_formulas_from_file('question2.pl')
kb = KnowledgeBase()
kb.tell_formulas(formulas)
for question in questions:
    print(question)
    print_answers(kb.ask(question))
    print()