def deletebook(phonebook):
  print(f"{'삭제기능':-^30}")
  name = input('삭제할 이름을 입력하세요: ')
  for i in range(0, len(phonebook)):
    get_name = phonebook[i]  
    if name == get_name['name']:
      del phonebook[i]
      print('정보가 삭제되었습니다.')
      break
  else:
    print('해당하는 정보가 없습니다.')