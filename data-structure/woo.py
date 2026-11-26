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