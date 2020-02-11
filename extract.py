import re

with open('from.txt') as f:
    raw_result = f.readlines()
    global result
    result = ''.join(raw_result[0])

after_extract = re.findall(r'\b[A-z]+\b', result)

def case_sort(liststring):
  return sorted(liststring, key=str.lower)

answer = case_sort(after_extract)

with open('to.txt', 'w', encoding='gbk') as f:
    for l in answer:
        f.write(l + '\n')