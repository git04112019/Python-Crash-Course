# Modules

import datetime
from datetime import date
import time
from time import time

# Pip module
# Use pip to install modules
import camelcase
from camelcase import CamelCase
# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()
print(timestamp)
print(today)

c = CamelCase()
print(c.hump('hello there world'))
