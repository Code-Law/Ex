#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import date
from collections import Counter
counter = Counter()
for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1
print(counter[6])