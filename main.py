from hornclause import HornClause
from knowledge_base import create_kb, print_solutions


filename = input('Input knowledge-base file: ')
kb = create_kb(filename)
while True:
    clause_str = ':-' + input('?- ')
    clause = HornClause.from_str(clause_str)
    print_solutions(kb.ask(clause))