import os

with os.popen('arp -a') as f:
    data = f.read()

import re
for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
    print(line)