import pymysql

def searchbook(phonebook):
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  print(f"{'검색기능':-^30}")
  print('이름을 입력해주세요.')
  try:
    sql = "select * from phoneBook where username like '%{0}'".format(input("이름:"))
    curs.execute(sql) 
    print('번호\t성명\t전화\t주소\t')
    print('-'*34)
    rows = curs.fetchall()
    for row in rows:
      print(row[0], row[1], row[2], row[3], end="\t")
      print()
  except Exception as e:
    conn.rollback()
    print('쿼리 실행 오류발생', e)
    
  conn.close()