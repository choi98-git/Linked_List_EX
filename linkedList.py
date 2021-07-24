# 클래스와 함수 선언
class Node():
    def __init__ (self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def makeSimpleLinkedList(namePhone):
    global head, current, pre

    newNode = Node()
    newNode.data = namePhone
    
    # 첫 번째 노드일 때
    if head == None:
        head = newNode
        return
    
    # 첫 번째 노드보다 작을 때
    elif head.data[0] > namePhone[0]:
        newNode.link = head
        head = newNode
        return
    
    # 중간 노드로 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] > namePhone[0]:
            pre.link = newNode
            newNode.link = current
            return
        
    # 삽입 노드가 가장 클 때
    current.link = newNode

def deleteLinkedList(deleteData):
    global head, current, pre

    if searchLinkedList(deleteData) != None:
        if head == current:
            head = head.link
            del(current)
            print("%s님의 정보가 삭제되었습니다." %deleteData)
            return
        pre.link = current.link
        del(current)
        print("%s님의 정보가 삭제되었습니다." %deleteData)

def searchLinkedList(searchData):
    global head, current, pre

    if head == None:
        print("빈 리스트입니다")
        return

    current = head

    while current != None:
        if current.data[0] == searchData:
            print(current.data)
            return current
        pre = current
        current = current.link

    print("입력하신 정보가 없습니다!!")
    return

def updateLinkedList(updateData):
    global head, current, pre

    if searchLinkedList(updateData) != None:
        print("{}님의 전화번호는  {}입니다.".format (current.data[0], current.data[1]))
        current.data[1] = input("수정할 전화번호: ")
        print("{}님의 전화번호가 {}로 수정되었습니다.".format (current.data[0], current.data[1]))
    
def menu():
    while True:
        print("==================================================\n")
        print(" [0: 종료] [1: 입력] [2: 수정] [3: 삭제] [4, 탐색]\n")
        print("==================================================\n")
        menu = int(input("메뉴 입력: "))

        # 종료
        if menu == 0:
            quit()
            
        # 입력
        elif menu == 1:
            # 사용자로부터 이름, 전화번호 입력 받음
            name = input("이름: ")
            phone = input("전화번호: ")
            data = [name, phone]
            # 데이터를 노드에 삽입
            makeSimpleLinkedList(data)         
            printNodes(head)
            
        # 수정
        elif menu == 2:
            update_name = input("수정할 사람의 이름: ")
            updateLinkedList(update_name)
            printNodes(head)


        # 삭제
        elif menu == 3:
            delete_name = input("삭제할 사람의 이름: ")
            deleteLinkedList(delete_name)
            printNodes(head)

        # 탐색
        elif menu == 4:
            search_name = input("탐색할 사람의 이름: ")
            searchLinkedList(search_name)
            
        # 오류
        else:
            print("[Error]다시 입력!!")
            
## 전역 변수 선언 부분 ##
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__" :
    menu()
            
