import random
import time

guesstime = int(input('你想一局猜几次？'))
round_game =0
scores =[]  #定义/清空列表scores


while(True):    #开始一轮游戏
    round_game +=1
    number =random.randint(1,10)
    result_game =False 
    time_begin =time.time()  #开始时时间
    for i in range(guesstime):  #循环：输入数字并对比
        guess = int(input('请输入10以内整数：'))    #生成随机数

        if(guess >=11 or guess <= -1):  #判断是否正确/错误
            print('犯规！')
            break
        if(guess == number):
            result_game =True
            break
        elif(guess < number):
            print('太小了！')
        else:
            print('太大了！')

        if(i < guesstime-1):    #判断是否继续猜测
            print('请继续猜：')
        else:
            print(f'次数达到{guesstime}次了！')

    if(result_game):    #游戏结果
        print('你成功了！')
    else:
        print('你失败了，抱歉！')

    time_end =time.time()  #结束时时间
    time_used =time_end - time_begin    #统计游戏时长
    time_used = round(time_used,2)  #精确到两位小数
    print(f'共用时{time_used}秒。')

    scores.append((round_game,result_game,time_used))   #在列表scores末尾加入新一局的游戏数据
    print(scores)

    cont_game=input('\n若继续游戏，请输入yes；\n若想修改猜测次数，请输入reset；\n否则请键入任意内容以退出游戏：')
    if(cont_game !='yes' and cont_game != 'reset'):
       print('886')
       break
    elif(cont_game =='reset'):
        guesstime =int(input('请输入新的猜测次数：'))