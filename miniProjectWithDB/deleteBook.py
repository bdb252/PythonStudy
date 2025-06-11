import pymysql

def deletebook(phonebook):
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  print(f"{'삭제기능':-^30}")
  name = input('삭제할 이름을 입력하세요: ')
  sql = f"delete from phoneBook where username='{name}'"
  
  try:
    curs.execute(sql)
    conn.commit()
    print('정보가 삭제되었습니다.')  
  except Exception as e:
    conn.rollback()
    print('쿼리 실행 오류발생', e)
    
  conn.close()