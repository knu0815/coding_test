import collections
import re

class ValidPalindrome:
    @classmethod
    def list_iteration(cls, s):
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        while len(chars) > 1:
            if chars.pop(0) != chars.pop():
                return False
        return True


    # Deque is Far more faster than normal list manipulation because 
    # list.pop(0) runs on O(N) time while list.popleft() on deque
    # runs on O(1)
    @classmethod    
    def deque(cls, s):
        chars: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        while len(chars) > 1:
            if chars.popleft() != chars.pop():
                return False
        return True

    @classmethod
    def slicing(cls, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1] # Slicing Used


# Point 1: Slicing is very powerful when manipulating list, could be much faster than iteration
# Point 2: Deque.popleft() = O(1), list.pop(0) = O(N)


def main(argv):
    # Answer for number #1
            
if __name__ == "__main__":
    main(sys.argv[1:])