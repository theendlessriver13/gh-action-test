# unordered imports
import datetime
import time

import psycopg2
"""
this is a docstring which does not come first
"""

# mypy error
a: int = 'abc'
# this line is very long so flake8 has to complain about this, so I can see that this works properly

# trailing whitespace
# no newline at the end of the file
b = 'double quotes'

# no trailng commas
c = (
    'a',
    'b',
)
