# lisp-parser

Basic Lisp parser which uses recursion to create the abstract syntax tree
which would then require some implementation to perform the functions

The function will return a nested list representing the lisp code
So the following input:  `(first (list (+ 1 3) (+ 2 3) 9 10))`
will yield: `['first', ['list', ['+', '1', '3'], ['+', '2', '3'], '9', '10']]`

#### Usage:
```
python lisp.py
```

You can modify the line `code = "(first (list (+ 1 3) (+ 2 3) 9 10))"`
to alter the code being run.
