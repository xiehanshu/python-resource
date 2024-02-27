import sys

from ListNode import ListNode
from TreeNode import TreeNode


def list_sort():
    list01 = [8, 7, 1, 2, 5, 4, 0, 9]

    for i in range(len(list01)):
        for j in range(len(list01) - 1):
            if list01[j] > list01[j + 1]:
                list01[j], list01[j + 1] = list01[j + 1], list01[j]

    print(list01)


def list_search_two_part():
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


def bracket():
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


def list_node_conn():
    res = ListNode()
    node = res
    list1 = ListNode()
    list2 = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    if list1:
        node.next = list1
    else:
        node.next = list2
    print(res.next)


def del_dup_list():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in nums[0:i]:
            nums.pop(i)
    print(len(nums))


def rem_ele_list():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    print(nums)


def find_first_index():
    haystack = "mississippi"
    needle = "pi"

    res = haystack.find(needle, 0)
    # print(res)

    for i in range(len(haystack)):
        if haystack[0:i + 1] == needle:
            print(0)
            break
        if haystack[len(haystack) - 1:len(haystack)] == needle:
            print(len(haystack) - 1)
            break
        for j in range(i + 1, len(haystack)):
            if haystack[i:j + 1] == needle:
                print(i)
                break
    print(-1)


def search_insert_index():
    nums = [1, 3, 5, 6]
    target = 7

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            print(mid)
            break
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    print(start)


def find_last_word():
    s = "luffy is still joyboy"

    list01 = s.split(' ')
    for i in range(len(list01) - 1, -1, -1):
        if list01[i] == '':
            continue
        else:
            print(len(list01[i]))
            break


def plus_one():
    digits = [0]
    str01 = ''
    for i in range(len(digits)):
        str01 = str01 + str(digits[i])
    int01 = int(str01) + 1
    list01 = []
    for i in str(int01):
        list01.append(int(i))
    print(list01)


def binary_plus():
    a = "11"
    b = "1"

    res = bin(int(a, 2) + int(b, 2))[2:]
    print(res)


def plus_plus():
    x = 8
    if x == 0:
        print(0)
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        square = mid * mid

        if x == square:
            print(mid)
            break
        if square > x:
            end = mid - 1
        else:
            start = mid + 1
    print(start - 1)


def climb_stairs():
    n = 3

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    a, b = 1, 2

    for i in range(3, n + 1):
        a, b = b, a + b
    print(b)


def list_node_del_dup():
    head = ListNode()
    if head is None:
        return None
    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def tree_mid():
    root = TreeNode()
    cur = root
    tmp = []
    res = []

    while cur or tmp:
        while cur:
            tmp.append(cur)
            cur = cur.left
        cur = tmp.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def max_income():
    prices = [2, 4, 1]
    # dist = 0
    #
    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         if prices[j] - prices[i] > dist:
    #             dist = prices[j] - prices[i]
    # print(dist)
    minV = prices[0]
    maxV = 0

    for i in range(1, len(prices)):
        maxV = max(maxV, prices[i] - minV)
        minV = min(minV, prices[i])

    print(maxV)


def back_to_end_str():
    s = "0P"
    s = s.lower()
    print(s)
    tmpList = []
    tmpStr = ''
    for i in s:
        if i.isalpha() or i.isnumeric():
            tmpList.append(i)
    tmpStr = ''.join(tmpList)
    if tmpStr == tmpStr[::-1]:
        print(True)
    else:
        print(False)


def only_one():
    nums = [2, 2, 1]
    list01 = []

    for i in nums:
        if i not in list01:
            list01.append(i)
        elif i in list01:
            list01.remove(i)
    print(list01)


def appear_half():
    nums = [2, 2, 1, 1, 1, 2, 2]
    times = len(nums) / 2
    dict01 = {}

    for i in range(len(nums)):
        if nums[i] not in dict01.keys():
            dict01[nums[i]] = 1
        elif nums[i] in dict01.keys():
            dict01[nums[i]] += 1
    for i, j in dict01.items():
        if j > times:
            print(i)


