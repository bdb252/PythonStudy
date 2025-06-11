from insertBook import *
from printBook import *
from searchBook import *
from updateBook import *
from deleteBook import *

def menu():
  # 메뉴 출력 및 입력값을 반환하는 함수
  print()
  print('메뉴 중 숫자를 선택하세요:')
  print('1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료')
  return input('선택:')

phoneBook = []
print('PhoneBook with DB')
while True:
  choice = int(menu())
  if choice == 1:
    phoneBook = insert(phoneBook)
  elif choice == 2:
    printbook(phoneBook)
  elif choice == 3:
    searchbook(phoneBook)
  elif choice == 4:
    updatebook(phoneBook)
  elif choice == 5:
    deletebook(phoneBook)
  elif choice == 6:
    break
  else:
    print('잘못된 입력입니다.')