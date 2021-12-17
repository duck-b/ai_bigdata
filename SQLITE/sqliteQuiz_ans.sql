-- 0) sqlite Browser를 실행하고 [새 데이타베이스] 클릭해서 데이타베이스를 파일명.db로 저장 하거나 
--      기존 데이타베이스와 연결할 경우 [데이타베이스 열기] 클릭후 연결하고자 하는 데이타베이스 파일 선택 


-- 1) userTBL 테이블을 다음과 같은 구조로 생성한 후 구조를 확인한다.

CREATE TABLE userTBL -- 회원 테이블
( userID  	TEXT NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  userName  TEXT NOT NULL, -- 이름
  birthYear 	INTEGER NOT NULL,  -- 출생년도
  addr	  	TEXT NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1	TEXT, -- 휴대폰의 국번(010, 011, 016, 017, 018, 019 등)
  mobile2	TEXT, -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    	INTEGER,  -- 키
  mDate    	date  -- 회원 가입일
);

SELECT count(*) FROM userTBL;



-- 2) userTBL에 아래  데이터를 참조하여 데이터를 삽입하고 출력하여라.
/*
USERID   USERNAME    BIRTHYEAR      ADDR      MOBILE1    MOBILE2    HEIGHT       MDATE   
--------    ----------           ---------- -- --- -------- ---------- -       -------
LSG         이승기           1987                  서울          011   11111111          182       08/08/08
KBS         김범수           1979                  경남          011   22222222          173      12/04/04
KKH        김경호           1971                  전남          019   33333333          177       07/07/07
JYP         조용필           1950                  경기          011    44444444         166       09/04/04
SSK         성시경           1979                  서울                                             186      13/12/12
LJB          임재범           1963                  서울          016     66666666        182        09/09/09
YJS         윤종신           1969                  경남                                             170        05/05/05
*/


INSERT INTO userTBL VALUES ('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES ('KBS', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES ('KKH', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES ('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES ('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO userTBL VALUES ('LJB', '임재범', 1963, '서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES ('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');


SELECT count(*) FROM userTBL;


-- 3) userTBL 테이블에서 ADDR 컬럼값이 경남인 경우 경남을 부산으로 데이터값을 수정하여라.

UPDATE userTBL SET ADDR='부산' WHERE ADDR='경남'; 
SELECT * FROM userTBL;



-- 4) userTBL 테이블에서 MOBILE1과 MOBILE2 값이 NULL 인 경우 011, 55555555 값으로 수정하여라.

-- NULL 값 조회 
SELECT * FROM userTBL WHERE (MOBILE1 IS NULL) AND (MOBILE2 IS NULL);

-- UPDATE userTBL SET MOBILE1='010' WHERE MOBILE1 IS NULL; 
-- UPDATE userTBL SET MOBILE2='55555555' WHERE MOBILE2 IS NULL; 

-- NULL 값 조회 
SELECT * FROM userTBL WHERE (MOBILE1 IS NULL) AND (MOBILE2 IS NULL);

UPDATE userTBL SET mobile1 = '010', MOBILE2='55555555'
		WHERE (MOBILE1 IS NULL) AND (MOBILE2 IS NULL);

SELECT * FROM userTBL;



-- 5) userTBL 테이블 모두를 복사하여 userTBL2 테이블로 생성하여라. 

CREATE TABLE userTBL2 AS SELECT * FROM userTBL;
SELECT * FROM userTBL2;



-- 6) userTBL2 테이블에서 국번이 011인 데이터를 삭제하여라

DELETE FROM userTBL2 WHERE MOBILE1='011';

SELECT * FROM userTBL2;


-- 7) userTBL 테이블에서 구조만 복제하여 userTBL3 테이블을 생성하여라.(X)
-- DROP TABLE userTBL3;
-- CREATE TABLE userTBL3 AS SELECT * FROM userTBL WHERE 1<>1;
-- SELECT count(*) FROM userTBL3;


-- 8) userTBL 테이블에서 지역이 서울, 경기인 레코드만 복사해서 userTBL3 테이블을 생성하여라. 

CREATE TABLE userTBL3 
  AS 
  SELECT * FROM userTBL WHERE  (addr = '서울') OR (addr =  '경기');


CREATE TABLE userTBL3 
  AS 
  SELECT * FROM userTBL WHERE  addr IN ('서울', '경기');

SELECT * FROM userTBL3;


-- 9) userTBL3 테이블에서 BIRTHYEAR 컬럼명을 BIRTH로 변경하여라.
ALTER TABLE userTBL3 RENAME COLUMN BIRTHYEAR TO BIRTH;
SELECT * FROM userTBL3;


-- 10) userTBL3 테이블에서 AGE 컬럼을 추가하고 현재년도와 BIRTH 컬럼을 이용하여 데이터를 수정하여라. 

ALTER TABLE userTBL3 ADD COLUMN AGE INTEGER;
SELECT * FROM userTBL3;

UPDATE userTBL3 SET AGE = 2021-BIRTH;
SELECT * FROM userTBL3;


-- 11) userTBL3 테이블에서  MDATE와 height 컬럼을 삭제하여라.
-- sqlite에서는 DROP COLUMN 명령문이 없다.
-- ALTER TABLE userTBL3 DROP COLUMN MDATE; -- 안된다. 
-- 공식 사이트에서는 DROP TABLE, ALTER TABLE RENAME TO문을 이용하라고 가이드 하고 있다.

CREATE TABLE temp 
	AS SELECT userID, userName, BIRTH, addr, mobile1, mobile2, AGE FROM userTBL3;

DROP TABLE userTBL3;

ALTER TABLE temp RENAME TO userTBL3;
SELECT * FROM userTBL3;


