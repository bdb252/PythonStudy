import pymysql

def printbook(phonebook):
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  
  print(f"{'출력기능':-^30}")
  print('번호\t성명\t전화\t주소\t')
  print('-'*34)
  try:
    sql = "select * from phoneBook"
    curs.execute(sql) 
    rows = curs.fetchall()
    for row in rows:
      print(row[0], row[1], row[2], row[3], end="\t")
      print()
  except Exception as e:
    print("쿼리 실행시 오류발생",e)
