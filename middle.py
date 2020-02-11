with open('F:/python-learning/report.txt', encoding='utf-8') as f:
    raw_results = f.readlines()
    global count
    count = len(raw_results)
    #print(count)
    results = ''.join(raw_results).splitlines()
    #print(results)

modified_1 = []

for result in results:
    modified_1.append(result.split(' '))

modified_2 = []

def process(List):
    scores = List[1:]
    name = List[0]
    num = 0
    for i in range(0,9):
        scores[i] = int(scores[i])
    for score in scores:
        num = num + score
    avg = round(num / 9, 1)
    scores.append(num)
    scores.append(avg)
    scores.insert(0, name)
    modified_2.append(scores)
    return modified_2

for i in range(1,31):
    process(modified_1[i])

newline = modified_1[0]
newline.append('总分')
newline.append('平均分')
newline.insert(0, '名次')

modified_2.sort(key=lambda x: x[-1], reverse=True)
for j in range(1, 31):
    modified_2[j-1].insert(0, str(j))

total_results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2,13):
    for mo in modified_2:
        total_results[i-2] = total_results[i-2] + mo[i]
#print(total_result)
avg_results = [round(total_result/count, 1) for total_result in total_results]
avg_results.insert(0, '平均')
avg_results.insert(0, '0')

for i in range(2,13):
    avg_results[i] = str(avg_results[i])
#print(avg_results)

modified_2.insert(0, avg_results)
modified_2.insert(0, newline)
modified_3 = modified_2[2:]

for i in range(2,13):
    for modi in modified_3:
        modi[i] = str(modi[i])
        if float(modi[i]) < 60:
            modi[i] = '不合格'

modified_3.insert(0, avg_results)
modified_3.insert(0, newline)

modified_4 = []
for modis in modified_3:
    modified_4.append(' '.join(modis))

#print(modified_4)
with open('result.txt', 'w', encoding='gbk') as f:
    for l in modified_4:
        f.write(l + '\n')







