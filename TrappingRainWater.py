from typing import List


class TrappingRainWater:

    # Runtime: 56 ms
    # Memory: 14.8 MB
    @classmethod
    def two_pointer(cls, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    # Runtime: 56 ms
    # Memory:	14.6 MB
    @classmethod
    def stack(cls, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            stack.append(i)
        return volume


def main():
    # Answer for number #1
    TrappingRainWater.stack()


if __name__ == "__main__":
    main()