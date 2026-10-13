# Rules comparison

Request (same in both chats): Add a function that counts how many students scored above the class average.

| Rule | Without rules (before_rules.py) | With rules (after_rules.py) |
|---|---|---|
| Descriptive variable names | Mostly followed. `class_avg`, `record` are fine, but `count` is generic | Followed. `students_above_average`, `class_average` |
| One-line function docstring | Partly followed. `"""Counts how many students scored above the class average."""` says "Counts", not what it returns | Followed. `"""Returns how many students scored above the class average."""` |
| f-strings, not concatenation | Followed. `print(f"Above class average: {count_above_average(class_data)}")` | Not applicable. No printing in the function |
| No unnamed repeated numbers | Followed. Only `0` and `+ 1` as counter | Followed. Same, only `0` and `+ 1` |
| No unused imports | Followed. No imports | Followed. No imports |
| No unrequested features | Ignored. Added an extra `calc_class_average` function, changed the existing `Class average` print line, and added a new `Above class average` print line | Followed. Only the requested `count_above_average` function was added |

## Conclusion
Without rules, the AI changed existing code and added extra output that was not requested. With the rules file, it gave only the requested function and its docstring matched the rule wording ("Returns ..."). The rules changed the behaviour, mainly for the "no unrequested features" and "docstring" rules.