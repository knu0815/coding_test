from functools import reduce
from typing import List

# URL:
# https://leetcode.com/problems/product-of-array-except-self

# Question:
# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is
# equal to the product of all the elements of
# nums except nums[i].


class ProductOfArrayExceptSelf:
    @classmethod
    def my_solution(cls, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1]
        right = 1

        for i in range(1, len(nums)):
            answer.append(nums[i - 1] * answer[i - 1])

        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer


def main():
    # Answer for number #1
    print(ProductOfArrayExceptSelf.my_solution([1, 2, 3, 4]))


if __name__ == "__main__":
    main()