5.4 #if-then-else语句
age = 11
if age == 12:
    print("A pig fell in the mud !")
else:
    print("shh .It's a secret.")
5.5 #if和elif语句
age =15
if age ==10:
    print("what do you call an unhappy cranberry?")
    print("A blueberry!")
elif age == 11:
    print("what did the green grape say to the blue grape?")
    print("Breathe! Breathe!")
elif age == 12:
    print("why wasn't 10 afraid of 7 ?")
    print("Because rather than eating 9,7 8 pi.")
else:
    print("Huch?")
#
age="10"
converted_age=int(age)
if age == 10:
    print("what's the best way to a monster? ")
    print("From as far away as possible!")
#6.1关于for循环
#不添加数字的方法 range的意思是列表
for x in range(0,2):
    print('hello')
#添加数字的方法
for x in range(2,4):
    print('dog %s'% x)
#也可以不用range和list
wizard_list=['1',' 2','3',]
for i in wizard_list:
    print(i)
    for j in wizard_list:
        print(j)
#用一个for循环计算金币数量
found_coins = 20   #发现的金币
magic_coins = 70   #每天增加的十个金币，每增加周七十个金币
stolen_coins = 3   #每周偷去三枚金币
coins=found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print('week %s = %s' % (week,coins)) #prthon用占位符，打印出周数和到此为止的金币数

#7.1.2变量名和作用域 使用函数 def是define缩写
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
print(variable_test())

#
import sys
def silly_joke():
    print('How old are you ?')
    age=int(sys.stdin.readline())
    if age >=10 and age <=13:
        print('what is 13')
    else:
        print('huh')
#


