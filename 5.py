x = int( input() )
i = 1
n = x
tmp = x
while (x * n != x * ( 10 ** (i - 1) ) + n // 10 ):
    n = n + 10**i *( ((tmp%10)*x + (tmp//10)) %10)
    tmp = ((tmp%10)*x + (tmp//10))
    i+=1
print(int(n))
