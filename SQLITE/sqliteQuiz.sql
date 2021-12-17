/* CREATE TABLE
CREATE TABLE userTBL
(
	userID TEXT NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
	userName TEXT NOT NULL, -- 이름
	birthYear INTEGER NOT NULL,  -- 출생년도
	addr TEXT NOT NULL, -- 지역
	mobile1 TEXT, -- 휴대폰의 국번(010, 011, 016, 017, 018, 019 등)
	mobile2 TEXT, -- 휴대폰의 나머지 전화번호(하이픈제외)
	height INTEGER,  -- 키
	mDate date  -- 회원 가입일
);
*/

/* INSERT
INSERT INTO userTBL VALUES ('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES ('KBS', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES ('KKH', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES ('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES ('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO userTBL VALUES ('LJB', '임재범', 1963, '서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES ('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
*/

/* UPDATE
UPDATE userTBL SET addr='부산' WHERE addr='경남';
*/

/* IS NULL
UPDATE userTBL SET mobile1='011' WHERE mobile1 IS NULL;
UPDATE userTBL SET mobile2='55555555' WHERE mobile2 IS NULL;
*/

/* TABLE 복사
CREATE TABLE userTBL2 AS SELECT * FROM userTBL;
SELECT * FROM userTBL2;
*/

/* DELETE
DELETE FROM userTBL2 WHERE MOBILE1='011';
*/

/* TABLE 구조만 복사
CREATE TABLE userTBL3 AS SELECT * FROM userTBL WHERE 1<>1;
SELECT count(*) FROM userTBL3;
*/

/*
CREATE TABLE userTBL3
	AS
	SELECT * FROM userTBL WHERE addr IN ('서울', '경기');
--또는
CREATE TABLE userTBL3
	AS
	SELECT * FROM userTBL WHERE addr ='서울' OR addr='경기';
*/

/* RENAME COLUMN
ALTER TABLE userTBL3 RENAME COLUMN birthyear TO birth;
*/

/* ADD COLUMN
ALTER TABLE userTBL3 ADD COLUMN age INTEGER;
UPDATE userTBL3 SET age = 2021-birth;
*/

/* DELETE COLUMN
CREATE TABLE temp 
   AS SELECT userID, userName, BIRTH, addr, mobile1, mobile2, AGE FROM userTBL3;
DROP TABLE userTBL3;
ALTER TABLE temp RENAME TO userTBL3;
*/

SELECT * FROM userTBL3;