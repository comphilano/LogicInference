parent("Queen Elizabeth II", "Prince Charles").
parent("Queen Elizabeth II", "Princess Anne").
parent("Queen Elizabeth II", "Prince Andrew").
parent("Queen Elizabeth II", "Prince Edward").
parent("Princess Anne", "Zara Phillips").
parent("Prince Charles", "Prince Harry").
parent("Prince Phillips", "Prince Charles").
male("Prince Charles").
male("Prince Harry").
male("Timothy Laurence").
male("Prince Phillips").
male("Prince Andrew").
male("Prince Edward").
female("Queen Elizabeth II").
female("Princess Anne").
female("Zara Phillips").
marriedTo("Timothy Laurence", "Princess Anne").
marriedTo("Queen Elizabeth II", "Prince Phillips").
married(X, Y) :- marriedTo(X, Y); marriedTo(Y, X).
child(X, Y) :- parent(Y, X).
husband(X, Y) :- married(X, Y), male(X).
son(X, Y) :- parent(Y, X), male(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y).
niece(X, Y) :-  parent(Z, X), sibling(Z, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
uncle(X, Y) :- husband(X, Z), sibling(Z, T), parent(T, Y).