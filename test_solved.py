from  solved import *
import pytest


def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring('') == 0
    assert lengthOfLongestSubstring('abbcat') == 4
    assert lengthOfLongestSubstring('zzzatcat') == 4
    assert lengthOfLongestSubstring('pwwkew') == 3
    assert lengthOfLongestSubstring('pwkkkkw.kewababertyu') == 7
    assert lengthOfLongestSubstring('pwkkkkwkew') == 3
    assert lengthOfLongestSubstring('dvdf') == 3
    assert lengthOfLongestSubstring('abbcat') == 4

@pytest.mark.parametrize("nums, output",
[([1,2,45,2],48),
([2,22],24),
([1,5,6,1,2,4,6],18),
 ([4,2,4,5,6],17),
 ([4, 2, 4, 5, 6], 17)

 ])
def test_maximumUniqueSubarray(nums, output):
    assert maximumUniqueSubarray(nums) == output


# def test_maximumUniqueSubarray()