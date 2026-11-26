# 0(n) time complexity
# sum = 0
# for n in range(10000000,0,-1):
#     sum += n
#     print(sum)

# 0(1) time complexity
def sum_numbers(n, m):
    if n>m:
        max=n
        min=m
    else:
        max=m
        min=n
    foo = ((min+max)*max)/2
    print(foo)

sum_numbers(1,10000000)