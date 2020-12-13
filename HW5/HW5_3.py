# 輸入records資料
records = []
data = input()
while data != "RECORDSTOP":
    records.append([i for i in data.split(',')])
    data = input()

# 將打擊數、安打數存為整數
for i in range(len(records)):
    records[i][3] = int(records[i][3])
    records[i][4] = int(records[i][4])


# 球員打擊率[0隊伍, 1球號, 2球季, 3打擊數, 4安打數]
def player_avg(seasons, records, player_number):
    at_bat, hit = 0, 0
    for i in range(len(records)):
        if (records[i][2] in seasons) and (records[i][1] == player_number):
            at_bat += records[i][3]
            hit += records[i][4]
    if at_bat != 0:
        player_bt = hit / at_bat
    else:
        player_bt = 0
    return player_bt, at_bat  # 回傳打擊率、打擊數


# 球隊打擊率[0隊伍, 1球號, 2球季, 3打擊數, 4安打數]
def team_avg(seasons, records, team_number):
    at_bat, hit = 0, 0
    for i in range(len(records)):
        if (records[i][2] in seasons) and (records[i][0] == team_number):
            at_bat += records[i][3]
            hit += records[i][4]
    if at_bat != 0:
        team_bt = hit / at_bat
    else:
        team_bt = 0
    return team_bt, at_bat  # 回傳打擊率、打擊數


# 表現最佳球員[0隊伍, 1球號, 2球季, 3打擊數, 4安打數]
def best_player(seasons, records):
    best = []  # 儲存各球季表現最佳球員
    # 各球季迴圈
    for s in range(len(seasons)):
        player = []  # 指定球季，球員
        player_at_bat = []  # 指定球季，球員打擊數
        player_bt = []  # 指定球季，球員打擊率
        # 計算指定球季裡，各球員的打擊數、打擊率
        for i in range(len(records)):
            if records[i][2] == seasons[s] and records[i][1] not in player:
                player.append(records[i][1])
                player_bt_value, player_at_bat_value = player_avg(
                    [records[i][2]], records, records[i][1])
                player_at_bat.append(player_at_bat_value)
                player_bt.append(player_bt_value)
        best_bt = -1
        best_one = 10000
        best_at_bat = 10000
        # 尋找指定球季裡，最佳球員
        for i in range(len(player_bt)):
            if (player_bt[i] > best_bt) or (
                player_bt[i] == best_bt and
                player_at_bat[i] < best_at_bat) or (
                 player_bt[i] == best_bt and
                 player_at_bat[i] == best_at_bat and
                 int(player[i]) < best_one):
                best_bt = player_bt[i]
                best_one = int(player[i])
                best_at_bat = player_at_bat[i]
        best.append(best_one)
    return best


# 表現最佳球隊[0隊伍, 1球號, 2球季, 3打擊數, 4安打數]
def best_team(seasons, records):
    best = []  # 儲存各球季表現最佳球隊
    # 各球季迴圈
    for s in range(len(seasons)):
        team = []  # 指定球季，球隊
        team_at_bat = []  # 指定球季，球隊打擊數
        team_bt = []  # 指定球季，球隊打擊率
        # 計算指定球季裡，各球隊的打擊數、打擊率
        for i in range(len(records)):
            if records[i][2] == seasons[s] and records[i][0] not in team:
                    team.append(records[i][0])
                    team_bt_value, team_at_bat_value = team_avg(
                        [records[i][2]], records, records[i][0])
                    team_at_bat.append(team_at_bat_value)
                    team_bt.append(team_bt_value)
        best_bt = -1
        best_group = 'A'
        best_at_bat = 10000
        # 尋找指定球季裡，最佳球隊
        for i in range(len(team_bt)):
            if (team_bt[i] > best_bt) or (
                team_bt[i] == best_bt and team_at_bat[i] < best_at_bat) or (
                 team_bt[i] == best_bt and team_at_bat[i] == best_at_bat and
                 team[i] < best_group):
                best_bt = team_bt[i]
                best_group = team[i]
                best_at_bat = team_at_bat[i]
        best.append(best_group)
    return best


# 輸入function資料 [函數, 球季, 指定]
function = []
data = input()
while data != "FUNCTIONSTOP":
    function.append([i for i in data.split(' ')])
    data = input()

# 處理function的年度資料
for i in range(len(function)):
    function[i][1] = function[i][1].split(',')


# 定義題目所述之無條件捨去
def chop(avg):
    avg = int(avg * 100) / 100
    return avg if avg > 0 else 0


# 定義list輸出
def printlist(alist):
    for i in range(len(alist)):
        if (i != len(alist) - 1):
            print(alist[i], end=',')
        else:
            print(alist[i])


# 輸出結果
for i in range(len(function)):
    if function[i][0] == '1':
        player_bt, player_at_bat = player_avg(
            seasons=function[i][1], records=records,
            player_number=function[i][-1])
        print(chop(player_bt))
    elif function[i][0] == '2':
        team_bt, team_at_bat = team_avg(
            seasons=function[i][1], records=records,
            team_number=function[i][-1])
        print(chop(team_bt))
    elif function[i][0] == '3':
        printlist(best_player(seasons=function[i][1], records=records))
    else:
        printlist(best_team(seasons=function[i][1], records=records))
