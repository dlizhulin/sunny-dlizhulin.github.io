uname = "lizhulin"
upass = "123456"
count = 0;
for i in range(1,4):
    sname = input("请输入用户名：")
    spass = input("请输入密码：")
    if(sname == uname and spass == upass):
        print("登录成功！")
        break
    else:
        print('用户名或密码错！')
        count+= 1
if(count == 3):
    print("错误超过3次,不允许登录！")
    exit(0)