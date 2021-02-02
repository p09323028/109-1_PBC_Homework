# 城鎮, 基地台, 距離
npd = [int(i) for i in input().split()]
n, p, d = npd[0], npd[1], npd[2]

# 各城市資料 [x座標, y座標, 人數]
citylist = []
for i in range(n):
    citylist.append([int(i) for i in input().split()])

# 建造點及總人數
loc, people = [], 0
# 建p座
for i in range(p):
    # 紀錄各城市可覆蓋到的地方及其人數和
    coverplist = []
    for a in range(n):
        cp = 0
        covercity = []
        for b in range(n):
            dist = ((citylist[a][0]-citylist[b][0])**2+(citylist[a][1]-citylist[b][1])**2)** 0.5
            if dist <= d:
                cp += citylist[b][2]
                covercity.append(b)
        coverplist.append([covercity, cp, a])
    # print(coverplist)
    # maxp 最大涵蓋人數; maincity 最大涵蓋人數的城市
    maxp, maincity = 0, 0
    for c in range(n):
        if coverplist[c][1] > maxp:
            maxp = coverplist[c][1]
            mcovercity = coverplist[c][0] # 城市可覆蓋到的地方
            maincity = c + 1
    loc.append(str(maincity))
    people += maxp
    # print(maincity, mcovercity, maxp, people)
    # 將建造基地台城市可覆蓋到的地方人口數改成 0
    for j in mcovercity:
        citylist[j][2] = 0
print(' '.join(loc), people)

    
    
