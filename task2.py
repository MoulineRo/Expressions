import re

y1 = '12-12-2022'

res = re.sub(r"[-\\.]", "/", re.search(r"(\d+.*?\d+.*?\d+)", y1).group())

print(res)