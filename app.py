# demo_three.py
import sqlite3, subprocess, builtins

# BUG-1  eval() – pattern match, no taint needed
builtins.eval("print('hello')")        # unsafe eval (caught)

# BUG-2  straight-pattern SQL (no taint)
sqlite3.connect(":memory:")\
        .execute("SELECT * FROM users WHERE name = 'Alice' -- '")   # SQL-i (caught)

# BUG-3  subprocess shell=True – pattern match
subprocess.check_output("ls -la", shell=True)   # cmd-inj (caught)

