?- parent(Who, "Prince Harry").
?- son(X, "Queen Elizabeth II").
?- son(X, Y).
?- child(X, Y).
?- sibling("Prince Charles", "Princess Anne").
?- niece("Zara Phillips", "Prince Charles").
?- uncle(X, "Prince Harry").
?- uncle(X, "Prince Harry"), grandparent("Queen Elizabeth II", Z).
?- grandparent("Queen Elizabeth II", Z), uncle(X?, "Prince Harry").
?- married(X, "Prince Phillips").
?- married("Princess Anne", "Timothy Laurence").
?- \+ married("Princess Anne", "Timothy Laurence").