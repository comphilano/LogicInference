import sys
from hornclause import get_clauses_from_file
from knowledge_base import create_kb, str_solutions


if __name__ == "__main__":
    kb = create_kb(sys.argv[1])
    queries = get_clauses_from_file(sys.argv[2])
    with open(sys.argv[3], 'w') as out_file:
        for query in queries:
            out_file.write(str(query) + '\n')
            out_file.write(str_solutions(kb.ask(query)) + '\n')