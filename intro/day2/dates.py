#DOCS: https://docs.python.org/3/library/datetime.html#module-datetime
#Format DOCS: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

from datetime import datetime, date, timedelta

print(date.today().strftime("%m/%d/%Y") )
print((datetime.now() - timedelta(hours=1)).strftime("%m/%d/%Y, %H:%M:%S %f"))