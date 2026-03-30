stack = []
capacity = 5

def isFull():
    if len(stack) == capacity:
        return True
    else:
        return False
    
def push(data):
    if isFull():
        print("Stack이 차 있어서 더 이상 추가할 수 없습니다.")
    else:
        stack.append(data)

def pop():
    if isEmpty():
        print()
        return -1
    else:
        return stack.pop()

print(f"[[ 정수형 스택 연산 실습 (용량 : {capacity})]]")

while True:
    menu = int(input("> 메뉴 선택 : "))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input("데이터 입력"))
        push(data)
    elif menu == 2:
        data = pop()
        print()

    print("> 현재 스택 상태 ", stack)
print("[[ 정수형 스택 연산 실습 종료 ]]")