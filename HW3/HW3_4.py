# 商品的種類數
item_number = int(input())
# 組成套組的商品編號
bundle_item = input().split(',')
for i in range(len(bundle_item)):
    bundle_item[i] = int(bundle_item[i])
# 商品編號是否為套組
bundle_tf = [0] * item_number
for i in bundle_item:
    bundle_tf[i - 1] = 1
# 商品價格
price = input().split(',')
for i in range(len(price)):
    price[i] = int(price[i])
# 購買數量
quantity = input().split(',')
for i in range(len(quantity)):
    quantity[i] = int(quantity[i])

# 計算未折扣金額
origin_cost = 0
for i in range(item_number):
    origin_cost += price[i] * quantity[i]

# 計算湊成的組數
min_bundle = 10000000000000000000
for i in range(item_number):
    if bundle_tf[i] != 0 and bundle_tf[i] * quantity[i] < min_bundle:
        min_bundle = bundle_tf[i] * quantity[i]

# 計算折扣後金額
discount_cost = 0
for i in range(item_number):
    if bundle_tf[i] == 0:
        discount_cost += price[i] * quantity[i]
    else:
        discount_cost += price[i] * (min_bundle // 5) * 5 * 0.8 + \
                         price[i] * (min_bundle % 5) * 0.9 + \
                         price[i] * (quantity[i] - min_bundle)
# 計算可招募人數
player = int((origin_cost - discount_cost) / 1000)

# 輸出結果
if player < 1:
    print("So sad. I messed up.")
else:
    print(int(discount_cost), player, sep=',')
    