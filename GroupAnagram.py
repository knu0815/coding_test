import collections


class GroupAnagram:

    # defaultdict creates a default key value for the demanded list.
    @classmethod
    def groupAnagrams(cls, strs: List[str]) -> List[List[str]]:
        anagram_list = collections.defaultdict(list)
        for word in strs:
            anagram_list[''.join(sorted(word))].append(word)
        return anagram_list.values()


def main(argv):
    # Answer for number #1


if __name__ == "__main__":
    main(sys.argv[1:])
