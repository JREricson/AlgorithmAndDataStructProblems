# def camelcase(s):
#     """
#     https://www.hackerrank.com/challenges/camelcase/
#     :param s:
#     :return:
#     """
#     count =1
#     for let in s:
#         if let.isupper():
#             count+ =1
#     return count
from typing import List


def pangrams(s):
    letters = {}  # char: 0 for char  in 'abcdfeghijklmnopqrstuvwxyz'
    for ch in s:
        ch_low = ch.lower()
        if ch_low.isalpha():
            if ch_low not in letters.keys():
                letters[ch_low] = 1
        if len(letters) == 26:
            return "pangram"

    return "not pangram"


##


def lengthOfLongestSubstring(s: str) -> int:
    """

    time O(n)
        -hashmap lookups O(1)
        -inner loop will run only loops through a total on n times with all calls from outer loop
    space(len(characterSet))

    :param s:
    :return:
    """
    ndx1, ndx2 = 0, 0
    len_s = len(s)
    letters = {}
    max_length = 0
    while ndx2 < len_s:
        if s[ndx2] not in letters:
            letters[s[ndx2]] = 1
            ndx2 += 1
            l = len(letters)
            if l > max_length:
                max_length = l
        else:
            while s[ndx1] != s[ndx2]:
                del letters[s[ndx1]]
                ndx1 += 1
            ndx1 += 1

            letters[s[ndx2]] = 1
            ndx2 += 1

    return max_length


def maximumUniqueSubarray(nums) -> int:
    ndx1, ndx2 = 0, 0
    max_sub = 0  # float('-inf') if want to include neg vals
    num_dict = {}

    while ndx2 < len(nums):
        if nums[ndx2] not in num_dict:
            num_dict[nums[ndx2]] = ndx2

            cur_tot = sum(nums[ndx1:ndx2 + 1])
            if cur_tot > max_sub:
                max_sub = cur_tot
        else:
            while ndx1 != num_dict[nums[ndx2]]:
                del num_dict[nums[ndx1]]
                ndx1 += 1
            num_dict[nums[ndx2]] = ndx2
            ndx1 += 1
        ndx2 += 1

    return max_sub
