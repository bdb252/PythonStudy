def updatebook(phonebook):
  print(f"{'수정기능':-^30}")
  origin_name = input('수정할 성명을 입력하세요: ')
  for i in range(0, len(phonebook)):
    get_name = phonebook[i]  
    if origin_name == get_name['name']:
      print('수정할 이름, 연락처, 주소를 입력하세요:')
      new_name = input('새로운 이름: ')
      new_phonenum = input('새로운 전화번호: ')
      new_address = input('새로운 주소: ')
      
      get_name['name'] = new_name
      get_name['phonenum'] = new_phonenum
      get_name['address'] = new_address
      
      print('연락처가 수정되었습니다.')
      break
  else:
    print('해당하는 성명이 없습니다.')