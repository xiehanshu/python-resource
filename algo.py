import collections
import math
import random
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
    # sys.set_int_max_str_digits(10000)
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


def list_rank():
    score = [10, 3, 8, 9, 4]
    tmp = score.copy()
    dict01 = {}
    res = []
    c = 0
    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            if tmp[i] < tmp[j]:
                tmp[i], tmp[j] = tmp[j], tmp[i]
    for i in tmp:
        if c == 0:
            dict01[i] = 'Gold Medal'
        elif c == 1:
            dict01[i] = 'Silver Medal'
        elif c == 2:
            dict01[i] = 'Bronze Medal'
        elif c > 2:
            dict01[i] = str(c + 1)
        c += 1

    for i in score:
        res.append(dict01[i])

    print(res)


def fib_num():
    n = 4

    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n - 2) + fib(n - 1)

    print(fib(n))

    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)


def upper_in_word():
    word = "USA"
    upC = 0

    for i in word:
        if i.isupper():
            upC += 1

    if upC == 0:
        print(True)
    elif upC == len(word):
        print(True)
    elif upC == 1 and word[0].isupper():
        print(True)
    else:
        print(False)


def stu_on():
    s = "PPALLL"
    a = 0
    l = 0

    for i in range(len(s)):
        if s[i] == 'A':
            a += 1
        if s[i] == 'L':
            l += 1
        elif s[i] != 'L' and l != 0 and l < 3:
            l = 0

    if a < 2 and l < 3:
        print(True)
    else:
        print(False)


def rev_word():
    s = "Mr Ding"
    list_s = s.split(' ')
    list_r = []

    for i in list_s:
        str_r = ''
        for j in range(len(i) - 1, -1, -1):
            str_r += i[j]
        list_r.append(str_r)
    s_r = ' '.join(list_r)
    print(s_r)


def split_candy():
    candyType = [6, 6, 6, 6]
    candyNum = len(set(candyType))

    if (len(candyType) / 2) < candyNum:
        print(int(len(candyType) / 2))
    elif (len(candyType) / 2) >= candyNum:
        print(candyNum)


def most_same_least_index():
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    indexDict = {}
    res = []

    tmp = list(set(list1) & set(list2))

    for i in tmp:
        indexDict[i] = list1.index(i) + list2.index(i)
    print(indexDict)
    indexList = sorted(indexDict.items(), key=lambda x: x[1])
    print(indexList)
    minV = indexDict[indexList[0][0]]

    for i, j in indexDict.items():
        if j == minV and i not in res:
            res.append(i)
    print(res)


def sub_str_avg():
    nums = [-1]
    k = 1

    w_sum = sum(nums[0:k])
    avg = w_sum / k

    for i in range(k, len(nums)):
        w_sum -= nums[i - k]
        w_sum += nums[i]
        avg = max(avg, w_sum / k)

    print(avg)


def list_lost_num():
    nums = [1, 3, 3]
    list_sum = sum(nums)
    set_sum = sum(set(nums))
    dup_num = list_sum - set_sum
    tmp = 0

    for i in range(1, len(nums) + 1):
        tmp += i

    res = [dup_num, tmp - set_sum]

    print(res)


def list_ele_num_same():
    moves = "UD"
    uC = 0
    dC = 0
    lC = 0
    rC = 0

    for i in moves:
        if i == 'U':
            uC += 1
        elif i == 'D':
            dC += 1
        elif i == 'L':
            lC += 1
        elif i == 'R':
            rC += 1
    if uC == dC and lC == rC:
        print(True)
    else:
        print(False)


def conti_asec_sub_list():
    nums = [1, 3, 5, 7]
    length = 1
    res = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 0:
            length += 1
            if i == (len(nums) - 2):
                if length >= res:
                    res = length
        elif nums[i + 1] - nums[i] <= 0:
            if length >= res:
                res = length
            length = 1
    print(res)


def two_div():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            print(mid)
            break
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(-1)


def turn_to_lower():
    s = "Hello"
    res = ''

    for i in s:
        if i.isupper():
            res += i.lower()
        else:
            res += i
    print(res)


def self_div():
    left = 47
    right = 85
    list01 = []
    res = []
    div = False

    for i in range(left, right + 1):
        list01.append(i)

    for i in list01:
        for j in range(len(str(i))):
            if int(str(i)[j]) == 0:
                div = False
                break
            if i % int(str(i)[j]) == 0:
                div = True
            else:
                div = False
                break
        if div == True:
            res.append(i)
    print(res)


def small_char():
    letters = ["x", "x", "y", "y"]
    target = "z"

    list01 = []
    index = 0

    for i in letters:
        list01.append(ord(i))
    for i in range(len(list01)):
        if list01[i] > ord(target):
            index = i
            break
    print(letters[index])


def twice_other_num():
    nums = [1, 2, 16, 35, 44, 100, 27, 0]
    maxNum = sorted(nums, reverse=True)[0]
    nums_tmp = []
    for i in nums:
        if i != 0 and i != maxNum:
            nums_tmp.append(i)
    mark = False

    if len(nums_tmp) == 0:
        print(nums.index(maxNum))

    for i in nums_tmp:
        tmpRes = maxNum / i
        if tmpRes >= 2:
            mark = True
        else:
            mark = False
            break

    if mark == True:
        print(nums.index(maxNum))
    else:
        print(-1)


def how_many_jewels():
    jewels = "z"
    stones = "ZZ"
    c = 0

    for i in stones:
        if i in jewels:
            c += 1
    print(c)


def rotate_str():
    s = "abcde"
    goal = "cdeab"

    for i in range(len(s)):
        s = s[1:len(s)] + s[0]
        if s == goal:
            print(True)
            break
        if i == (len(s) - 1) and s != goal:
            print(False)
            break


def mos_code():
    mos = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
           ".--.",
           "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    dict_mos = {}

    first = 97
    i = 0
    while True:
        dict_mos[chr(first)] = mos[i]
        first += 1
        i += 1
        if i == len(mos):
            break
    words = ["a"]
    res = []

    for word in words:
        str01 = ''
        for i in word:
            str01 += dict_mos[i]
        res.append(str01)
    print(len(set(res)))


