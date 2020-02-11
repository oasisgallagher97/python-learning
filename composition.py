import re

def wordcount(text):
    with open(text) as f:
        result = f.read()

    rule = re.compile(r"\b[A-z]+[']{0,1}[A-z]\b")
    answer = rule.findall(result)
    return len(answer)

filename = input("请输入文件名：")
number = wordcount(filename)
print("该文件单词数为：%s" % str(number))