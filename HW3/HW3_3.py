# 級距個數與食材公斤
num_kg = [int(i) for i in input().split(',')]
num = num_kg[0]
food_kg = num_kg[1]

# 級距公斤與其單價
interval_price = input().split(',')
# 級數公斤
interval = [int(i) for i in interval_price[:num]]
# 單價
price = [int(i) for i in interval_price[num:]]

previous_q = 0  # 紀錄前一筆
cost = 0  # 總成本

# 計算剛好x公斤的最佳解
for i in range(num):
    if food_kg <= interval[i]:
        cost += (food_kg - previous_q) * price[i]
        break
    else:
        cost += (interval[i] - previous_q) * price[i]
        previous_q = interval[i]

best_cost = cost  # 將"剛好買x公斤時的成本"預設為最佳解
best_kg = food_kg  # 將"x公斤"預設為最佳解公斤數

previous_q = 0  # 重置紀錄
cost = 0  # 重置總成本

# 計算最佳解
for i in range(num):
    cost += (interval[i] - previous_q) * price[i]
    previous_q = interval[i]
    if interval[i] >= food_kg and cost <= best_cost:
        best_kg = interval[i]
        best_cost = cost

print(best_kg, best_cost, sep=',')
