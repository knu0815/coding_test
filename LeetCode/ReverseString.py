import math
# URL:
# https://leetcode.com/problems/reverse-string/

# Question:
# Write a function that reverses a string.
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.



class RevereString:
    @classmethod

    # Used two pointers in an inefficient way
    def mySoluion(cls, s:List[str]) -> None:
        for i in range(math.floor(len(s) / 2)):
            temp = s[i]
            s[i] = s[len(s) - i -1]
            s[len(s) - i -1] = temp

    # Two pointers in a more fashionable way
    @classmethod
    def twoPointers(cls, s:List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # The Pythonic way, shortest and fastest
    @classmethod
    def reverseFunction(cls, s:List[str]) -> None:
        s.reverse()
        # s[:] = s[::-1] also works but is a tricky solution

def main(argv):
    # Answer for number #1
            
if __name__ == "__main__":
    main()