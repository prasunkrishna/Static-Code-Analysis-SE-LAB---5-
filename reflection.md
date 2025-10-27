Reflection
1. 
Easiest Issues: 
Unused Import (F401): Simply deleting the import logging line was the easiest.
Hardest Issues:
Dangerous Default Value (W0102): You can't just delete it, The fix required changing the default to None and then adding new logic (if logs is None: logs = []) inside the function, which is a conceptual fix, not just a syntax fix.

2. 
Yes, 
W0603: Using the global statement (global-statement)
Pylint flagged this in the loadData function. The use of global here is intentional and necessary for the script's simple design.

3.
Local Development: This is for catching issues before they're even saved.
IDE Integration: I would install extensions for Pylint, Flake8, and Bandit directly into my code editor (like VS Code). This gives me real-time feedback, underlining problems as I type, so I can fix them immediately.

4. 
The improvements were very clear and tangible:
•	Robustness (Fewer Bugs): Fixing the mutable default argument (logs=[])
•	Security: By removing the eval() function, we eliminated a critical security
•	Readability and Maintainability: Clarity - Removing the unused logging import cleans up the file
