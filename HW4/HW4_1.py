# 輸入變數
num_ubound = [int(i) for i in input().split(',')]  # 物品個數與負重上限
weight = [int(i) for i in input().split(',')]  # 重量
utility = [int(i) for i in input().split(',')]  # 效用
tf = [int(i) for i in input().split(',')]  # 攜帶與否

# 變數整理
number = num_ubound[0]  # 物品個數
upper = num_ubound[1]  # 負重上限
weight_t = 0  # 攜帶重量(初始0)
utility_t = 0  # 得到效用(初始0)

# 計算結果
for i in range(number):
    weight_t += weight[i] * tf[i]
    utility_t += utility[i] * tf[i]

# 輸出結果
if weight_t <= upper:
    print(weight_t, utility_t, sep=',')
else:
    print(-1)
