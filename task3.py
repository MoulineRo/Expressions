import re

email = 'apple orange london@gmail.org table'
pattern = r'\w*@[a-z]*.\D\D\D'

match = re.split("@", re.search(pattern, email).group())
print(match[0])
print(match[1])
