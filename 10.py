def matrix(lst: list):
    def det3x3(lst: list):
        plus = lst[0][0] * lst[1][1] * lst[2][2]
        plus += lst[1][0] * lst[0][2] * lst[2][1]
        plus += lst[0][1] * lst[2][0] * lst[1][2]
        minus = lst[0][2] * lst[1][1] * lst[2][0]
        minus += lst[0][0] * lst[1][2] * lst[2][1]
        minus += lst[1][0] * lst[0][1] * lst[2][2]
        return plus - minus
    det = 0
    for i, num in enumerate(lst[0]):
        x = det3x3([ list(lst[1][:i]) + list(lst[1][(i+1)%5:]), \
                    list(lst[2][:i]) + list(lst[2][(i+1)%5:]), \
                    list(lst[3][:i]) + list(lst[3][(i+1)%5:]) ])
        det += (-1)**i * x * num
    return det

def main():
    lst = eval(input())
    print(matrix(lst))

if __name__ == "__main__":
    main()