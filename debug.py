from horn_clause import HornClause, get_clauses_from_file
from knowledge_base import KnowledgeBase, create_kb, to_str

kb = create_kb('knowledge.pl')
print(to_str(kb.ask(HornClause.from_str(':- greater(X, khoa).'))))