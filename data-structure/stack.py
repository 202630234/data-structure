# 스택 초기화 함수
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    print("스택 초기화 완료 스택 크기는: " + str(size) + "입니다")
# 스택 full 여부 확인 함수
def is_full():
    global stack, top
    rest = len(stack) - 1 - top
    if top == len(stack) -1:
        return print("스택이 가득 찼습니다.") # True
    else:
        return print("스택이 가득 차지 않았습니다. 남은 용량:",rest) # False
# 스택 empty 여부 확인 함수
def is_empty():
    global stack, top
    if top == -1:
        return True
    else:
        return False
# 스택 peek 함수
def peek():
    global top
    data = stack[top]
    return print("peek된 데이터: " + str(data))


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
    if (is_empty()):
        return print("스택이 비어있습니다.")
    return print("pop된 데이터: " + str(data))

# 스택 출력 함수
# range(start, stop, step)
def print_stack():
    print("------스택 상태------")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("====================")

init_stack(7)
is_full()
push("커피")
push("녹차")
push("꿀물")
push("콜라")
push("사이다")
print_stack()
is_full()
pop()
pop()
pop()
print_stack()
peek()