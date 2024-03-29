# _*_ coding: utf-8 _*_
"""
# @Time : 9/28/2021 7:19 PM
# @Author : byc
# @File : Plus One.py
# @Description :
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i]>= 10:
                digits[i] = 0
                if i > 0:
                    digits[i-1] += 1
                else:
                    digits.insert(0, 1)
        return digits