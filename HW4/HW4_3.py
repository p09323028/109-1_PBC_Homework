# 輸入變數
num_ubound = [int(i) for i in input().split(',')]  # 物品個數與負重上限
weight = [int(i) for i in input().split(',')]  # 重量
utility = [int(i) for i in input().split(',')]  # 效用

# 變數整理
number = num_ubound[0]  # 物品個數
upper = num_ubound[1]  # 負重上限
sum_weight_i = 0  # 攜帶重量(初始0)
sum_utility_i = 0  # 總效用(初始0)
unpick_i = [i for i in range(number)]
pick_i = []
cp = [utility[i] / weight[i] for i in range(number)]  # CP值
sum_weight_ii = 0  # 攜帶重量(初始0)
sum_utility_ii = 0  # 總效用(初始0)
unpick_ii = [i for i in range(number)]
pick_ii = []

loop = 1  # 計數
while loop <= number:
    # 演算法I
    max_cp = -10000
    max_utility = -10000
    min_weight_i = 10000
    for i in unpick_i:
        if (cp[i] > max_cp) or (cp[i] == max_cp and weight[i] < min_weight_i):
            max_cp = cp[i]
            min_weight_i = weight[i]
            index = i
    if sum_weight_i + weight[index] <= upper:
        sum_weight_i += weight[index]
        sum_utility_i += utility[index]
        pick_i.append(index + 1)
    unpick_i.remove(index)
    # 演算法II
    min_weight_ii = 10000
    for i in unpick_ii:
        if (utility[i] > max_utility) or \
           (utility[i] == max_utility and weight[i] < min_weight_ii):
            max_utility = utility[i]
            min_weight = weight[i]
            index = i
    if sum_weight_ii + weight[index] <= upper:
        sum_weight_ii += weight[index]
        sum_utility_ii += utility[index]
        pick_ii.append(index + 1)
    unpick_ii.remove(index)
    loop += 1

# 整理結果
pick_i.sort()
pick_cp = pick_i
method_cp = sum_utility_i

pick_ii.sort()
pick_utility = pick_ii
method_utility = sum_utility_ii

# 輸出結果
if method_utility > method_cp:
    for i in range(len(pick_utility)):
        print(pick_utility[i]) if (i == len(pick_utility) - 1) else print(
            pick_utility[i], end=',')
else:
    for i in range(len(pick_cp)):
        print(pick_cp[i]) if (i == len(pick_cp) - 1) else print(
            pick_cp[i], end=',')
