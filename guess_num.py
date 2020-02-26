import requests

def guess_num(a, b, c):
    global result
    try:
        response = requests.get("https://python666.cn/cls/number/guess/")
        answer = int(response.text)
    except:
        print("network error")
    times = 0
    bingo = False
    while bingo == False:
        times += 1
        try:
            guess = int(input("请猜一个 1 - 100 的数字："))
            if guess < answer:
                print("猜小了，再试试")
            if guess > answer:
                print("猜大了，再试试")
            if guess == answer:
                bingo = True
                print("猜对了，你一共猜了" + str(times) + "次")
                if times < b or a == 0:
                    b = times
                totaltime = a * c
                a += 1
                c = round((totaltime + times) / a, 2)
                print(user + '，' + '你已经玩了' + str(a) + '次，最少' + str(b) + '轮猜出答案，' + '平均' + str(c) + '轮猜出答案')
                choice = input("是否继续游戏？（输入y继续，其他退出）")
                if choice == 'y':
                    guess_num(a, b, c)
                else:
                    result = [str(a), str(b), str(c)]
                    print("退出游戏，欢迎下次再来！")
        except:
            print("输入异常")

    return result

user = input("请输入你的名字：")

users_name = []
users_count = []
users_least_count = []
users_avg_count = []

with open('game_many_user.txt') as f:
    user_infos = f.read().splitlines()
    print(user_infos)
    for user_info in user_infos:
        users_name.append(user_info.split(' ')[0])
        users_count.append(user_info.split(' ')[1])
        users_least_count.append(user_info.split(' ')[2])
        users_avg_count.append(user_info.split(' ')[3])

if user in users_name:
    index = users_name.index(user)
    count = int(users_count[index])
    least_count = int(users_least_count[index])
    avg_count = float(users_avg_count[index])
    print(user+'，'+'你已经玩了'+str(count)+'次，最少'+str(least_count)+'轮猜出答案，'+'平均'+str(avg_count)+'轮猜出答案，开始游戏！')
    game_result = guess_num(count, least_count, avg_count)
    game_result.insert(0, user)
    new_line = ' '.join(game_result)
    del user_infos[index]
    user_infos.insert(index, new_line)
    #print(user_infos)
    with open('game_many_user.txt', 'w', encoding='gbk') as f:
        for user_info in user_infos:
            f.write(user_info+'\n')

else:
    count = 0
    least_count = 0
    avg_count = 0.00
    print(user+'，'+'你已经玩了'+str(count)+'次，最少'+str(least_count)+'轮猜出答案，'+'平均'+str(avg_count)+'轮猜出答案，开始游戏！')
    game_result = guess_num(count, least_count, avg_count)
    game_result.insert(0, user)
    new_line = ' '.join(game_result)
    #print(new_line)
    user_infos.append(new_line)
    with open('game_many_user.txt', 'w', encoding='gbk') as f:
        for user_info in user_infos:
            f.write(user_info+'\n')
























