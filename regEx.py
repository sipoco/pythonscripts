#! /usr/bin/env python3

import re
phonReg = re.compile(r'(\d{3})-(\d{4})')
var1 = 'My num is 444-5555.'
mo = phonReg.search(var1)
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.groups())
netNummer, hoofdNummer = mo.groups()
print(netNummer)
print(hoofdNummer)