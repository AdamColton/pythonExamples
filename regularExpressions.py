import re

x = re.compile(".+ing")
if x.match("testing") : print("Ends in -ing")
if not x.match("foobar") : print("Does not end in -ing")