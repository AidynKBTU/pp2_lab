import re

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"ab{2,3}"
    result = re.findall(pattern, text)
    print(result)