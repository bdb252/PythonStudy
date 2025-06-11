import pymysql

# 삭제를 위한 함수 선언
def delete_record():  
  conn = pymysql.connect(host='localhost', user='sample_user',
                        password='1234', db='sample_db', charset='utf8')
  curs = conn.cursor()
  # 무한루프 구성
  while True:
    # exit를 입력하는 경우 프로그램 종료
    isStr = input("삭제할일련번호(종료하려면 'exit'입력):")
    # 대문자를 입력하더라도 하나의 조건으로 판단하기 위해 소문자로 변경
    if isStr.lower()=='exit':
      print('프로그램을 종료합니다.')
      break
    
    # f-String 으로 쿼리문 작성
    sql = f"delete from board where num='{isStr}'"
    
    try:
      curs.execute(sql)
      conn.commit()
      print('1개의 레코드가 삭제됨')  
    except Exception as e:
      conn.rollback()
      print('쿼리 실행 오류발생', e)
      
    conn.close()
    
# 함수 호출하기
delete_record()
