# 輸入變數
num_ubound = [int(i) for i in input().split(',')]  # 物品個數與負重上限
weight = [int(i) for i in input().split(',')]  # 重量
utility = [int(i) for i in input().split(',')]  # 效用

# 變數整理
number = num_ubound[0]  # 物品個數
upper = num_ubound[1]  # 負重上限
sum_weight = 0  # 攜帶重量(初始0)
sum_utility = 0  # 總效用(初始0)
unpick = [i for i in range(number)]
pick = []
cp = [utility[i] / weight[i] for i in range(number)]  # CP值

while unpick != []:
    max_cp = -10000
    min_weight = 10000
    for i in unpick:
        if (cp[i] > max_cp) or (cp[i] == max_cp and weight[i] < min_weight):
            max_cp = cp[i]
            min_weight = weight[i]
            index = i
    unpick.remove(index)
    if sum_weight + weight[index] <= upper:
        sum_weight += weight[index]
        sum_utility += utility[index]
        pick.append(index + 1)
pick.sort()

# 輸出結果
for i in range(len(pick)):
    print(pick[i]) if (i == len(pick) - 1) else print(pick[i], end=',')
