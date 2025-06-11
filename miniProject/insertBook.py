def insert(phonebook):
  print(f"{'입력기능':-^30}")
  name=input('성명>>> ')
  phonenum=input('전화>>> ')
  address=input('주소>>> ')
  dict = {"name" : name, "phonenum":phonenum, "address": address}
  # print(dict)
  phonebook.append(dict)
  print('주소 입력 완료!')
  return phonebook