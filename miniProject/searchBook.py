def searchbook(phonebook):
  print(f"{'검색기능':-^30}")
  print('이름을 입력해주세요.')
  name = input('이름: ')
  for i in range(0, len(phonebook)):
    get_name = phonebook[i]  
    if name == get_name['name']:
      print('번호\t성명\t전화\t주소\t')
      print('-'*34)
      get_values = get_name.values()
      print(i+1, end='\t')
      for k in get_values:
        print(k, end='\t') 
      print()
      break
  else:
    print('검색 결과가 없습니다.')
  