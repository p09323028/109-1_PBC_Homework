# 紀錄list
figure_list = []
input_keep = input()
while input_keep != "LINESTOP":
    figure_list.append([float(i) for i in input_keep.split(',')])
    input_keep = input()

# 紀錄shift
shift = [float(i) for i in input().split(',')]


# 定義plotshift
def plotshift(linelist, xshift=shift[0], yshift=shift[1]):
    for i in range(len(figure_list)):
        linelist[i][0] += xshift
        linelist[i][2] += xshift
        linelist[i][1] += yshift
        linelist[i][3] += yshift
    return linelist


# 定義printlines
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1],
                                                   aline[2], aline[3]))


# 使用plotshift, printlines輸出結果
printlines(plotshift(figure_list))
