import re

strg = "this is a test 123"

match = re.search(".+ \d", strg)
print(match.group())
