# 宣告變數與整理
n_b_eta = []  # 標的個數、預算、風險係數
for i in input().split(','):
    n_b_eta.append(int(i))
number = n_b_eta[0]  # 標的個數
bound = n_b_eta[1]  # 預算
eta = n_b_eta[2]  # 風險趨避係數
fund = []  # 資金需求陣列
for i in input().split(','):
    fund.append(int(i))
revenue = []  # 預期報酬陣列
for i in input().split(','):
    revenue.append(int(i))
sigma = []  # 變異數矩陣
for i in range(number):
    sigma.append([])
    for j in input().split(','):
        sigma[i].append(int(j))

# 建立其他變數
max_rev = 0
min_fund = 0
pick = []  # 挑選清單
unpick = []  # 未挑選清單
for i in range(number):
    unpick.append(int(i))

# 執行演算法
while unpick != []:
    index = -10
    for i in unpick:
        tf = [0] * number
        if pick != []:
            for j in pick:
                tf[j] = 1
        tf[i] = 1
        comp_rev = 0
        comp_fund = 0
        for j in range(number):
            comp_rev += tf[j] * revenue[j]
            comp_fund += tf[j] * fund[j]
        for j in range(number):
            for k in range(number):
                comp_rev += (-eta) * tf[j] * sigma[j][k] * tf[k]
        if (comp_fund <= bound) and \
           ((comp_rev > max_rev) or (comp_rev == max_rev and
                                     comp_fund < min_fund)):
            max_rev = comp_rev
            min_fund = comp_fund
            index = i
    if index != -10:
        unpick.remove(index)
        pick.append(index)
    else:
        break

pick.sort()
if pick == []:
    print(0)
else:
    for i in range(len(pick)):
        print(pick[i] + 1) if i == len(pick) - 1 else print(
            pick[i] + 1, end=',')