def most_row():
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "abcdefghijklmnopqrstuvwxyz"

    first = 97
    dict_widths = {}
    j = 0
    for i in range(first, first + 26):
        dict_widths[chr(i)] = widths[j]
        j += 1
    # print(dict_widths)

    length = 0
    row = 1

    for i in s:
        length += dict_widths[i]
        if length <= 100:
            continue
        else:
            length = 0
            row += 1
            length = dict_widths[i]
    print(row, length)


def sec_appear_word():
    paragraph = "a."
    banned = []

    dots = ',.:;!?\''
    for i in dots:
        paragraph = paragraph.replace(i, ' ')
    paragraph = paragraph.lower()
    para_list = paragraph.split(' ')
    dict_para = {}
    for i in para_list:
        if i == '':
            continue
        if i not in dict_para.keys():
            dict_para[i] = 1
        else:
            dict_para[i] += 1
    times_list = sorted(dict_para.items(), key=lambda x: x[1], reverse=True)

    for i in times_list:
        if i[0] not in banned:
            print(i[0])
            break


def goat_latin():
    m = ['a', 'e', 'i', 'o', 'u']
    sentence = "The quick brown fox jumped over the lazy dog"
    sentence = sentence.split(' ')
    res = ''

    for i in range(len(sentence)):
        if sentence[i][0].lower() in m:
            sentence[i] += 'ma'
        else:
            sentence[i] = sentence[i][1:len(sentence[i])] + sentence[i][0]
            sentence[i] += 'ma'
        sentence[i] += 'a' * (i + 1)
        res = ' '.join(sentence)
    print(res)


def rev_list_twice():
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    tmp = []

    for i in image:
        sub = []
        for j in range(len(i) - 1, -1, -1):
            if i[j] == 1:
                sub.append(0)
            else:
                sub.append(1)
            # sub.append(i[j])
        tmp.append(sub)
    print(tmp)


def str_back():
    s = "y#fo##f"
    t = "y#f#o##f"
    list_s = []
    list_t = []

    for i in s:
        if i == '#' and list_s != []:
            list_s.pop()
        elif i != '#':
            list_s.append(i)

    for i in t:
        if i == '#' and list_t != []:
            list_t.pop()
        elif i != '#':
            list_t.append(i)

    if list_s == list_t:
        print(True)
    else:
        print(False)


def lemon_exchange():
    bills = [5, 5, 5]
    dict01 = {
        5: 0,
        10: 0,
        20: 0
    }

    for i in bills:
        if i == 5:
            dict01[5] += 1
        elif i == 10:
            if dict01[5] >= 1:
                dict01[5] -= 1
                dict01[10] += 1
            else:
                print(False)
                break
        elif i == 20:
            if 1 <= dict01[5] and dict01[10] >= 1:
                dict01[5] -= 1
                dict01[10] -= 1
                dict01[20] += 1
            elif dict01[5] >= 3:
                dict01[5] -= 3
                dict01[20] += 1
            else:
                print(False)
                break
    print(True)


def bin_two_dis():
    n = 8
    binV = bin(n)[2:]
    list01 = []
    list02 = []

    for i in range(len(str(binV))):
        if str(binV)[i] == '1':
            list01.append(i)

    if len(list01) == 1:
        print(0)

    for j in range(len(list01) - 1, 0, -1):
        list02.append(list01[j] - list01[j - 1])
    list02.sort(reverse=True)
    print(list02[0])


def only_once_word():
    s1 = "apple apple"
    s2 = "banana"
    dict01 = {}
    dict02 = {}
    list01 = s1.split(' ')
    list02 = s2.split(' ')
    res = []

    for i in list01:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    for i in list02:
        if i not in dict02.keys():
            dict02[i] = 1
        else:
            dict02[i] += 1

    for i, j in dict01.items():
        if j == 1:
            if i not in dict02.keys():
                res.append(i)

    for i, j in dict02.items():
        if j == 1:
            if i not in dict01.keys():
                res.append(i)

    print(res)


def one_way_list():
    nums = [1, 3, 2]

    if nums[0] < nums[len(nums) - 1]:
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                print(False)
                break
        print(True)
    elif nums[0] > nums[len(nums) - 1]:
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                continue
            else:
                print(False)
                break
        print(True)
    elif nums[0] == nums[len(nums) - 1]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            else:
                print(False)
                break
        print(True)


def odd_even_list():
    nums = [0]
    nums01 = []
    nums02 = []
    res = []

    for i in nums:
        if i % 2 == 0:
            nums01.append(i)
        else:
            nums02.append(i)
    res = nums01 + nums02
    print(res)


def list_ele_count_same():
    deck = [1, 1, 2, 2, 2, 2]
    # 统计列表元素，形成字典
    count = collections.Counter(deck)
    n = len(deck)
    for x in range(2, n + 1):
        # 每一组的牌数
        if n % x == 0:
            # 一共多少组
            if all(v % x == 0 for v in count.values()):
                return True
    return False


def rev_str_with_dot():
    s = "Test1ng-Leet=code-Q!"

    list_s = []
    list_n = []
    for i in s:
        list_n.append(i)
        if i.isalpha():
            list_s.append(i)
    list_s.reverse()

    for i in range(len(list_n)):
        if not list_n[i].isalpha():
            list_s.insert(i, list_n[i])
    res = ''.join(list_s)
    print(res)


def odd_even_sort():
    nums = [2, 3]
    num_one = []
    num_two = []
    nums.sort()
    num_res = []

    for i in nums:
        if i % 2 == 0:
            num_two.append(i)
        else:
            num_one.append(i)

    for i in range(len(nums)):
        num_res.append(0)

    o = 0
    t = 0

    for i in range(len(num_res)):
        if i % 2 == 0:
            num_res[i] = num_two[t]
            t += 1
        else:
            num_res[i] = num_one[o]
            o += 1
    print(num_res)


def ava_email():
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    res = []

    for i in range(len(emails)):
        pre = emails[i].split('@')[0]
        suf = emails[i].split('@')[1]
        pre = pre.replace('.', '')
        if '+' in pre:
            pre = pre.split('+')[0]
        emails[i] = pre + '@' + suf
    print(len(set(emails)))


def rev_bin_sort():
    n = 100101
    n = str(n)
    n = n[::-1]
    res = int(n, 2)
    print(res)


def list_bin_one_count():
    n = 5
    res = []

    for i in range(n + 1):
        binV = bin(i)[2:]
        binV = str(binV)
        oc = 0
        for i in binV:
            if '1' in i:
                oc += 1
        res.append(oc)
    print(res)


