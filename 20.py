import sys

def main():
    L = int(input())
    Txt = sys.stdin.read().replace("\n    ", " @ ").split()
    for i in range(L):
        if Txt[i] == '@':
            print("\n    ", end=' ')
            continue
        print(Txt[i], end=' ')

if __name__=="__main__":
    main()