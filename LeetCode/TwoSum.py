from typing import List

# URL:
# https://leetcode.com/problems/two-sum/

# Question:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


class TwoSum:
    # 5500ms, 15.1MBm, O(n^2)
    @classmethod
    def brute_force(cls, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 1052ms , 15MB, O(n^2)
    @classmethod
    def using_in(cls, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1 :]:
                return [i, nums[i + 1 :].index(target - nums[i]) + i + 1]

    @classmethod
    def invert_index(cls, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums):
            if target - num in index:
                return [index[num], i]
            else:
                index[num] = i


def main():
    # Answer for number #1
    print((TwoSum.invert_index([2, 7, 11, 15], 9)))


if __name__ == "__main__":
    main()