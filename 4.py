from math import log2
maxPow = int(log2( 1000000 ))
def pow2( num: int ) -> bool:
    for i in range( 2, maxPow + 1 ):
        # print(int( num ** ( 1 / i ) ))
        if ( ( round( num ** ( 1 / i ) ) ** i ) )  == num:
            return True
    return False

def main():
    x = int(input())
    print("YES" if pow2(x) else "NO")

if __name__ == "__main__":
    main()