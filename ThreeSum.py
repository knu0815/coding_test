from typing import List


class ThreeSum:
    @classmethod
    def two_pointer(cls, nums: List[int]) -> List[List[int]]:
        results = []
        if len(nums) < 3:
            return results
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                if sum > 0:
                    right -= 1
                if sum == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


def main():
    # Answer for number #1
    print(ThreeSum.two_pointer([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()