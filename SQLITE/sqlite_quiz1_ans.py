# 퀴즈 : 아래의 파일을 생성하고
# sqlite_quiz1.py
# 테이블 생성 및 CRUD 실습
# 제출하지 않으셔도 됩니다. 

import sqlite3

# 0) productDb 생성
# 연결변수 생성 => sqliteDB 연결
conn = sqlite3.connect('productDb2.db')
# 작업변수 생성 
cursor = conn.cursor()
#
# 1) productTbl 테이블 생성
#   모든 필드는 필수항목 Not Null
#
#   제품코드(pCode) : Text, Primary Key
#   제품명(pName) : Text
#   가격(price) : int
#   재고수량(amount) : int

# 테이블이 있다면 삭제 
# cursor.execute('DROP TABLE IF EXISTS  productTbl;')
# conn.commit()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS productTbl (
                    pCode text not null primary key, 
                    pName text not null, 
                    price integer not null, 
                    amount integer not null 
             );
''')
print('테이블 생성 완료')
conn.commit()


# 2) 데이타 삽입
#    5개 이상의 데이타 임의로 삽입
'''
p001  바나나우유  1000  5
p002  저지방 우유 2200  4
p003  초코 우유  700  10
p004  커피 우유  1200  6
p005  유기농 우유  4200  17

'''


# sql = 'insert into productTbl values (?,?,?,?)'
# cursor.execute(sql, ('p001', "바나나 우유", 1000, 5))
# cursor.execute(sql, ('p002', "저지방 우유", 2200, 4))
# cursor.execute(sql, ('p003', "초코 우유", 700, 10))
# cursor.execute(sql, ('p004', "커피 우유", 1200, 6))
# cursor.execute(sql, ('p005', "유기농 우유", 4200, 17))

# conn.commit()

# 3) 모든 데이타 출력
# cursor.execute('select * from productTbl')

# result = cursor.fetchall()
# title_list = ['제품코드', '제품명', '가격', '재고수량']
# print("="*50)
# for row in result:
#     for i in range(4):
#         print(title_list[i], '=>', row[i])
#     print('_'*50)



# 4) 데이타 수정
#   마지막에 삽입된 레코드에서 가격(price) 변경


# 1) 수정하고자 하는 레코드의 제품코드값 직접 입력 
# sql = 'update productTbl set price = 1000 where pCode = ? ;'
# cursor.execute(sql, ('p005'))
# conn.commit()
# print('레코드 수정 완료')

# 2) 가장 마지막에 삽입레코드의 제품코드값을 별도로 저장하고 다시 수정명령에 사용 
# rowid는 sqlite의 고유 행번호 

# 테이블의 마지막 레코드의 pCode 조회 
cursor.execute('select pCode from productTbl order by rowid desc limit 1 ')
temp = cursor.fetchone()
print('마지막 레코드의 pCode => ', temp)

# 마지막 레코드의 pCode를 이용해서 레코드 수정 
sql = 'update productTbl set price = 1000 where pCode = ? ;'
cursor.execute(sql, temp)
conn.commit()
print('레코드 수정 완료')


# 5) 데이타가 수정된 레코드만 출력
# sql = 'select * from productTbl where pCode = ? ;'
# cursor.execute(sql, temp)
# result = cursor.fetchone()
# print("="*50)
# print(result)



# 6) 데이타 삭제
#    가격이 임의의 값보다 작은 레코드 삭제
#    예) 가격이 1000 원이하의 레코드 

cursor.execute('delete from productTbl where price <= 1000')
conn.commit()
print("="*50)
print("가격이 1000 원이하의 레코드 삭제완료")

# 7) 모든 데이타 출력


cursor.execute('select * from productTbl')

result = cursor.fetchall()
title_list = ['제품코드', '제품명', '가격', '재고수량']
print("="*50)
for row in result:
    for i in range(4):
        print(title_list[i], '=>', row[i])
    print('_'*50)

conn.close()