def three_square():
    n = 6

    if n == 0:
        print(False)

    if n == 1:
        print(True)

    while True:
        n = n / 3
        if n == 3:
            print(True)
            break
        if n % 3 != 0:
            print(False)
            break


def two_square():
    n = 4

    if n == 0:
        print(False)

    if n == 1:
        print(True)

    while True:
        if n == 2:
            print(True)
            break
        n = n / 2
        if n % 2 != 0:
            print(False)
            break


def four_square():
    n = 1

    if n == 0:
        print(False)
    if n == 1:
        print(True)

    while True:
        if n == 4:
            print(True)
            break
        n = n / 4
        if n % 4 != 0:
            print(False)
            break


def cont_sub_str():
    s = "abab"
    t = s + s
    t = t[1: len(t) - 1]
    if s in t:
        print(True)
    else:
        print(False)


def list_period():
    nums = [0, 2, 3, 4, 6, 8, 9]
    list_res = []
    c = 0

    if len(nums) == 1:
        list_res.append(str(nums[0]))
        print(list_res)

    nums = nums + [0]
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            c += 1
            continue
        if nums[i] + 1 != nums[i + 1]:
            if c == 0:
                list_res.append(str(nums[i]))
            else:
                list_res.append(str(nums[i - c]) + '->' + str(nums[i]))
            c = 0
    print(list_res)


def two_word_same_char():
    s = "anagram"
    t = "nagaram"
    dict_s = collections.Counter(s)
    dict_t = {}

    for i in t:
        if i not in dict_t.keys():
            dict_t[i] = 1
        else:
            dict_t[i] += 1
    if dict_s == dict_t:
        print(True)
    else:
        print(False)


def int_bin_rev_int():
    num = 5
    bin_s = bin(num)[2:]
    list_s = []

    for i in str(bin_s):
        if i == '1':
            list_s.append('0')
        elif i == '0':
            list_s.append('1')
    bin_n = ''.join(list_s)
    res = int(bin_n, 2)
    print(res)


def bin_one_zero():
    n = 11
    bin_a = bin(n)[2:]

    for i in range(len(str(bin_a)) - 1):
        if str(bin_a)[i] == str(bin_a)[i + 1]:
            print(False)
            break
    print(True)


def up_down_list():
    arr = [0, 3, 2, 1]
    up = False
    down = False

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            print(False)
            break
        if arr[i] < arr[i + 1]:
            up = True
            if down == True:
                print(False)
                break
        elif arr[i] > arr[i + 1]:
            down = True

    if up == True and down == True:
        print(True)
    else:
        print(False)


def make_of_str():
    s = "DDI"
    list01 = []
    list02 = []

    for i in range(len(s) + 1):
        list01.append(i)
    for i in range(len(s)):
        if s[i] == 'I':
            list02.append(list01[0])
            list01.pop(0)
        elif s[i] == 'D':
            list02.append(list01[len(list01) - 1])
            list01.pop()
    list02.append(list01[0])

    print(list02)


def reformat_list():
    strs = ["a", "b"]
    list01 = []

    for i in range(len(strs)):
        for j in range(len(strs[i])):
            if len(list01) == len(strs[i]):
                list01[j] = list01[j] + strs[i][j]
            else:
                list01.append(strs[i][j])
    res = 0
    tmp = False

    for i in range(len(list01)):
        for j in range(len(list01[i]) - 1):
            if ord(list01[i][j]) <= ord(list01[i][j + 1]):
                tmp = True
            else:
                tmp = False
                break
        if tmp == True:
            res += 1
    res = len(list01) - res
    print(res)


def n_ele_in_2n():
    nums = [5, 1, 5, 2, 5, 3, 5, 4]
    dict01 = {}
    for i in nums:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1
    for i, j in dict01.items():
        if j == len(nums) / 2:
            print(i)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    cc = 1

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            target = nums[i]
            cc += 1
            if cc == (len(nums) / 2):
                print(target)
                break
        else:
            cc = 1


def list_ele_square():
    nums = [-4, -1, 0, 3, 10]
    start = 0
    end = len(nums) - 1
    k = len(nums) - 1
    res = [0] * len(nums)

    while start <= end:
        if nums[start] ** 2 > nums[end] ** 2:
            res[k] = nums[start] ** 2
            start += 1
            k -= 1
        else:
            res[k] = nums[end] ** 2
            end -= 1
            k -= 1
    print(res)

    res01 = []

    for i in nums:
        res01.append(i * i)
    for i in range(len(res01)):
        for j in range(i + 1, len(res01)):
            if res01[i] > res01[j]:
                res01[i], res01[j] = res01[j], res01[i]
    print(res01)


def list_ele_add_list():
    num = [1, 2, 0, 0]
    k = 34
    tmp = 0
    num.reverse()

    for i in range(len(num)):
        tmp += num[i] * (10 ** i)
    tmp += k

    res = []

    for i in str(tmp):
        res.append(int(i))
    print(res)


def list_com_ele():
    words = ["bella", "label", "roller"]
    tmp = collections.Counter(words[0])

    for i in range(len(words)):
        tmp = tmp & collections.Counter(words[i])

    res = []
    for i, j in tmp.items():
        for k in range(j):
            res.append(i)
    print(res)


def list_rev_ele_max():
    nums = [2, -3, -1, 5, -4]
    k = 2

    for i in range(k):
        nums.sort()
        nums[0] = -nums[0]
    sum01 = 0

    for i in nums:
        sum01 += i
    print(sum01)


def bin_rev_value():
    n = 5
    bV = bin(n)[2:]
    tmp = ''

    for i in bV:
        if i == '1':
            tmp += '0'
        elif i == '0':
            tmp += '1'
    print(int(tmp, 2))


def list_len_sum_three_part():
    arr = [0, 0, 0, 0]
    sum01 = 0
    for i in arr:
        sum01 += i
    if sum01 % 3 != 0:
        print(False)

    tarSum = int(sum01 / 3)
    tmp = 0
    c = 0

    for i in range(len(arr)):
        tmp += arr[i]
        if tmp == tarSum:
            tmp = 0
            c += 1
        if tmp == 0 and c == 3:
            print(True)
    print(False)


def bin_list_five_div():
    nums = [0, 1, 1, 1, 1, 1]
    res = []

    for i in range(len(nums)):
        str01 = ''
        for j in range(0, i + 1):
            str01 += str(nums[j])
        if int(str01, 2) % 5 == 0:
            res.append(True)
        else:
            res.append(False)
    print(res)


