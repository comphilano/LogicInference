class Atom:
    predicate: str
    terms: list

    def __init__(self, atom_str: str):
        open_prts_index = atom_str.find('(')
        close_prts_index = atom_str.find(')')
        if open_prts_index != -1 and close_prts_index != -1:
            self.predicate = atom_str[:open_prts_index].strip()
            terms_str = atom_str[open_prts_index + 1:close_prts_index].split(',')
            self.terms = [x.strip() for x in terms_str]

    def __str__(self):
        return self.predicate + '(' + ', '.join(self.terms) + ')'
