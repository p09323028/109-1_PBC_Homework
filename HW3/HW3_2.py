# 級距個數與食材公斤
num_kg = [int(i) for i in input().split(',')]
num = num_kg[0]
food_kg = num_kg[1]

# 級距公斤與其單價
interval_price = input().split(',')
# 級距公斤
interval = [int(i) for i in interval_price[:num]]
# 單價
price = [int(i) for i in interval_price[num:]]

previous_q = 0  # 紀錄前一筆
cost = 0  # 總成本

# 計算總成本
for i in range(num):
    if food_kg <= interval[i]:
        cost += (food_kg - previous_q) * price[i]
        break
    else:
        cost += (interval[i] - previous_q) * price[i]
        previous_q = interval[i]
print(cost)
