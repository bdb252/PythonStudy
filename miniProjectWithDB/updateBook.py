import pymysql

def updatebook(phonebook):
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  print(f"{'수정기능':-^30}")

  sql = """update phoneBook 
  set username='{1}', phonenum='{2}', address='{3}' where username='{0}'
  """.format(input('수정할 성명을 입력하세요: '),input('새로운 이름: '),input('새로운 전화번호: '), 
             input('새로운 주소: '))
  
  try:
    curs.execute(sql)
    conn.commit()
    print('연락처가 수정되었습니다.')
  except Exception as e:
    conn.rollback()
    print('쿼리 실행 오류발생', e)  
  
  conn.close()