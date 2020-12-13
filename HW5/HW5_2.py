import math

# 圖形座標list
figure_list = []
input_keep = input()
while input_keep != "LINESTOP":
    figure_list.append([float(i) for i in input_keep.split(',')])
    input_keep = input()

# 逆轉角度
rotate_degree = float(input())


# 定義rotate
def rotate(linelist, degree=rotate_degree):
    # 建立空list以儲存計算結果
    result = []
    for i in range(len(linelist)):
        result.append([0, 0, 0, 0])
    # 角度轉為弧度
    rad = 2 * math.pi * degree / 360
    for i in range(len(linelist)):
        result[i][0] = math.cos(rad) * linelist[i][0] - math.sin(
            rad) * linelist[i][1]
        result[i][1] = math.sin(rad) * linelist[i][0] + math.cos(
            rad) * linelist[i][1]
        result[i][2] = math.cos(rad) * linelist[i][2] - math.sin(
            rad) * linelist[i][3]
        result[i][3] = math.sin(rad) * linelist[i][2] + math.cos(
            rad) * linelist[i][3]
    return result


# 定義printlines
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1],
                                                   aline[2], aline[3]))


# 使用rotate, printlines輸出結果
printlines(rotate(figure_list))
