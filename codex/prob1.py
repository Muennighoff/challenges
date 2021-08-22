"""
Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry.
"""

### ME, 0 ASSISTS ###

from datetime import date

import pandas as pd

from io import StringIO


def diff_days(csv_contents: str) -> int:
    idx = csv_contents.split("\n")[0].split(",").index("Date")
    dates = [x.split(",")[idx] for x in csv_contents.split("\n")[1:-1]]

    dates = [date(int(d.split('-')[0]), int(d.split('-')[1]), int(d.split('-')[2])) for d in dates if "-" in d]

    if len(dates) == 0:
        return 0

    diff = max(dates) - min(dates)
    #print(diff.days)
    return diff.days

# Examples
print(diff_days("Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"))
print(diff_days('Date\n2000-01-01\n2000-01-01\n'))

# The last expression evaluated is always shown when
# you run your code, just like a Jupyter notebook cell.
"Good luck!"


### CODEX ###

from datetime import date

import pandas


def diff_days(csv_contents: str) -> int:
    """
    Codex attempt #8
    """
    df = pandas.read_csv(io.StringIO(csv_contents))
    min_date = date.fromisoformat(df['Date'].min())
    max_date = date.fromisoformat(df['Date'].max())
    return (max_date - min_date).days