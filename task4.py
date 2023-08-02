import re

number = '210985683498'

pattern = r'\d{12}'
try:
    x = re.search(pattern,number).group()
    y3 = re.match(r'380', str(x)).group()
    print(x)
except AttributeError:
    print("Ivalid format, should start from 380")