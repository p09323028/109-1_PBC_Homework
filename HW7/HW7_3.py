# 資料來源
source_title = input()
source_dict = input()
source_company = input()

# 處理輸入變數
condition = [i for i in input().split(',')]
# 產業類別、總張數
industry, stocks = condition[0], int(condition[1])
# 張數分配
shares = [int(i) for i in condition[2].split(':')]

# 讀入新聞標題，並儲存於title_list
with open(source_title, mode='r', encoding='utf-8') as t:
    title_list = []
    for i in t:
        title_list.append(i.strip().replace(" ", ""))

# 讀入各關鍵字權重，並儲存於keyword_dict
with open(source_dict, mode='r', encoding='utf-8') as d:
    keyword_dict = dict()
    for i in d:
        keyword_weight = i.strip().split(' ')
        keyword_dict[keyword_weight[0]] = int(keyword_weight[1])

# 讀入各公司產業，並儲存於ban_ind_dict
with open(source_company, mode='r', encoding='utf-8') as b:
    ban_ind_dict = dict()
    for i in b:
        ban_industry = i.strip().split(' ')
        ban_ind_dict[ban_industry[0]] = ban_industry[1]


# 定義title_fuc函數，用以處理新聞所含公司名稱及計算分數
def title_fuc(title,
              keywords=list(keyword_dict.keys()),
              companies=list(ban_ind_dict.keys()),
              keyword_dict=keyword_dict):
    # 尋找公司名稱
    ban_result = []
    for i in range(len(companies)):
        if companies[i] in title:
            ban_result.append(companies[i])
    # 將關鍵字以其長度排序，以利後續使用
    keywords = sorted(keywords, key=len, reverse=True)
    # 尋找關鍵字，並計算分數
    score = 0
    i = 0
    while i < len(title):
        for k in keywords:
            if title.count(k) != 0:
                if title[i:i + len(k)] == k:
                    score += keyword_dict[k]
                    i += (len(k) - 1)
                    break
        i += 1
    return ban_result, score  # 回傳公司名稱及分數


# 建立ban_score_dict，儲存各公司分數
ban_score_dict = dict()
for ban in ban_ind_dict.keys():
    ban_score_dict[ban] = 0

# 以 title_fuc 函數計算各家分數，並儲存於ban_score_dict
for t in range(len(title_list)):
    ban_result, banscore = title_fuc(title_list[t])
    # 有出現的公司都要處理
    if ban_result != []:
        for b in ban_result:
            ban_score_dict[b] += banscore

# 建立 target_list，用以儲存指定類別的公司及其分數
target_list = []
ban_ind_list = list(ban_ind_dict.items())
for n in range(len(ban_ind_list)):
    # 指定類別才新增至 target_list
    if ban_ind_list[n][1] == industry:
        target_list.append(
            [ban_ind_list[n][0], ban_score_dict[ban_ind_list[n][0]]])

# 將 target_list先依名稱排序在依分數排序，以符合題目要求
target_list = sorted(target_list, key=lambda s: s[0], reverse=True)
target_list = sorted(target_list, key=lambda s: s[1], reverse=True)

# 計算各公司買張數
if target_list != []:
    buy = [0] * min(len(target_list), len(shares))
    while stocks > 0:
        for i in range(len(buy)):
            if stocks >= shares[i]:
                buy[i] += shares[i]
                stocks -= shares[i]
            else:
                buy[i] += stocks
                stocks = 0
                break

# 輸出結果
if target_list == []:
    print('NO_MATCH')
else:
    for i in range(len(buy)):
        if buy[i] != 0:
            print('{name}購買{number}張'.format(
                name=target_list[i][0], number=buy[i]))