x=int(input())
tmp = x
m = 0
while x > 0:
    num = x % 10
    m = m * 10 + num
    x = x // 10
if m == tmp:
    print("YES")
else:
    print("NO")