def last_ele_list():
    stones = [10, 4, 2, 10]
    stones.sort()

    for i in range(len(stones) - 1, -1, -1):
        stones.sort()
        if len(stones) == 1:
            print(stones[0])
            break
        elif len(stones) == 0:
            print(0)
            break
        if i >= len(stones):
            i -= 1
            continue
        if stones[i] == stones[i - 1]:
            stones.pop(i)
            stones.pop(i - 1)
        else:
            stones[i - 1] = stones[i] - stones[i - 1]
            stones.pop(i)


def rm_dup_ele_str():
    s = "abbaca"
    dup = 0

    while True:
        if len(s) == 0:
            print('')
            break
        if len(s) == 1:
            print(s[0])
            break
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dup = 1
                s = s.replace(s[i] + s[i + 1], '')
                break
            else:
                dup = 0
        if dup == 0:
            break
    print(s)

    res = []
    resStr = ''

    for i in range(len(s)):
        if len(res) >= 1:
            if s[i] == res[-1]:
                res.pop()
                continue
        res.append(s[i])
    resStr = ''.join(res)
    print(resStr)


def dif_ele_after_sort_list():
    heights = [1, 1, 4, 2, 1, 3]
    tmp = heights.copy()
    tmp.sort()

    c = 0

    for i in range(len(tmp)):
        if tmp[i] != heights[i]:
            c += 1
    print(c)


def cont_two_next_word():
    text = "we will we will rock you"
    first = "we"
    second = "will"
    text = text.split(' ')
    res = []

    for i in range(len(text) - 1):
        if i == (len(text) - 2):
            break
        if text[i] == first and text[i + 1] == second:
            res.append(text[i + 2])
    print(res)


def rep_zero_in_list():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    l = len(arr)
    i = 0

    while i < l:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 2
        else:
            i += 1
    print(arr)

    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         listN.append(arr[i])
    #     else:
    #         listN.append(0)
    #         listN.append(0)
    #     if len(listN) == len(arr):
    #         break
    # arr = listN
    # print(arr)


def asc_list_ele():
    candies = 7
    num_people = 4
    res = []
    for i in range(num_people):
        res.append(0)
    i = 0
    v = 1
    s = 0

    while s < candies:
        if candies - s >= v:
            res[i] += v
            i += 1
            s += v
            v += 1
        else:
            res[i] += candies - s
            break
        if i > len(res) - 1:
            i = 0
    print(res)


def replace_dot_in_ip():
    address = "1.1.1.1"
    tmp = address.split('.')
    res = '[.]'.join(tmp)
    print(res)

    resStr = ''

    for i in address:
        if i == '.':
            resStr += '[.]'
        else:
            resStr += i
    print(resStr)

    address = address.replace('.', '[.]')
    print(address)


def sort_two_list():
    arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    arr2 = [2, 42, 38, 0, 43, 21]
    dict01 = {}
    l = len(arr2)
    j = 0
    res = []

    for i in arr1:
        if i in arr2:
            if i not in dict01.keys():
                dict01[i] = 1
            else:
                dict01[i] += 1

    while j < l:
        res.append(arr2[j])
        dict01[arr2[j]] -= 1
        if dict01[arr2[j]] == 0:
            j += 1
    print(res)

    tmp = []

    for i in arr1:
        if i not in arr2:
            tmp.append(i)
    tmp.sort()
    res = res + tmp
    print(res)


def dup_list_ele():
    dominoes = [[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]
    dict01 = {}

    for i in range(len(dominoes)):
        dominoes[i].sort()
        dominoes[i] = [str(i) for i in dominoes[i]]
        l = ''.join(dominoes[i])
        if l not in dict01.keys():
            dict01[l] = 1
        else:
            dict01[l] += 1
    print(dict01)

    res = 0

    for i in dict01.values():
        for j in range(0, i):
            res += j
    print(res)


def new_fib_num():
    n = 31
    if n == 0:
        print(0)
    if n == 1:
        print(1)
    if n == 2:
        print(1)
    a = 0
    b = 1
    c = 1
    for i in range(2, n):
        a, b, c = b, c, a + b + c
    print(c)

    def sub_new_fib_num(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return sub_new_fib_num(n - 3) + sub_new_fib_num(n - 2) + sub_new_fib_num(n - 1)

    print(sub_new_fib_num(n))


def day_in_year():
    date = "1900-05-02"
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    if month.startswith('0'):
        month = int(month[1:2])
    else:
        month = int(month)
    if day.startswith('0'):
        day = int(day[1:2])
    else:
        day = int(day)
    res = 0

    for i in range(len(days)):
        if i == (month - 1):
            break
        res += days[i]
        if (year[2:4] == '00' and int(year) % 400 == 0) or (year[2:4] != '00' and int(year) % 4 == 0):
            if i == 1:
                res += 1
    res += day
    print(res)


def words_char():
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    res = 0

    for i in range(len(words)):
        t = chars
        label = True
        for j in words[i]:
            if j in t:
                t = t.replace(j, '', 1)
            else:
                label = False
                break
        if label == True:
            res += len(words[i])
    print(res)


def join_words():
    text = "nlaebolko"
    tar = 'balloon'
    s = ''
    r = 0

    while True:
        for i in tar:
            if i in text:
                s += i
                text = text.replace(i, '', 1)
        if s == tar:
            s = ''
            r += 1
        else:
            break
        list01 = list(set(text) & set(tar))
        if list01 == []:
            break
    print(r)


def min_abs_dist():
    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    res = []
    m = abs(arr[0] - arr[1])

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) <= m:
                m = abs(arr[i] - arr[j])

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == m:
                res.append([arr[i], arr[j]])

    for i in res:
        i.sort()
    res.sort()
    print(res)

    arr.sort()
    res01 = []
    mm = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) <= m:
            mm = abs(arr[i] - arr[i + 1])

    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) == m:
            if arr[i] > arr[i + 1]:
                res01.append([arr[i + 1], arr[i]])
            else:
                res01.append([arr[i], arr[i + 1]])
    res01.sort()
    print(res01)


def list_ele_count_only_one():
    arr = [1, 2, 2, 1, 1, 3]
    dict01 = {}

    for i in arr:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    listV = dict01.values()
    listVS = set(listV)

    if len(listV) == len(listVS):
        print(True)
    else:
        print(False)


