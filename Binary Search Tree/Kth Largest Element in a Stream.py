# _*_ coding: utf-8 _*_
"""
# @Time : 12/1/2021 9:15 PM
# @Author : byc
# @File : Kth Largest Element in a Stream.py
# @Description :
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]