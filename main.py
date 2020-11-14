from knowledge_base import KnowledgeBase


def get_kb_from_file(filename):
    with open(filename, 'r') as kb_file:
        data = kb_file.read()
    data = data.replace('\n', '')
    kb_str = data.split('.')
    kb_str.pop()
    base = KnowledgeBase()
    for formula_str in kb_str:
        base.tell(formula_str)
    return base


def get_question_from_file(filename):
    with open(filename, 'r') as q_file:
        data = q_file.read()
    data = data.replace('\n', '')
    q_str = data.split('.')
    q_str.pop()
    quests = []
    for quest in q_str:
        quests.append(quest)
    return quests


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


kb = get_kb_from_file('kb.pl')
questions = get_question_from_file('question.pl')
for question in questions:
    print(question)
    print_answers(kb.ask(question))
    print()
# ans = kb.ask('?- \+ child(X, Y).')
# print_answers(ans)
