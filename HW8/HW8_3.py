from datetime import datetime as dt


class Dog:
    def __init__(self, name, height, weight, adopted_date):
        # Class初始化
        self.name = name
        self.height = height
        self.weight = weight
        self.adopted_date = adopted_date
        self.dust = 0
        self.walk_count = 0  # 散步次數
        self.longest_duration = 0  # 最大散步間隔天數
        self.last_walk_date = adopted_date  # 上次散步日期
        self.is_small_dog = self.check_if_small_dog()

    def __str__(self):
        # 設定物件輸出
        return self.name + ',' + str(self.height) + ',' + str(
            self.weight) + ',' + str(self.dust)

    def check_if_small_dog(self):
        # 判 斷 是 否 為 小 型 犬， 回 傳 boolean 值
        if self.height > 60 or self.weight > 30:
            return False
        else:
            return True

    def walk(self, walk_date):
        if self.is_small_dog:
            # 依 據 小 型 犬 的 灰 塵 累 積 效 率 更 新 累 積 灰 塵 量
            self.dust += 3
        else:
            # 依 據 大 型 犬 的 灰 塵 累 積 效 率 更 新 累 積 灰 塵 量
            self.dust += 2
        # 更 新 散 步 次 數、 最 大 散 步 間 隔 時 間、 最 近 散 步 日 期
        # 判斷最大間隔時間
        if self.walk_count == 0:  # 第一次散步
            diff = (walk_date - self.adopted_date)
        else:  # 非第一次散步
            diff = (walk_date - self.last_walk_date)
        if diff.days > self.longest_duration:
            self.longest_duration = diff.days
        self.walk_count += 1
        self.last_walk_date = walk_date

    def bathe(self):
        # 更 新 累 積 灰 塵 量
        self.dust = 0

    def is_heigher(self, dog):
        # 比較身高高者
        if self.height > dog.height:
            return True
        return False

    def is_heavier(self, dog):
        # 比較重量重者
        if self.weight > dog.weight:
            return True
        if self.weight == dog.weight and self.is_heigher(dog):
            return True
        return False

    def is_same_size(self, dog):
        # 比較大小狗
        if (self.is_small_dog is False) and (dog.is_small_dog is True):
            return True
        if (self.is_small_dog is True) and (dog.is_small_dog is True):
            if self.is_heavier(dog):
                return True
        if (self.is_small_dog is False) and (dog.is_small_dog is False):
            if self.is_heavier(dog):
                return True
        return False

    def is_frqlower(self, dog):
        # 比較出頻率低者
        diff1 = (today - self.adopted_date)
        diff2 = (today - dog.adopted_date)
        if (self.walk_count / diff1.days) < (dog.walk_count / diff2.days):
            return True
        if (self.walk_count / diff1.days) == (dog.walk_count / diff2.days):
            if self.is_same_size(dog):
                return True
        return False

    def is_steplonger(self, dog):
        # 比較最大散步間隔時間較長者
        if self.longest_duration > dog.longest_duration:
            return True
        if (self.longest_duration == dog.longest_duration):
            if self.is_same_size(dog):
                return True
        return False

    def is_dirtier(self, dog):
        # 比較灰塵數較多者
        if self.dust > dog.dust:
            return True
        if (self.dust == dog.dust):
            if self.is_same_size(dog):
                return True
        return False


# 今天日期
today = dt.strptime(input(), "%Y/%m/%d")

# 任務、狗狗名稱
task_name = input()
task = task_name[0:5]

# 事件清單
inputkeep, event = input(), []
while inputkeep != 'Done':
    event.append([i for i in inputkeep.split('|')])
    inputkeep = input()

# 記錄狗狗名稱
namelist = []

# 事件發生
for i in range(len(event)):
    # A事件:領養
    if event[i][0] == 'A':
        # 以狗狗名稱建立物件
        locals()[event[i][1].lower()] = Dog(
            event[i][1], int(event[i][2]), int(event[i][3]),
            dt.strptime(event[i][4], "%Y/%m/%d"))
        namelist.append(event[i][1].lower())
    # B事件:洗澡
    if event[i][0] == 'B':
        locals()[event[i][1].lower()].bathe()
    # W事件:散步
    if event[i][0] == 'W':
        locals()[event[i][1].lower()].walk(
            dt.strptime(event[i][2], "%Y/%m/%d"))
    # L事件:換主人
    if event[i][0] == 'L':
        namelist.remove(event[i][1].lower())
namelist = sorted(namelist)

# 任務A: 輸出指定狗狗的資料
if task == 'TaskA':
    name = task_name[6:]
    print(locals()[name.lower()])

# 任務B: 散步頻率最少的狗狗資料
if task == 'TaskB':
    minfrq_dog = locals()[namelist[0]]
    for i in range(1, len(namelist)):
        if locals()[namelist[i]].is_frqlower(minfrq_dog):
            minfrq_dog = locals()[namelist[i]]
    print(minfrq_dog)

# 任務C: 間隔最長的狗狗資料
if task == 'TaskC':
    steplogest_dog = locals()[namelist[0]]
    for i in range(1, len(namelist)):
        if locals()[namelist[i]].is_steplonger(steplogest_dog):
            steplogest_dog = locals()[namelist[i]]
    print(steplogest_dog)

# 任務D: 灰塵數最多的狗狗資料
if task == 'TaskD':
    dirtiest_dog = locals()[namelist[0]]
    for i in range(1, len(namelist)):
        if locals()[namelist[i]].is_dirtier(dirtiest_dog):
            dirtiest_dog = locals()[namelist[i]]
    print(dirtiest_dog)