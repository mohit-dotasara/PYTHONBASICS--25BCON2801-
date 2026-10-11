# README Audit

| Claim made in README (AI draft) | True? | Evidence or correction made |
|---|---|---|
| Project structure lists 4 files in repo root | No | factorial.py is inside the folder "prompt assignment 1", not in the root. README now uses the correct path |
| Requires Python 3.8 or higher | No | Code only needs f-strings (3.6+). Changed to 3.6+ |
| git clone https://github.com/<your-username>/... | No | Placeholder username, not a real URL. Section removed, replaced with run instructions |
| No external packages, standard library only | Yes | Only `import math` in factorial.py, no imports in fibonacci.py and student_dict.py |
| factorial prompt is "Enter a number: " | No | Code says "Enter a non-negative number: ". Corrected |
| Output labels "Factorial using loop: 120" etc. | No | Code prints "Loop           :", "Recursion      :", "math.factorial :". Corrected |
| fibonacci prints 0 1 1 2 3 5 8 13 21 34 | Yes | Ran fibonacci.py, output matches (code prints a trailing space) |
| student_dict prints Name: Rahul, Marks: 85 | No | Code uses Mohit, 101, 87.5 with :.1f. Output corrected |
| Licensed under MIT | No | No LICENSE file in repo. License section deleted |

## Commit comparison

| Commit | My message | AI message | Which is clearer, why? |
|---|---|---|---|
| 1 | feat: add fibonacci program | | |
| 2 | feat: add student dict program | | |
| 3 | docs: add comments and call main() | | |

## Peer review notes

(partner ka review yahan likh)
