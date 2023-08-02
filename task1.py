import re

x = "we are looking for adana@gmail.com becouse we want to set up roewq@icloud.com and this raw for ensure qqq@mail.ru"

y = re.findall(r'\w*@[a-z]*', x)
print(y)


