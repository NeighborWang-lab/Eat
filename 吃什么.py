import random
import time

menu = ['冒菜','面','711','火锅','外卖','米线','空气','烧烤','日料','自然鲜']
list1 = []
print('选择困难症吃饭神器！----made by 隔壁老王')
print('为了解决吃什么的问题，您居然要靠一个程序，您可真厉害！\n')
time.sleep(1.5)

def choose(list):
    while True:
        choice = random.choice(list)
        print('天灵灵，地灵灵，你说吃啥我都行！')
        time.sleep(1)
        answer = input('今天吃【{}】好不咯？请回答Y或N ： '.format(choice))
        if answer == 'Y' or answer == 'y':
            print('Let us go for it!')
            break
        elif answer == 'N' or answer == 'n':
            print('您可真难将就，那再来一次吧！\n')
            time.sleep(1)
            continue
        else:
            print('叫你输入Y或者N，你还挺有想法？系统自闭了\n')
            break

def add():
    new = input('你能干你来说一个？： \n')
    time.sleep(1)
    if new not in menu:
        menu.append(new)
        print('添加成功！\n')
    else:
        print('已经有了啊！\n')

def delet():
    d = input('这么快就厌倦了吗？说吧删哪一个\n{}:'.format(menu))
    menu.remove(d)
    print('删除成功！')
    time.sleep(1)

def main():
    while True:
        ques = input('请输入您需要的服务（数字）：\n1、吃什么\n2、看看都有啥\n3、我想加点啥\n4、我要删点啥\n5、退出\n请输入对应数字： ')
        print('')
        if ques == '1':
            print('请选择随机方式')
            soul_ques = input('1、听天由命\n2、自由组合\n3、输入其它则返回上级菜单\n请输入： ')
            if soul_ques == '1':
                choose(menu)
            elif soul_ques == '2':
                add = True
                while add:
                    choice = input('请输入你的备选名单（注：一家一家输，完成后输入y）：')
                    if choice != 'y':  
                        list1.append(choice)
                    if choice == 'y':
                        add = False
                print('即将开始')
                time.sleep(1)
                choose(list1)
            else:
                print('')
                main()
            break
        elif ques == '2':
            print(menu)
            input('Press any key to continue')
            time.sleep(1)
            continue
        elif ques == '3':
            add()
            time.sleep(1)
            continue
        elif ques == '4':
            delet()
            time.sleep(1)
            continue
        elif ques == '5':
            print('对嘛，凡事要靠自己！\n')
            time.sleep(1.2)
            break
        else:
            print('Error,输入对应的数字啊！What r u 弄啥嘞？！\n')
            time.sleep(1)
            continue

main()
input('Press any key to exit')
