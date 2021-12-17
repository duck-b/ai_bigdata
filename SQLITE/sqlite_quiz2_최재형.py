# 다음과 같이 sqlite를 이용하여 주소록 프로그램을 완성하여라. 
# quiz_connect_수강생명.py 으로
# coderecipe@naver.com으로 제출

# sqlite 임포트 
import sqlite3

# 연결변수와 작업변수 생성
conn = sqlite3.connect('contact2.db')
cursor = conn.cursor()

# 테이블 생성 함수 정의
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactTb1(
            code integer not null primary key autoincrement,
            name text not null,
            mobile text not null,
            email text,
            addr text not null
        );
    ''')
    conn.commit()

# 레코드 삽입 함수 정의
def insert_record():
    print('='*50)
    print('\t레코드 삽입')
    name = input('이름 : ')
    mobile = input('연락처 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    sql = 'INSERT INTO contactTb1 (name, mobile, email, addr) VALUES (?, ?, ?, ?);'
    cursor.execute(sql, (name, mobile, email, addr))
    conn.commit()

# 레코드 출력 함수 정의
def print_record():
    sql = 'SELECT * FROM contactTb1;'
    cursor.execute(sql)
    rows = cursor.fetchall()
    # 주소록에 데이터가 없다면 메세지 출력.
    if len(rows) == 0:
        print('등록된 주소 목록이 없습니다.')
    else:
        print('-'*50)
        print('  번호\t|  이름\t\t|  연락처\t\t|  이메일\t\t|  주소\t|\n')
        for row in rows:
            for(item) in row:
                print(' ', item, end='\t|')
            print('\n')
        print('-'*50)

# 레코드 수정 함수 정의
def update_record():
    print('='*50)
    print('\t수정할 코드')
    code = input('코드 : ')
    selectSql = 'SELECT * FROM contactTb1 WHERE code = ?;'
    cursor.execute(selectSql, code)
    row = cursor.fetchone()
    print('번호 :', row[0], ', 이름: ', row[1], ', 연락처: ', row[2], ', 이메일: ', row[3], ', 주소: ', row[4])
    
    name = input('이름 : ')
    mobile = input('연락처 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    updateName = name if name != '' else row[1]
    updateMobile = mobile if mobile != '' else row[2]
    updateEmail = email if email != '' else row[3]
    updateAddr = addr if addr != '' else row[4]
    
    updateSql = 'UPDATE contactTb1 SET name = ?, mobile = ?, email = ?, addr = ? WHERE code = ?;'
    cursor.execute(updateSql, (updateName, updateMobile, updateEmail, updateAddr, code))
    conn.commit()
    print('레코드가 수정되었습니다.')

def delete_record():
    print('='*50)
    print('\t삭제할 코드')
    code = input('코드 : ')
    sql = 'DELETE FROM contactTb1 WHERE code = ?;'
    cursor.execute(sql, code)
    conn.commit()
    print('레코드가 삭제되었습니다.')

# 레코드 전체 삭제 (초기화)
def delete_all():
    sql = 'DELETE FROM contactTb1;'
    cursor.execute(sql)
    conn.commit()
    print('레코드가 모두 삭제되었습니다.')

# 메인 메뉴 기능
while True:
    print()
    print('='*50)
    print('\t\t주소록 메뉴\t\t')
    print('='*50)
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 수정')
    print('4. 연락처 삭제')
    print('5. 연락처 초기화')
    print('6. 종료')
    print('='*50)
    print()
    menu = input('메뉴선택 : ')
    if menu == '1':
        insert_record()
    elif menu == '2':
        print_record()
    elif menu == '3':
        update_record()
    elif menu == '4':
        delete_record()
    elif menu == '5':
        delete_all()
    elif menu == '6':
        print('프로그램 종료')
        break
    else:
        print('잘못 선택하였습니다.')

# 데이터베이스 종료
conn.close()