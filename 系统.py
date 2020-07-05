import time
import os


# 账号库
with open('账号管理.txt', 'a+', encoding='utf-8') as account_database:
    pass



# 登录成功界面
def gn(user):
    print("""欢迎进入系统，选择您需要的功能：
          1：查询余额
          2：充值
          3：转账
          4：提现
          5：修改密码
          0：退出""")

    input_cg = int(input('输入数字即可完成相应功能：'))
    if input_cg == 1:
        inquire_money(user)
    elif input_cg == 2:
        pay_money(user)
    elif input_cg == 3:
        transfer(user)
    elif input_cg == 4:
        withdraw(user)
    elif input_cg == 5:
        change_password(user)
    elif input_cg == 0:
        print('88，欢迎下次光临！')


# 充值
def pay_money(name):
    dic = {}
    with open('db.txt', 'r', encoding='utf-8') as f:
        for ret in f:
            use, money = ret.strip().split(':')
            dic[use] = int(money)

    # 检查当前传入用户是否存在
    if name not in dic:
        print('用户不存在，程序结束！')
        return

    while True:
        money = input('请输入充值金额：').strip()
        # 若用户输入的不是数字，则让用户重新输入
        if not money.isdigit():
            print('输入必须是数字！')
            continue

        money = int(money)
        dic[name] += money
        with open('db.txt', 'w', encoding='utf-8') as f:
            for use, money in dic.items():
                f.write(f'{use}:{money}\n')
        print(f'成功充值！您当前余额为：{dic[name]}')
        gn(user=name)
        break



# 查询余额
def inquire_money(name):
    with open('db.txt', 'r', encoding='utf-8') as account_database:
        for res in account_database:
            use, money = res.strip().split(':')
            if use == name:
                print(f'尊敬的{name}, 您的余额为{money}')
                gn(user=name)

# 转账功能
def transfer(A_user):
    dic = {}
    B_user = input('请输入转账用户：')
    transfer_money = int(input('请输入转账金额：'))
    with open('db.txt', 'r', encoding='utf-8') as f:
        for ret in f:
            user, money = ret.strip().split(':')
            dic[user] = int(money)

    if dic.get(A_user) >=transfer_money:
        # 转账用户扣钱
        dic[A_user] -= transfer_money
        # 收款用户加钱
        dic[B_user] += transfer_money
        os.remove('db.txt')  # 删除文件
        for i in dic:
            with open('db.txt', 'a+', encoding='utf-8') as f:
                f.write(f'{i}:{dic.get(i)}\n')
        print('转账成功！')
        gn(user=A_user)


# 修改密码
def change_password(user):
    dic = {}
    with open('账号管理.txt', 'r', encoding='utf-8') as account_database:
        for res in account_database:
            use, pwd = res.strip().split(':')
            dic.setdefault(use, pwd)
    new_mm = input('请输入修改后的密码：')
    dic[user] = new_mm
    os.remove('账号管理.txt')  # 删除文件
    for i in dic:
        with open('账号管理.txt', 'a+', encoding='utf-8') as f:
            f.write(f'{i}:{dic.get(i)}\n')
    print('修改成功，请重新登录！')
    sign_in()

# 提现功能
def withdraw(name):
    dic = {}
    with open('db.txt', 'r', encoding='utf-8') as f:
        for ret in f:
            use, money = ret.strip().split(':')
            dic[use] = int(money)
    # 检查当前传入用户是否存在
    if name not in dic:
        print('用户不存在，程序结束！')
        return

    while True:
        money = input('请输入提现金额：').strip()
        # 若用户输入的不是数字，则让用户重新输入
        if not money.isdigit():
            print('输入必须是数字！')
            continue

        money = int(money)
        dic[name] -= money
        with open('db.txt', 'w', encoding='utf-8') as f:
            for use, money in dic.items():
                f.write(f'{use}:{money}\n')
        print(f'提现成功！您当前余额为：{dic[name]}')
        gn(user=name)
        break


# 登录
def sign_in():
    dic = {}
    n = 0
    while True:
        name = input('请输入账号：').strip()
        password = input('请输入密码：').strip()
        with open('账号管理.txt', 'r', encoding='utf-8') as account_database:
            for res in account_database:
                use, pwd = res.strip().split(':')
                dic.setdefault(use, pwd)
        if name in dic and password == dic.get(name):
            print('登录成功!')
            gn(user=name)
            break
        elif name not in dic or password != dic.get(name):
            print(f'账号或密码错误，请重新输入账号！您还有{2 - n}次机会')
        n += 1
        if n == 3:
            print('您的次数已用完，请10秒后再试！')
            time.sleep(10)
            sign_in()


# 注册
def register():
    with open('账号管理.txt', 'r', encoding='utf-8') as account_database:
        for res in account_database:
            use, pwd = res.strip().split(':')
    name = input('请输入需要注册的用户名:')
    if name == use:
        print('账号名重复，请重新输入!')
        register()
    else:
        password = input('请输入注册密码:')
        with open('账号管理.txt', 'a+', encoding='utf-8') as account_database:
            account_database.write(name + ':' + password + '\n')
        with open('db.txt', 'a+', encoding='utf-8') as f:
            f.write(name + ':' + '0' + '\n')
        print('恭喜，注册成功！')
        welcome()


# 欢迎界面
def welcome():
    print('欢迎来到功能有点丰富的ATM系统！')
    input_function = input('请登录账号，如没有账号请注册（输入登录或者注册即可）:')
    if input_function == "登录":
        sign_in()
    elif input_function == "注册":
        register()


welcome()

