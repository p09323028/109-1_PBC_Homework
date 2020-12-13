import operator

# 輸入資料來源及關鍵字
source = input()
keyword = input()

# 以 with open() as 讀入資料
with open(source, mode='r', encoding='utf-8') as qa:
    qalist = []
    for line in qa:
        qalist.append(line.split('\t')[0].strip())
        qalist.append(line.split('\t')[1].strip())

# 建立空白字典，儲存關鍵字前後字元，及其頻率
prefix_freq = dict()
suffix_freq = dict()

# 建立關鍵字list，儲存出現關鍵字的句子
keylist = []
for s in range(len(qalist)):
    if keyword in qalist[s]:
        keylist.append(qalist[s])


# 定義fix_search函數，用以處理前後字元
def fix_search(sentence, keyword):
    for index in range(len(sentence)):
        if sentence[index:index + len(keyword)] == keyword:
            # 處理前一個字
            if index - 1 >= 0:
                global prefix_freq
                if sentence[index - 1] not in prefix_freq:
                    prefix_freq[sentence[index - 1]] = 1
                else:
                    prefix_freq[sentence[index - 1]] += 1
            # 處理後一個字
            if index + len(keyword) < len(sentence):
                global suffix_freq
                if sentence[index + len(keyword)] not in suffix_freq:
                    suffix_freq[sentence[index + len(keyword)]] = 1
                else:
                    suffix_freq[sentence[index + len(keyword)]] += 1


# 呼叫fix_search，處理keylist中的每一個句子
for s in range(len(keylist)):
    fix_search(keylist[s], keyword)

# 排序
prefix_list = sorted(
    prefix_freq.items(), key=operator.itemgetter(0), reverse=True)
suffix_list = sorted(
    suffix_freq.items(), key=operator.itemgetter(0), reverse=True)
prefix_list = sorted(prefix_list, key=operator.itemgetter(1), reverse=True)
suffix_list = sorted(suffix_list, key=operator.itemgetter(1), reverse=True)

print("熱門前一個字:")
for p in range(min(len(prefix_list), 10)):
    print(prefix_list[p][0] + "---" + keyword)

print("熱門下一個字:")
for p in range(min(len(suffix_list), 10)):
    print(keyword + "---" + suffix_list[p][0])