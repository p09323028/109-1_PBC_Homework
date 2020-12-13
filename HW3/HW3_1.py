number = int(input())  # 輸入數字(1~9999)
n_list = [0, 0, 0, 0]  # 依序儲存千百十個位數

while True:
    n_list[0] = number // 1000  # 取千位數
    n_list[1] = (number % 1000) // 100  # 取百位數
    n_list[2] = (number % 100) // 10  # 取十位數
    n_list[3] = (number % 10)  # 取個位數
    n_list.sort()  # 遞增
    number = \
        (n_list[3] * 1000 + n_list[2] * 100 + n_list[1] * 10 + n_list[0]) - \
        (n_list[0] * 1000 + n_list[1] * 100 + n_list[2] * 10 + n_list[3])
    print(number, end=",") if number != 6174 else print(number)
    if number == 6174:
        break
