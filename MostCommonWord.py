import re
import collections


class MostCommonWord:

    # runtime 40 ms, Memory Usage: 13.9MB
    @classmethod
    def myAnswer(cls, paragraph: str, banned: List[str]) -> str:
        banned = sorted(banned, key=len, reverse=True)
        for ban in banned:
            paragraph = paragraph.lower().replace(ban, '')
        words = re.sub('\W+', ' ', paragraph).split()
        word_dict = {word: words.count(word) for word in words}
        item = max(word_dict.items(), key=lambda x: x[1])
        return item[0]

    # cleanse special chars, empty spaces, banned words
    # use the collections Counter method to get a list of counts
    # runtime 40ms, Memory Usage: 14MB
    @classmethod
    def moreCleanerAnswer(cls, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


def main(argv):
    # Answer for number #1


if __name__ == "__main__":
    main(sys.argv[1:])