def odd_even_less():
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30]
    odd = 0
    even = 0

    for i in position:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd > even:
        print(even)
    elif odd < even:
        print(odd)
    else:
        print(odd)


def how_many_balance_str():
    s = "LLLLRRRR"
    t = 0
    r = 0

    for i in s:
        if i == 'L':
            t += 1
        if i == 'R':
            t -= 1
        if t == 0:
            r += 1
    print(r)


def rotate_list_list():
    grid = [[1], [2], [3], [4], [7], [6], [5]]
    k = 23
    t = []

    for i in grid:
        for j in i:
            t.append(j)

    if k > len(t):
        k = k % len(t)
    r = t[len(t) - k:len(t)] + t[0:len(t) - k]
    res = []
    resIn = []
    la = len(grid)
    li = len(grid[0])
    print(r)

    for i in r:
        resIn.append(int(i))
        if len(resIn) == li:
            res.append(resIn)
            resIn = []
    print(res)


def plus_multi_dist():
    n = 234
    multi = 1
    plus = 0

    for i in str(n):
        multi *= int(i)
        plus += int(i)
    res = multi - plus
    print(res)


def ele_in_list_appear_25_percent():
    arr = [1, 2, 3, 3]
    dict01 = {}

    for i in arr:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    for i, j in dict01.items():
        if j > len(arr) / 4:
            print(i)


def list_ele_count_even():
    nums = [12, 345, 2, 6, 7896]
    even = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            even += 1
    print(even)


def replace_ele_right_max():
    arr = [17, 18, 5, 4, 6, 1]

    # for i in range(len(arr)):
    #     m = -1
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] > m:
    #             m = arr[j]
    #     arr[i] = m
    # print(arr)

    res = [-1] * len(arr)

    for i in range(len(res) - 2, -1, -1):
        if res[i + 1] < arr[i + 1]:
            res[i] = arr[i + 1]
        else:
            res[i] = res[i + 1]
    print(res)


def list_ele_sum_zero():
    n = 5
    res = []
    t = 1

    if n % 2 == 0:
        res = []
        for i in range(int(n / 2)):
            p = 0 - t
            if t and p not in res:
                res.append(t)
                res.append(p)
            t += 1
    else:
        res.append(0)
        for i in range(int((n - 1) / 2)):
            p = 0 - t
            if t and p not in res:
                res.append(t)
                res.append(p)
            t += 1
    print(res)


def nums_to_char():
    s = "10#11#12"
    dict01 = {}
    s1 = 1
    r = ''

    for i in range(97, 97 + 26):
        dict01[str(s1)] = chr(i)
        s1 += 1

    l = len(s)
    i = l - 1

    while i >= 0:
        if s[i] == '#':
            t = str(s[i - 2]) + str(s[i - 1])
            r += dict01[t]
            i -= 3
        else:
            r += dict01[s[i]]
            i -= 1
    print(r[::-1])


def create_list_with_ele_in_list():
    nums = [65, 44, 72, 15]
    res = []
    i = 0

    while i < len(nums) - 1:
        if i % 2 == 0:
            c = nums[i]
            n = nums[i + 1]
        for j in range(c):
            res.append(n)
        i += 2
    print(res)


def sub_num_without_zero():
    n = 11
    s = 1
    p = n - s

    while True:
        if str(s).find('0') != -1 or str(p).find('0') != -1:
            s += 1
            p -= 1
        if str(s).find('0') == -1 and str(p).find('0') == -1:
            break

    print([s, p])


def six_nine_max_num():
    num = 9996
    t = list(str(num))

    for i in range(len(t)):
        if t[i] == '9':
            continue
        if t[i] == '6':
            t[i] = '9'
            break
    print(int(''.join(t)))


def list_ele_num_in_sorted():
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    t = arr.copy()
    t = list(set(t))
    t.sort()
    dict01 = {}

    for i in range(len(t)):
        dict01[t[i]] = i + 1

    for i in range(len(arr)):
        arr[i] = dict01[arr[i]]
    print(arr)


def dict_sort():
    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]]
    k = 2
    dict01 = {}

    for i in range(len(mat)):
        o = 0
        for j in mat[i]:
            if j == 1:
                o += 1
        dict01[i] = o

    list01 = sorted(dict01.items(), key=lambda x: x[1])
    res = []

    for i in range(k):
        res.append(list01[i][0])
    print(res)


def num_trans_to_zero():
    num = 123
    t = 0

    while num > 0:
        if num % 2 == 0:
            num = num / 2
            t += 1
        if num % 2 != 0:
            num -= 1
            t += 1
    print(t)


def double_ele_in_list():
    arr = [3, 1, 7, 11]
    arr.sort()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] / 2:
                print(True)
                break
            if arr[i] == arr[j] * 2:
                print(True)
                break
    print(False)


def less_zero_num_in_list():
    grid = [[3, 2], [1, 0]]
    c = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                c += len(grid[i]) - j
                break
    print(c)


def bin_one_num_sort():
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    arr = [10, 100, 1000, 10000]
    dict01 = {}

    for i in arr:
        b = bin(i)[2:]
        c = 0
        for j in str(b):
            if j == '1':
                c += 1
        if c not in dict01.keys():
            dict01[c] = [i]
        else:
            dict01[c] += [i]

    list01 = sorted(dict01.items(), key=lambda x: x[0])

    res = []
    for i in list01:
        i[1].sort()
        for j in i[1]:
            res.append(j)
    print(res)


def less_ele_list():
    nums = [7, 7, 7, 7]
    dict01 = {}
    t = nums.copy()
    t.sort()
    res = []

    for i in range(len(t)):
        if t[i] not in dict01.keys():
            dict01[t[i]] = i

    for i in range(len(nums)):
        if nums[i] in dict01.keys():
            res.append(dict01[nums[i]])
    print(res)


def reformat_list_ord():
    s = "aaaabbbbcccc"
    ls = list(s)
    res = ''

    while len(ls) > 0:
        t = ''
        ls.sort(reverse=True)
        for i in range(len(ls) - 1, -1, -1):
            if t == '':
                t += ls[i]
                ls.pop(i)
            else:
                if ord(ls[i]) > ord(t[len(t) - 1:len(t)]):
                    t += ls[i]
                    ls.pop(i)
        res += t
        t = ''
        ls.sort()
        for j in range(len(ls) - 1, -1, -1):
            if t == '':
                t += ls[j]
                ls.pop(j)
            else:
                if ord(ls[j]) < ord(t[len(t) - 1:len(t)]):
                    t += ls[j]
                    ls.pop(j)
        res += t
    print(res)


