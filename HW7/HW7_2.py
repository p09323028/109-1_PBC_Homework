# 輸入來源及電影ID
u_item = input()
u_genre = input()
movie_id = int(input())

# 以 with open() as 讀入電影資料
with open(u_item, mode='r', encoding='ISO-8859-1') as m:
    movie = dict()
    # index 0為儲存電影名稱, 1為類型布林值
    for line in m:
        movie[int(line.split("|")[0])] = [line.split("|")[1]]
        movie[int(line.split("|")[0])].append(
            [int(i) for i in line.strip().split("|")[5:]])

# 以 with open() as 讀入類型資料
with open(u_genre, mode='r', encoding='ISO-8859-1') as g:
    genre = dict()
    for line in g:
        # 有"|"才讀入
        if "|" in line:
            genre[int(line.split("|")[1])] = line.split("|")[0]


# 定義movie_genre函數，用以輸出電影類型名稱
def movie_genre(genre_list):
    genre_name = []
    # 利用順序特性做轉換
    for i in range(len(genre_list)):
        if genre_list[i] == 1:
            genre_name.append(genre[i])
    return genre_name


# 將字典中，原本01電影類型，以movie_genre函數，換成電影類型名稱
for item in movie.keys():
    movie[item][1] = movie_genre(movie[item][1])

# 輸出結果
if movie_id in movie.keys():
    print(movie[movie_id][0] + ": " + ", ".join(movie[movie_id][1]))
else:
    print("No movie found.")