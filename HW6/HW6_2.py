# 距離
wid = int(input())
# 關鍵字
keyword_1 = input()
keyword_2 = input()
# 輸入各行字串，並將其連結
string_list = []
string_keep = input()
while string_keep != "INPUT_END":
    string_list.append(string_keep.strip())
    string_keep = input()
string = " ".join(string_list)

# 其他變數
len_k1, len_k2 = len(keyword_1), len(keyword_2)
index_k1, index_k2 = [], []

# 找出關鍵字位置
for index in range(len(string)):
    if string[index:index + len(keyword_1)] == keyword_1:
        index_k1.append(index)
    if string[index:index + len(keyword_2)] == keyword_2:
        index_k2.append(index)


# 定義輸出函數
def printstring(start_k1, start_k2, string):
    #  第1個index
    if (start_k1 - 7) <= 0:
        first = 0
    else:
        first = start_k1 - 7
    # 第2個index
    second = start_k1
    # 第3個index
    third = start_k1 + len(keyword_1)
    # 第4個index
    fourth = start_k2
    # 第5個index
    fifth = start_k2 + len(keyword_2)
    # 第6個index
    if (fifth + 7) > len(string):
        sixth = len(string)
    else:
        sixth = fifth + 7
    # 利用index印出
    print(string[first:second] + "**" + keyword_1 + "**" +
          string[third:fourth] + "**" + keyword_2 + "**" + string[fifth:sixth])


# 判斷兩關鍵字距離是否小於等於距離參數 [0,1,2,3,4,5]
if index_k1 != [] and index_k2 != []:
    find_or_not = False
    for f in index_k1:
        for s in index_k2:
            if s > f and s - f - len(keyword_1) <= wid:
                find_or_not = True
                printstring(start_k1=f, start_k2=s, string=string)

# 輸出結果
if index_k1 == [] or index_k2 == [] or find_or_not is False:
    print("NO_MATCH")
