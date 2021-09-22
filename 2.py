x,y,z = eval(input())
a,b=eval(input())
z_2 = z ** 2
while a != 0 or b != 0:
    num = ( a - x ) ** 2 + ( b - y ) ** 2
    if num > z_2:
        print("NO")
        exit(0)
    a,b=eval(input())
print("YES")