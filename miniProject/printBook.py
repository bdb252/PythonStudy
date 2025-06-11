def printbook(phonebook):
  print(f"{'출력기능':-^30}")
  print('번호\t성명\t전화\t주소\t')
  print('-'*34)
  for cnt in range(0, len(phonebook)):
    get_values = phonebook[cnt].values()
    print(cnt+1, end='\t')
    for k in get_values:
      print(k, end='\t') 
    print()