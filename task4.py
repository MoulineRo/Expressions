import re

number = '210985683498'


def task4(number):
    pattern = r'\d{12}'
    x = re.search(pattern,number).group()
    y3 = re.match(r'380', str(x)).group()
    return x

