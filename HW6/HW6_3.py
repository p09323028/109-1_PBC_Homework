# 公司名稱
company = [i for i in input().split(",")]
# 關鍵字，並將其依長度做stable sort，以利使用
keyword = [i for i in input().split(",")]
keyword = sorted(keyword, key=len, reverse=True)

# 輸入各新聞標題，並將其儲存於list
title_list = []
title_keep = input()
while title_keep != "INPUT_END":
    title_list.append(title_keep.replace(" ", ""))
    title_keep = input()


# 定義company_name函數，用以輸出公司名稱
def company_name(title, company):
    result = []
    count = []
    # 計算各公司名稱出現於標題的次數
    for i in range(len(company)):
        count.append(title.count(company[i]))
    # 若次數皆為0，則此筆為NO_MATCH
    if count == [0] * len(company):
        return "NO_MATCH"
    else:
        while count != [0] * len(company):
            max = -100
            max_index = -10
            # 尋找次數最多的關鍵字
            for i in range(len(count)):
                if count[i] > max:
                    max = count[i]
                    max_index = i
            # 找到後，將其儲存至result，並把其次數歸零
            if count[max_index] != 0:
                result.append(company[max_index])
            count[max_index] = 0
        return ",".join(result)


# 定義divide函數，用以切割新聞標題
def divide(title, keyword):
    result = []  # 用以儲存切割資料
    count = []
    # 計算各關鍵字出現於標題的次數
    for i in range(len(keyword)):
        count.append(title.count(keyword[i]))
    # 若次數皆為0，則直接回傳
    if count == [0] * len(keyword):
        return title
    else:
        i = 0
        string = ""
        # 由左自右找尋新聞標題
        while i != len(title):
            for k in keyword:
                # 判斷 字首及後續文字 是否為 關鍵字
                if title[i:i + len(k)] == k:
                    result.append(string) if result == [] else result.append(
                        string[1:])
                    string = ""
                    result.append(k)
                    i += (len(k) - 1)
                    break
            string += title[i]
            i += 1
        result.append(string[1:])
        return "/".join(result)  # 將切割資料以"/"做連結


# 呼叫company_name函數、divide函數，判斷各筆資料
for i in range(len(title_list)):
    output_name = company_name(title_list[i], company)
    # 將divide函數的輸出值，去除"//"及頭尾"/"
    output_title = divide(title_list[i], keyword).strip('/').replace('//', '/')
    if output_name == "NO_MATCH":
        print(output_name)
    else:
        print(output_name + ";" + output_title)