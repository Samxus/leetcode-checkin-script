from time_utils import get_CST_current
from datetime import datetime, timedelta
import time

a = datetime.now()
b = timedelta(days=1)

print((a - b).day)
