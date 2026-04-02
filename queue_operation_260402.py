from collections import deque
queue = deque()

def Enqueue(data) : queue.append(data)
def Dequeue() : return queue.popleft() if queue else None
def Get_Front() : return queue[0] if queue else None

while True : 
    print("""=============================================
  1.Enqueue  2.Dequeue  3.Get Front  0.Exit
=============================================""")
    menu = int(input(">> 연산 메뉴 선택 : "))

    if menu == 1 : 
        data = int(input(">> 추가할 데이터 입력 : "))
        Enqueue(data)
    if menu == 2 :
        data = Dequeue()
        print("가져온 데이터 : ",data,end=" ") if data is not None else print("데이터가 비어 있습니다",end=" ")
    if menu == 3 :
        data = Get_Front()
        print("가져올 데이터 : ",data,end=" ") if data is not None else print("데이터가 비어 있습니다",end=" ")
    if menu == 0 :    
        print("정수형 Queue 종료")
        break
    print("[Queue] ",queue)