# 스택 초기화
# index  0    1    2    3    4
stack = [None,None,None,None,None]
top = -1

top += 1 # top = 0
stack[top] = "커피"
top += 1 # top = 1
stack[top] = "녹차"
top += 1 # top = 2
stack[top] = "꿀물"

# 스택 출력
# range(start, stop, step)
print("------스택 상태------")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])


# push 함수
def push(data):
    global top
    top += 1
    stack[top] = data
# pop 함수
def pop():
    global top
    data = stack[top]
    stack[top] = None
    top -= 1
    return print("pop된 데이터: " + str(data))

# 스택 출력 함수
def print_stack():
    print("------스택 상태------")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("====================")

print_stack()
pop()
pop()
print_stack()
##ggg