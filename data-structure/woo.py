def count_down(n):
    if n <= 0:
        print("Countdown finished!")
        return
    print(n)
    m =n-1
    count_down(m) # count_down callback

count_down(5)

def print_star(num):
    if num > 0:
        print_star(num-1)
        print("*" * num)

print_star(5)

# def gugu(dan,num=1):
#     print("%d X %d = %d") % (dan, num , dan*num)
#     if num < 9:
#         gugu(dan,num+1)

# for i in range(2,10):
#     gugu(1)

def pow(base, exponent):
    if exponent == 0:
        return 1
    else:
        print("base:", base, "exponent:", exponent)
        return base * pow(base, exponent-1)

print(pow(2,4))

###############################

def arr_sum(arr,n):
    if n <= 0:
        return 0
    else:
        return arr[n-1] + arr_sum(arr, n-1) # arr_sum callback

foo = [1,2,3,4,5]
arr_sum(foo,len(foo))
###############################

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) #fibonacci callback

print(fibonacci(5))