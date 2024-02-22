def list_sort():
    list01 = [8, 7, 1, 2, 5, 4, 0, 9]

    for i in range(len(list01)):
        for j in range(len(list01) - 1):
            # print('{}-{}'.format(list01[i], list01[j]))
            if list01[j] > list01[j + 1]:
                list01[j], list01[j + 1] = list01[j + 1], list01[j]

    print(list01)


def list_search():
    list01 = [11, 8, 7, 1, 2, 5, 4, 0, 9, 12]
    for i in range(len(list01)):
        for j in range(len(list01) - 1):
            if list01[j] > list01[j + 1]:
                list01[j], list01[j + 1] = list01[j + 1], list01[j]

    print(list01)

    target = 8
    start = 0
    end = len(list01) - 1
    while start <= end:
        index = (start + end) // 2
        if list01[index] == target:
            print(index)
            break
        elif target > list01[index]:
            end = index - 1
        else:
            start = index + 1


def list_dis_dup():
    list01 = [11, 11, 7, 12, 2, 5, 4, 0, 9, 12]
    list02 = []

    for i in list01:
        if i not in list02:
            list02.append(i)
    print(list02)


def two_sum():
    nums = [3, 3]
    target = 6
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('{}-{}'.format(i, j))


def rev_num():
    x = 121
    if x > 0:
        res = int(str(x)[::-1])
        if res == x:
            return True
        else:
            return False
    if x == 0:
        return True
    if x < 0:
        return False


def roma_num():
    dict01 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    s = "MCMXCIV"
    sum = 0
    for i in range(len(s) - 1):
        if dict01[s[i]] >= dict01[s[i + 1]]:
            sum += dict01[s[i]]
        elif dict01[s[i]] < dict01[s[i + 1]]:
            sum -= dict01[s[i]]
    sum += dict01[s[len(s) - 1]]
    print(sum)


def most_prefix():
    strs = ["flower", "flow", "flight"]
    if len(strs) == 0:
        return ''
    firstStr = strs[0]
    for i in range(len(strs)):
        while strs[i].find(firstStr, 0) != 0:
            firstStr = firstStr[0:len(firstStr) - 1]
    if firstStr == '':
        return ''
    else:
        print(firstStr)


def brack():
    s = "(])"
    list01 = []

    for i in range(len(s)):
        if s[i] in ['(', '{', '[']:
            list01.append(s[i])
        if s[i] == ')':
            if len(list01) == 0:
                print(False)
                break
            if list01[len(list01) - 1] == '(':
                list01.pop()
            else:
                print(False)
                break
        if s[i] == '}':
            if len(list01) == 0:
                print(False)
                break
            if list01[len(list01) - 1] == '{':
                list01.pop()
            else:
                print(False)
                break
        if s[i] == ']':
            if len(list01) == 0:
                print(False)
                break
            if list01[len(list01) - 1] == '[':
                list01.pop()
            else:
                print(False)
                break
    if len(list01) == 0:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    # list_sort()
    # list_search()
    # list_dis_dup()
    # two_sum()
    # rev_num()
    # roma_num()
    # most_prefix()
    brack()