def happy_num():
    n = 19

    def a(n):
        sum = 0
        for i in str(n):
            sum += int(i) * int(i)
        return sum

    rec = set()

    while True:
        n = a(n)

        if n == 1:
            return True

        if n in rec:
            return False
        else:
            rec.add(n)


def if_dup_ele_list():
    nums = [1, 2, 3, 1]
    dict01 = {}

    for i in nums:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1
    for i, j in dict01.items():
        if j > 1:
            print(True)
            break
    print(False)


def if_dup_ele_list_s():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                print(True)
                break
    print(False)

    start = 0
    end = len(nums) - 1


def one_pos_num():
    num = 38
    # sum = 0

    while len(str(num)) != 1:
        sum = 0
        for i in str(num):
            sum += int(i)
        num = sum
    print(num)


def lost_num_in_list():
    nums = [0]
    length = len(nums)
    list01 = []
    for i in range(length + 1):
        list01.append(i)
    print(list01)

    for i in list01:
        if 0 <= i <= length and i not in nums:
            print(i)


def move_zero():
    nums = [0, 1, 0, 3, 12]
    numIndex = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            numIndex += 1

    for i in range(numIndex):
        nums.append(0)

    print(nums)


def rev_str():
    s = ["h", "e", "l", "l", "o"]
    start = 0
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print(s)


def list_cross():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    listRes = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))

    for i in nums1:
        for j in nums2:
            if j == i:
                listRes.append(j)
    print(listRes)


def list_cross_s():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    tmp = {}
    res = []

    for i in nums1:
        if i not in tmp.keys():
            tmp[i] = 1
        else:
            tmp[i] += 1

    for i in nums2:
        if i in tmp.keys() and tmp[i] > 0:
            res.append(i)
            tmp[i] -= 1
    print(res)


def perfect_square():
    num = 17
    start = 0
    end = num

    while start <= end:
        mid = (start + end) // 2
        sq = mid * mid

        if sq == num:
            print(mid)
            break
        if sq > num:
            end = mid - 1
        else:
            start = mid + 1
    print(mid)
    if mid * mid != num:
        print(False)


def list_cons():
    ransomNote = "bg"
    magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

    dict01 = {}

    for i in ransomNote:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    for i in magazine:
        if i in dict01.keys() and dict01[i] > 0:
            dict01[i] -= 1

    for i, j in dict01.items():
        if j != 0:
            print(False)
            break
    print(True)


def only_char_in_str():
    s = "loveleetcode"
    dict01 = {}

    for i in s:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    for i in range(len(s)):
        if dict01[s[i]] == 1:
            print(i)
            break
    print(-1)


def dif_str():
    s = "a"
    t = "aa"

    dict01 = {}

    for i in t:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1
    print(dict01)

    for i in s:
        if i in dict01.keys() and dict01[i] > 0:
            dict01[i] -= 1
    print(dict01)

    for i, j in dict01.items():
        if j > 0:
            print(i)
            break
    print(-1)


def long_rev_str():
    s = "bb"
    dict01 = {}

    for i in s:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    length = 0
    two = 0
    for i, j in dict01.items():
        if j % 2 == 0:
            length += j
        elif j > 2 and j % 2 == 1:
            length += j - 1
            two += 1
        elif j < 2 and j % 2 == 1:
            two += 1
    if two != 0:
        print(length + 1)
    else:
        print(length)