def char_str_odd_times():
    n = 4
    res = ''

    if n % 2 == 0:
        res = 'a' * (n - 1) + 'b'
    else:
        res = 'a' * n

    print(res)


def row_col_max():
    matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    rotate = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(rotate) < len(matrix[0]):
                rotate.append([matrix[i][j]])
            else:
                rotate[j].append(matrix[i][j])
    rowM = []
    colM = []

    for i in range(len(matrix)):
        matrix[i].sort()
        rowM.append(matrix[i][0])

    for i in range(len(rotate)):
        rotate[i].sort(reverse=True)
        colM.append(rotate[i][0])

    res = list(set(rowM) & set(colM))
    print(res)


def list_and_list_dist():
    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]
    d = 6
    res = 0

    for i in range(len(arr1)):
        c = True
        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) <= d:
                c = False
        if c == True:
            res += 1
    print(res)


def create_new_list_by_two():
    nums = [1]
    index = [0]
    target = []

    for i in range(len(index)):
        target.insert(index[i], nums[i])
    print(target)


def value_count_same_ele_list():
    arr = [7, 7, 7, 7, 7, 7, 7]
    dict01 = {}

    for i in arr:
        if i not in dict01.keys():
            dict01[i] = 1
        else:
            dict01[i] += 1

    res = []

    for i, j in dict01.items():
        if i == j:
            res.append(i)

    if len(res) == 0:
        print(-1)
    else:
        res.sort(reverse=True)
        print(res[0])


def sub_num_plus():
    n = 24
    dict01 = {}

    for i in range(1, n + 1):
        s = 0
        for j in str(i):
            s += int(j)
        if s not in dict01.keys():
            dict01[s] = 1
        else:
            dict01[s] += 1
    list01 = sorted(dict01.items(), key=lambda x: x[1], reverse=True)
    c = 0
    tar = list01[0][1]

    for i in list01:
        if i[1] == tar:
            c += 1
    print(c)


def min_list_larger_than_rest():
    nums = [4, 4, 7, 6, 7]
    s = 0
    for i in nums:
        s += i

    nums.sort(reverse=True)

    t = 0
    res = []

    for i in range(len(nums)):
        if t > s - t:
            break
        else:
            t += nums[i]
            res.append(nums[i])
    print(res)


def str_sub_str_list():
    words = ["blue", "green", "bu"]
    res = []

    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                if words[j].find(words[i]) != -1:
                    if words[i] not in res:
                        res.append(words[i])
    print(res)


def outer_min_ele_plus_list():
    nums = [-3, 2, -3, 4, 2]
    sV = 0
    sMinV = 0

    for i in nums:
        sV += i
        sMinV = min(sV, sMinV)
    print(1 - sMinV)


def str_num_new_str():
    s = "a12bcd"
    list01 = []
    res = ''

    for i in s:
        if i.isdigit():
            list01.insert(0, i)
        if i.isalpha():
            list01.append(i)
    print(list01)

    start = 0
    end = len(list01) - 1

    while start <= end:
        if len(list01) == 1:
            print(list01[0])
            break
        if start == end:
            if list01[start].isalpha() and res[0].isalpha():
                res = res + list01[start]
            else:
                res = list01[start] + res
            break
        if start != end:
            if (list01[start].isalpha() and list01[end].isalpha()) or (
                    list01[start].isdigit() and list01[end].isdigit()):
                print('')
                break
            res = list01[start] + res
            res = list01[end] + res
            start += 1
            end -= 1
    print(res)


def sub_list_zero_one_count():
    s = "1111"
    list01 = list(s)
    start = 0
    end = len(list01) - 1
    res = []

    while start < end:
        listF = list01[0:start + 1]
        listB = list01[start + 1:len(list01)]
        listF = [i for i in listF if i == '0']
        listB = [i for i in listB if i == '1']
        countF = len(listF)
        countB = len(listB)
        countS = countF + countB
        res.append(countS)
        start += 1
    res.sort(reverse=True)
    print(res[0])


def tower_triangle():
    numRows = 1
    res = [[1]]

    for i in range(1, numRows):
        t = []
        for j in range(0, i + 1):
            if j == 0:
                t.append(res[i - 1][0])
            elif j == i:
                t.append(res[i - 1][len(res[i - 1]) - 1])
                break
            else:
                s01 = res[i - 1][j - 1] + res[i - 1][j]
                t.append(s01)
        res.append(t)
    print(res)


def tower_triangle_single():
    rowIndex = 3
    res = [[1]]

    for i in range(1, rowIndex + 1):
        t = []
        for j in range(0, i + 1):
            if j == 0:
                t.append(res[i - 1][0])
            elif j == i:
                t.append(res[i - 1][len(res[i - 1]) - 1])
            else:
                sum01 = res[i - 1][j - 1] + res[i - 1][j]
                t.append(sum01)
        res.append(t)
    r = res[len(res) - 1]
    print(r)


def same_struct_str():
    s = "paper"
    t = "title"
    dict01 = {}

    for i in range(len(s)):
        if s[i] not in dict01.keys():
            if t[i] not in dict01.values():
                dict01[s[i]] = t[i]
            elif t[i] in dict01.values():
                print(False)
                break
        elif s[i] in dict01.keys():
            if t[i] != dict01[s[i]]:
                print(False)
                break
    print(True)


def dup_ele_list():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    dict01 = {}

    for i in range(len(nums)):
        if nums[i] not in dict01.keys():
            dict01[nums[i]] = [i]
        else:
            dict01[nums[i]].append(i)

    for i, j in dict01.items():
        if len(j) >= 2:
            j.sort()
            for l in range(len(j) - 1):
                if abs(j[l] - j[l + 1]) <= k:
                    print(True)
                    break
                else:
                    continue
    print(False)


def num_build_in_ttf():
    n = 1

    if n == 0:
        print(False)

    while n % 2 == 0:
        n /= 2

    while n % 3 == 0:
        n /= 3

    while n % 5 == 0:
        n /= 5

    print(n == 1)


