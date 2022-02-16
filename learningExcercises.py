"""
contains code that was used for learning purposes and may not be entirely my own
"""
from typing import List

from helperFunctions import *


def longestCommonSubstring(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    max_len = float('-inf')

    # col -> substring, row -> string
    dp = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]
    # dp[0][0] = 0

    for i in range(str1_len + 1):
        for j in range(str2_len + 1):
            if (i == 0 or j == 0):
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    printTable(dp)
    result = ''

    ndx1 = str1_len
    ndx2 = str2_len

    while ndx1 > 0 and ndx2 > 0:
        if str1[ndx1 - 1] == str2[ndx2 - 1]:
            result = str1[ndx1 - 1] + result
            ndx2 -= 1
            ndx1 -= 1
        elif dp[ndx1 - 1][ndx2] > dp[ndx1][ndx2 - 1]:
            ndx1 -= 1
        else:
            ndx2 -= 1

    print('result is \'' + result + "\'  and length of " + str(max_len))
    return result


def unboundedKnapsackReturnItems(maxWeight, weights, values):
    """
    :param maxWeight: maximum weight of bag
    :param weights: an ordered list of weights
    :param values: list of values associated with weight at corresponding index in weights
    :return: returns the maximum weight possible to put in that there bag
    """

    # initializing dp array with indexes from 0 to W
    dp = [0] * (maxWeight + 1)
    weightcounts = {}

    # going through each integer weight 0 to maxWeight
    for weightLimit in range(1, maxWeight + 1):

        for ndx in range(len(values)):
            weightOfItem = weights[ndx]
            if weightOfItem <= weightLimit:
                dp[weightLimit] = max(dp[weightLimit], dp[weightLimit - weightOfItem] + values[ndx])
                print(f" weight of item is {weightOfItem}")
                incrementKeyInDict(weightcounts, weightOfItem)

    return weightcounts


def incrementKeyInDict(dict, key, incAmount=1):
    if key in dict:
        dict[key] += incAmount;
    else:
        dict[key] = incAmount


def lengthOfLongestIncreasingSubsequence(nums) -> int:
    """
    space O(n), time O(n^2)
    https://www.youtube.com/watch?v=cjWnW0hdF1Y
    :param nums:
    :return:
    """
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):  # range params are start, stop, step
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)




            # 52132



