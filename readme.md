# Notes
In order for program to work correctly, these conditions about input data are required:
- Comments should be ended with a period.
- In rules, premises should be conjunctive. In other words, rules are written in implication form of Horn clause:
`u ← p ∧ q ∧ ... ∧ t`.
- Queries should contain `?-` or `:-` at the beginning.
# Run code
Run from command line:  
`python main.py knowledge_file queries_file output_file`

