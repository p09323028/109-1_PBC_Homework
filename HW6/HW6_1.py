# 關鍵字
keyword = input()
# 輸入各行字串，並將其連結
string_list = []
string_keep = input()
while string_keep != "INPUT_END":
    string_list.append(string_keep.strip())
    string_keep = input()
string = " ".join(string_list)


# 定義輸出函數
def printstring(start, string):
    #  第1個index
    if (start - 7) <= 0:
        first = 0
    else:
        first = start - 7
    # 第2個index
    second = start
    # 第3個index
    third = start + len(keyword)
    # 第4個index
    if (third + 7) > len(string):
        fourth = len(string)
    else:
        fourth = third + 7
    # 利用index印出
    print(string[first:second] + "**" + keyword + "**" + string[third:fourth])


# 輸出結果
if string.find(keyword) == -1:
    print("NO_MATCH")

for index in range(len(string)):
    if string[index:index + len(keyword)] == keyword:
        printstring(index, string)
