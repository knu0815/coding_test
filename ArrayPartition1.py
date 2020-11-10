from typing import List


class ArrayPartitionOne:
    # Runtime: 268 ms
    # Memory: 16.8 MB
    @classmethod
    def sort_than_min(cls, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(int(len(nums) / 2)):
            sum += min(nums[2 * i], nums[2 * i + 1])
        return sum

    # Runtime: 248 ms
    # Memory: 16.8 MB
    @classmethod
    def sort_than_add_even(cls, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(int(len(nums) / 2)):
            sum += nums[2 * i]
        return sum

    # Runtime: 244 ms
    # Memory: 16.8 MB
    @classmethod
    def slicing(cls, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


def main():
    # Answer for number #1
    print(ArrayPartitionOne.my_solution([1, 4, 3, 2]))


if __name__ == "__main__":
    main()