def climb_stairs():
    n = 4

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    elif n == 2:
        print(2)

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    print(b)


# 斐波那契數列
def fb_list():
    n = 10
    if n == 0:
        print([])
    elif n == 1:
        print([0])
    elif n == 2:
        print([0, 1])

    fb = [0] * n
    fb[0] = 0
    fb[1] = 1

    for i in range(2, n):
        fb[i] = fb[i - 1] + fb[i - 2]
    print(fb)


# 0-1 背包問題
def dp_bag():
    weights = [1, 2, 3, 5]
    values = [1, 6, 10, 16]
    W = 7

    n = len(weights)
    # 創建二維數組，第一層是物品數量，第二層是背包容量
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # 第一層循環 數量
    for i in range(1, n + 1):
        # 第二層循環 背包容量
        for j in range(1, W + 1):
            # 如果當前物品重量小於等於背包容量
            if weights[i - 1] <= j:
                # 不選擇第i個物品，前i-1個物品，在容量j的情況下總價值
                # 選擇第i個物品，背包容量會減少，但總價值會增加
                # 選較大的一個
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            # 如果當前物品重量大於背包容量
            else:
                # 不選擇第i個物品，前i-1個物品，在容量j的情況下總價值
                dp[i][j] = dp[i - 1][j]
    # 歷完所有物品，嘗試了所有容量之後的最大價值
    print(dp[n][W])


# 最長公共子串
def long_common_substring():
    s1 = "abcde"
    s2 = "bcdef"

    # 以兩個字符串長度為維度，創建二維數組
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # 最長長度、結束索引
    max_len = 0
    end_index = 0

    # 雙重循環
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # 如果相等
            if s1[i - 1] == s2[j - 1]:
                # 在前一個長度值基礎上加1
                dp[i][j] = dp[i - 1][j - 1] + 1
                # 更新最大長度和結束索引
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            # 如果不等，長度重置為0
            else:
                dp[i][j] = 0
    # 打印最大長度和最大長度字符串
    print(max_len)
    print(s1[end_index - max_len:end_index])


if __name__ == '__main__':
    # climb_stairs()
    # fb_list()
    # dp_bag()
    long_common_substring()