def same_struct_str_s():
    pattern = "abba"
    s = "dog dog dog dog"
    s = s.split(' ')
    dict01 = {}

    if len(pattern) != len(s):
        print(False)

    for i in range(len(pattern)):
        if pattern[i] not in dict01.keys():
            if s[i] in dict01.values():
                print(False)
            else:
                dict01[pattern[i]] = s[i]
        else:
            if s[i] != dict01[pattern[i]]:
                print(False)
                break
    print(True)


def rev_ao_ele_in_list():
    s = "leetcode"
    ao = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    list01 = []
    s = list(s)

    for i in range(len(s) - 1, -1, -1):
        if s[i] in ao:
            list01.append(s[i])
            s[i] = '$'

    for i in range(len(s)):
        if s[i] == '$':
            s[i] = list01[0]
            list01.pop(0)
    s = ''.join(s)
    print(s)


def two_list_sub_list():
    s = "ab"
    t = "baab"

    n = len(s)
    m = len(t)

    i = 0
    j = 0

    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    print(i == n)


def sub_list_contain_list():
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    g.sort()
    s.sort()

    i = 0
    j = 0

    n = len(g)
    m = len(s)
    c = 0

    while i < n and j < m:
        if i < n and s[j] < g[i]:
            j += 1
        elif s[j] >= g[i]:
            c += 1
            i += 1
            j += 1
    print(c)


def diff_char_in_bin():
    x = 3
    y = 1
    bx = bin(x)[2:]
    by = bin(y)[2:]

    if len(bx) < len(by):
        bx = (len(by) - len(bx)) * '0' + bx
    if len(bx) > len(by):
        by = (len(bx) - len(by)) * '0' + by

    c = 0
    for i in range(len(bx)):
        if bx[i] != by[i]:
            c += 1
    print(c)


def str_in_keyboard():
    s1 = set('qwertyuiop')
    s2 = set('asdfghjkl')
    s3 = set('zxcvbnm')
    r = []

    words = ["Hello", "Alaska", "Dad", "Peace"]

    for i in range(len(words)):
        seti = set(words[i].lower())
        if seti <= s1 or seti <= s2 or seti <= s3:
            r.append(words[i])
    print(r)


def num_sub_num_plus():
    num = 28
    r = []
    i = 1

    while i < math.sqrt(num):
        if num % i == 0:
            r.append(i)
            if i != 1:
                r.append(int(num / i))
        i += 1
    s = 0

    for i in r:
        s += i
    print(s == num)


def sp_sub_list_in_two_list():
    a = "aba"
    b = "cdc"

    if a == b:
        print(-1)

    if len(a) == len(b):
        print(len(a))
    if len(a) > len(b):
        print(len(a))
    if len(a) < len(b):
        print(len(b))


def gen_list_with_char():
    # 整数x - 表示本回合新获得分数
    # "+" - 表示本回合新获得的得分是前两次得分的总和。
    # "D" - 表示本回合新获得的得分是前一次得分的两倍。
    # "C" - 表示前一次得分无效，将其从记录中移除。
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    res = []

    for i in range(len(ops)):
        if ops[i] not in ["C", "D", "+"]:
            res.append(ops[i])
        if ops[i] == 'C':
            res.pop()
        if ops[i] == 'D':
            res.append(int(res[len(res) - 1]) * 2)
        if ops[i] == '+':
            res.append(int(res[len(res) - 1]) + int(res[len(res) - 2]))
    s = 0
    for i in res:
        s += int(i)
    print(s)


def bit_one_two_char():
    bits = [0, 0]
    # bits = [1, 0, 0]
    # bits = [1, 1, 1, 0]
    bits = [0, 1, 0]

    i = 0
    while i <= (len(bits) - 1):
        if bits[i] == 0 and i == (len(bits) - 1):
            print(True)
            break
        if bits[i] == 0 and bits[i + 1] == 0:
            i += 1
            continue
        if bits[i] == 0 and bits[i + 1] == 1:
            i += 1
            continue
        if bits[i] == 1 and i == (len(bits) - 1):
            print(False)
            break
        if bits[i] == 1 and bits[i + 1] in [1, 0]:
            i += 2
            continue
    print(False)


def mid_index_in_list():
    nums = [2, 1, -1]

    i = -1
    end = len(nums) - 1

    while i < end:
        s1 = 0
        s2 = 0
        # for j in nums[0:i + 1]:
        #     s1 += j
        s1 = sum(nums[0:i + 1])
        # for k in nums[i + 2:len(nums)]:
        #     s2 += k
        s2 = sum(nums[i + 2:len(nums)])
        if s1 == s2:
            print(i + 1)
            break
        i += 1
    print(-1)


def min_full_word():
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    dict01 = {}

    for i in licensePlate:
        i = i.lower()
        if i.isalpha():
            if i not in dict01.keys():
                dict01[i] = 1
            else:
                dict01[i] += 1
    res = ''

    for i in range(len(words)):
        dict02 = {}

        for j in words[i]:
            if j not in dict02.keys():
                dict02[j] = 1
            else:
                dict02[j] += 1

        label = True

        for n, m in dict01.items():
            if n not in dict02.keys():
                label = False
                break
            else:
                if m > dict02[n]:
                    label = False
                    break
                else:
                    label = True
        if label == True:
            if res == '':
                res = words[i]
            else:
                if len(words[i]) < len(res):
                    res = words[i]
    print(res)


def pri_num_in_list():
    left = 10
    right = 15
    r = 0
    pn = [2, 3, 5, 7, 11, 13, 17, 19]

    for i in range(left, right + 1):
        b = bin(i)[2:]
        t = 0
        for j in b:
            if j == '1':
                t += int(j)
        if t in pn:
            r += 1
    print(r)


def slash_in_rectangle():
    matrix = [[1, 2], [2, 2]]
    lable = True

    for i in range(len(matrix) - 1):
        if matrix[i][0:len(matrix[i]) - 1] == matrix[i + 1][1:len(matrix[i + 1])]:
            continue
        else:
            lable = False
    print(lable)


def char_in_str_dist():
    s = "loveleetcode"
    c = "e"
    r = []
    t = []

    for i in range(len(s)):
        if s[i] == c:
            t.append(i)

    for i in range(len(s)):
        p = []
        for j in t:
            p.append(abs(i - j))
        p.sort()
        r.append(p[0])
    print(r)


def big_interval_in_list():
    s = "aaa"
    r = []

    l = 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if l >= 3:
                r.append([i + 1 - l, i])
            l = 1
        else:
            l += 1
        if i == len(s) - 2 and l >= 3:
            r.append([len(s) - l, len(s) - 1])
    print(r)


