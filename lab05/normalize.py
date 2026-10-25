import sys
def main():
    s = sys.stdin.readline().rstrip('\n')
    normalized = ' '.join(s.split())
    words = normalized.split() if normalized else []
    print(len(s))
    print(len(normalized))
    print(normalized)
    print(len(words))
if __name__ == '__main__':
    main()
