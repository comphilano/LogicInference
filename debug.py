from horn_clause import HornClause, get_clauses_from_file
from knowledge_base import KnowledgeBase, create_kb, to_str

kb = create_kb('Hoang_Gia_Anh.pl.txt')
question = get_clauses_from_file('Test.txt')
print(to_str(kb.ask(HornClause.from_str(':-wife(queen_elizabeth_ii, prince_phillip).'))))