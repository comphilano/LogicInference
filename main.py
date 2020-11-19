import sys
from atom import Atom
from horn_clause import HornClause, get_clauses_from_file
from knowledge_base import KnowledgeBase, create_kb, to_str

if __name__ == "__main__":
    if len(sys.argv) == 4:
        kb = create_kb(sys.argv[1])
        queries = get_clauses_from_file(sys.argv[2])
        with open(sys.argv[3], 'w') as out_file:
            for query in queries:
                out_file.write(str(query) + '\n')
                out_file.write(to_str(kb.ask(query)) + '\n\n')
    # Demo
    else:
        # All men are mortal.
        # Socrates is a man.
        premises = ['mortal(X) :- man(X).', 'man("Socrates").']

        # Is Socrates mortal?
        query = ':- mortal("Socrates").'

        premise_clauses = [HornClause.from_str(x) for x in premises]
        kb = KnowledgeBase(premise_clauses)
        query_clause = HornClause.from_str(query)

        # Yes, he is.
        response = kb.ask(query_clause)[0]
        assert response

        # This is how it works
        conclusion = 'mortal("Socrates")'
        argument = kb.make_argument(Atom.from_str(conclusion))
        print(argument)