def rotate_rectangle():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    res = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(res) < len(matrix[0]):
                res.append([matrix[i][j]])
            else:
                res[j].append(matrix[i][j])
    print(res)


def long_press_char_in_word():
    name = "leelee"
    typed = "lleeelee"
    list01 = []
    list02 = []
    key01 = []
    key02 = []
    dict01 = {}
    dict02 = {}

    for i in name:
        if key01 == []:
            key01.append(i)
        else:
            if i != key01[len(key01) - 1]:
                key01.append(i)
    for i in typed:
        if key02 == []:
            key02.append(i)
        else:
            if i != key02[len(key02) - 1]:
                key02.append(i)

    if key01 != key02 or len(key01) != len(key02):
        print(False)

    for i in range(len(name)):
        if name[i] not in dict01.keys():
            if dict01 == {}:
                dict01[name[i]] = 1
            elif dict01 != {}:
                list01.append(list(dict01.values())[0])
                dict01 = {}
                dict01[name[i]] = 1
        else:
            dict01[name[i]] += 1
    list01 = list01 + list(dict01.values())

    for i in range(len(typed)):
        if typed[i] not in dict02.keys():
            if dict02 == {}:
                dict02[typed[i]] = 1
            elif dict02 != {}:
                list02.append(list(dict02.values())[0])
                dict02 = {}
                dict02[typed[i]] = 1
        else:
            dict02[typed[i]] += 1
    list02 = list02 + list(dict02.values())

    if len(list01) != len(list02):
        print(False)

    isP = True
    for i in range(len(list01)):
        if list01[i] <= list02[i]:
            continue
        else:
            isP = False
            break
    print(isP)


def list_plus_num():
    # sys.set_int_max_str_digits(10000000)
    num = [1, 2, 0, 0]
    k = 34

    t = ''

    for i in num:
        t += str(i)
    t = int(t) + k
    print([i for i in str(t)])


def sub_bracket():
    s = "()()"
    t = []
    l = 0
    r = ''

    for i in range(len(s)):
        if s[i] == '(':
            t.append(s[i])
            l += 1
        elif s[i] == ')':
            t.pop()
            l += 1
            if len(t) == 0:
                r += s[i - l + 2:i]
                l = 0
    print(r)


def after_plus_ele_max_in_list():
    candies = [12, 1, 12]
    extraCandies = 10
    t = candies.copy()
    t.sort(reverse=True)
    maxV = t[0]
    res = []

    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxV:
            res.append(True)
        else:
            res.append(False)
    print(res)


def remake_two_sub_list():
    paths = [["A", "Z"]]
    t = []

    for i in range(len(paths)):
        for j in range(len(paths[i])):
            if len(t) < len(paths[i]):
                t.append([paths[i][j]])
            else:
                t[j].append(paths[i][j])
    print(t)
    res = list(set(t[1]) - set(t[0]))[0]
    print(res)


if __name__ == '__main__':
    remake_two_sub_list()
    # after_plus_ele_max_in_list()
    # sub_bracket()
    # list_plus_num()
    # long_press_char_in_word()
    # rotate_rectangle()
    # big_interval_in_list()
    # char_in_str_dist()
    # slash_in_rectangle()
    # pri_num_in_list()
    # min_full_word()
    # mid_index_in_list()
    # bit_one_two_char()
    # gen_list_with_char()
    # sp_sub_list_in_two_list()
    # num_sub_num_plus()
    # str_in_keyboard()
    # diff_char_in_bin()
    # sub_list_contain_list()
    # two_list_sub_list()
    # rev_ao_ele_in_list()
    # same_struct_str_s()
    # num_build_in_ttf()
    # dup_ele_list()
    # same_struct_str()
    # tower_triangle()
    # tower_triangle_single()
    # sub_list_zero_one_count()
    # str_num_new_str()
    # outer_min_ele_plus_list()
    # str_sub_str_list()
    # min_list_larger_than_rest()
    # sub_num_plus()
    # value_count_same_ele_list()
    # create_new_list_by_two()
    # list_and_list_dist()
    # row_col_max()
    # char_str_odd_times()
    # reformat_list_ord()
    # less_ele_list()
    # bin_one_num_sort()
    # less_zero_num_in_list()
    # double_ele_in_list()
    # num_trans_to_zero()
    # dict_sort()
    # list_ele_num_in_sorted()
    # six_nine_max_num()
    # sub_num_without_zero()
    # create_list_with_ele_in_list()
    # nums_to_char()
    # list_ele_sum_zero()
    # replace_ele_right_max()
    # list_ele_count_even()
    # ele_in_list_appear_25_percent()
    # plus_multi_dist()
    # rotate_list_list()
    # how_many_balance_str()
    # odd_even_less()
    # list_ele_count_only_one()
    # min_abs_dist()
    # join_words()
    # words_char()
    # day_in_year()
    # new_fib_num()
    # dup_list_ele()
    # sort_two_list()
    # replace_dot_in_ip()
    # asc_list_ele()
    # rep_zero_in_list()
    # cont_two_next_word()
    # dif_ele_after_sort_list()
    # rm_dup_ele_str()
    # last_ele_list()
    # bin_list_five_div()
    # list_len_sum_three_part()
    # bin_rev_value()
    # list_rev_ele_max()
    # list_com_ele()
    # list_ele_add_list()
    # list_ele_square()
    # n_ele_in_2n()
    # reformat_list()
    # make_of_str()
    # up_down_list()
    # bin_one_zero()
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
    # most_same_least_index()
    # sub_str_avg()
    # list_lost_num()
    # conti_asec_sub_list()
    # two_div()
    # turn_to_lower()
    # self_div()
    # small_char()
    # twice_other_num()
    # how_many_jewels()
    # rotate_str()
    # mos_code()
    # most_row()
    # sec_appear_word()
    # goat_latin()
    # rev_list_twice()
    # str_back()
    # lemon_exchange()
    # bin_two_dis()
    # only_once_word()
    # one_way_list()
    # odd_even_list()
    # list_ele_count_same()
    # rev_str_with_dot()
    # odd_even_sort()
    # ava_email()
    # rev_bin_sort()
    # list_bin_one_count()
    # three_square()
    # two_square()
    # four_square()
    # cont_sub_str()
    # list_period()
    # two_word_same_char()
