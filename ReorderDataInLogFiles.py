class ValidPalindrome:
    @classmethod
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
            letters, digits = [],[]
            for log in logs:
                if log.split()[1].isdigit():
                    digits.append(log)
                else:
                    letters.append(log)
            
            letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
            return letters + digits

def main(argv):
    # Answer for number #1
            
if __name__ == "__main__":
    main(sys.argv[1:])