def three_five():
    n = 15
    list01 = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list01.append('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            list01.append('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            list01.append('Buzz')
        else:
            list01.append(str(i))
    print(list01)


def most_third():
    nums = [1, 2]
    list01 = []

    for i in nums:
        if i not in list01:
            list01.append(i)
    for i in range(len(list01)):
        for j in range(i, len(list01)):
            if list01[i] < list01[j]:
                list01[i], list01[j] = list01[j], list01[i]
    if len(list01) >= 3:
        print(list01[2])
    else:
        print(list01[0])


def str_to_int():
    sys.set_int_max_str_digits(10000)
    num1 = "11"
    num2 = "123"
    len2 = len(num2)
    num2Tmp = 0
    len1 = len(num1)
    num1Tmp = 0

    for i in range(len2):
        num2Tmp += int(num2[i]) * int('1' + '0' * (len2 - 1 - i))

    for i in range(len1):
        num1Tmp += int(num1[i]) * int('1' + '0' * (len1 - 1 - i))

    print(str(num1Tmp + num2Tmp))


def word_in_str():
    s = "                "
    if s == '':
        print(0)
    s = s.split(' ')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '':
            s.pop(i)
    print(len(s))


def arrange_nums():
    n = 8
    i = 1
    sum = 0
    while True:
        sum += i
        i += 1
        if n - sum < i:
            break
    print(i - 1)


def gone_nums_in_list():
    nums = [1, 1]
    len01 = len(nums)
    nums = set(nums)
    tmp = []
    for i in range(1, len01 + 1):
        tmp.append(i)

    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] in nums:
            tmp.pop(i)
    print(tmp)


def format_password():
    s = "--a-a-a-a--"
    k = 2
    res = ''
    mark = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i].isalpha() or s[i].isnumeric():
            mark += 1
            res += s[i]
            if mark == k:
                res += '-'
                mark = 0
    while True:
        if res.endswith('-'):
            res = res[0:len(res) - 1]
        else:
            break
    print(res)
    print(res[::-1].upper())


def most_appear_one():
    nums = [1, 0, 1, 1, 0, 1]
    res = 0
    tmp = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            tmp += 1
        if nums[i] != 1 or i == (len(nums) - 1):
            if tmp > res:
                res = tmp
            tmp = 0

    print(res)


def attack_duration():
    timeSeries = [1, 3, 5, 7, 9, 11, 13, 15]
    duration = 3
    poison = 0

    for i in range(len(timeSeries) - 1):
        if i == 0:
            poison = duration
        if timeSeries[i + 1] - timeSeries[i] >= duration:
            poison += duration
        else:
            poison += (timeSeries[i + 1] - timeSeries[i])

    if len(timeSeries) == 1:
        poison = duration

    print(poison)


def large_ele_in_list():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    res = []

    for i in range(len(nums1)):
        pos = nums2.index(nums1[i])
        for j in range(pos, len(nums2)):
            if nums2[j] > nums1[i]:
                res.append(nums2[j])
                break
            elif j == (len(nums2) - 1) and nums2[j] <= nums1[i]:
                res.append(-1)
                break
    print(res)

# def keyboard_word():
#     one = 'qwertyuiop'
#     two = 'asdfghjkl'
#     three = 'zxcvbnm'



if __name__ == '__main__':
    # list_sort()
    # list_search_two_part()
    # list_dis_dup()
    # two_sum()
    # rev_num()
    # roma_num()
    # most_prefix()
    # bracket()
    # del_dup_list()
    # rem_ele_list()
    # find_first_index()
    # search_insert_index()
    # find_last_word()
    # plus_one()
    # binary_plus()
    # plus_plus()
    # climb_stairs()
    # list_node_conn()
    # max_income()
    # back_to_end_str()
    # only_one()
    # appear_half()
    # happy_num()
    # if_dup_ele_list()
    # if_dup_ele_list_s()
    # one_pos_num()
    # lost_num_in_list()
    # move_zero()
    # rev_str()
    # list_cross()
    # list_cross_s()
    # perfect_square()
    # list_cons()
    # only_char_in_str()
    # dif_str()
    # long_rev_str()
    # three_five()
    # most_third()
    # str_to_int()
    # word_in_str()
    # arrange_nums()
    # gone_nums_in_list()
    # format_password()
    # most_appear_one()
    # attack_duration()
    large_ele_in_list()
