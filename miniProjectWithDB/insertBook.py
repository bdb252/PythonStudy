import pymysql

def insert(phonebook):
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  print(f"{'입력기능':-^30}")

  sql = f"""INSERT INTO phoneBook (username, phonenum, address)
    VALUES ('{input('성명>>> ')}', '{input('전화>>> ')}', '{input('주소>>> ')}')"""
  
  try:
    # 쿼리문 실행
    curs.execute(sql)
    # MariaDB에 변경사항을 적용
    conn.commit()
    print('1개의 주소 입력 완료!')  
  except Exception as e:
    # 오류가 발생하면 롤백처리
    conn.rollback()
    print('쿼리 실행 오류발생', e)
    
  # 작업완료되면 자원 해제
  conn.close()