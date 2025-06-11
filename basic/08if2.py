print(f"{'중첩된 if문':-^30}")
# 입력받은 값을 즉시 정수로 변환
num1 = int(input("숫자 하나를 입력하세요:"))
# 중첩된 구조의 if문 작성
if num1 % 2 == 0:
  if num1 % 3 == 0:
    print('2와 3으로 나누어짐')
  else:
    print('2는 가능, 3은 불가')
else:
  if num1 % 3 == 0:
    print('2는 불가, 3은 가능')
  else:
    print('2와 3 모두 불가')

'''
삼항연산자의 형식
  변수 = True일때문장 if 조건식 else False일때문장
  만약 결과를 할당할 필요가 없다면 좌측항은 생략할 수 있다. 
'''
print(f"{'삼항연산자':-^30}")
# 삼항연산자
number=99
# 조건에 맞는 값을 좌측항으로 할당
result = "100보다 크다" if number>100 else "100보다 작다"
print(result)
# 할당없이 즉시 조건에 맞는 print문을 실행한다. 
print("3의 배수") if number%3==0 else print('3의 배수 아님')

print(f"{'if~in문':-^30}")
countryList = ['세부', '보라카이', '파타야', '나트랑', '코타키나발루', '푸켓']
journey = input('여행할 나라를 입력하세요:')
# 리스트에 입력한 나라가 포함되었다면 True를 반환
if journey in countryList :
  print("{}는(은) 여행지 목록에 있습니다.". format(journey))
else:
  print("{}는(은) 여행지 목록에 없습니다.". format(journey))
  
  
'''
퀴즈1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
kor=int(input('국어 점수를 입력하시오:'))
math=int(input('수학 점수를 입력하시오:'))
eng=int(input('영어 점수를 입력하시오:'))
avg = float((kor+math+eng) / 3)
if avg >= 90:
  print('A학점')
elif avg >= 80:
  print('B학점')
elif avg >= 70:
  print('C학점')
elif avg >= 60:
  print('D학점')
else:
  print('F학점')


'''
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 
패스워드를 입력받아 일치하는지 확인하는 프로그램을 작성하시오.
여기서 패스워드는 1234로 가정합니다. 
'''
user_info = ['abcd', 'qwer', 'zxcv']
user_id = input('아이디를 입력하세요:')
if user_id in user_info :
  user_pass = input('패스워드를 입력하시오:')
  if user_pass=='1234' :
    print('아이디와 패스워드가 일치합니다.')
  else:
    print('패스워드가 일치하지 않습니다.')
else:
  print('아이디가 존재하지 않습니다.')
