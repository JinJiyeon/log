## [03_DB 아키텍쳐와 튜닝](./03_DB/README.md)

- 목적 : 효율적인 SQL 코드를 구현하자
- 기간 : 2022/08/01 ~ 2022/08/05
- Ref
  - 책 <오라클로 배우는 데이터베이스 입문>
- 주안점
  - oracle DB의 아키텍쳐를 분석한다 (eg. lock, memory, index, join)
  - 같은 결과 다른 성능인 두 코드를 비교한다
  - 운영에 필요한 세부 기능을 학습한다

- 목차

  - DB의 메모리, PGA와 SGA

  - DB 세션과 동기화 문제

  - DB index 

  - 권한 관리

  - join의 원리

    

## 아키텍쳐

- PGA와 SGA [[참고]](https://1duffy.tistory.com/18)

  - PGA와 SGA 모두 메모리인데, 공유 범위와 용도에 차이가 있다.

    - PGA :
      - DB에 접속한 각 유저에게 할당되는 DB 서버 프로세스의 메모리. 
        각 유저 간에 공유되지 않는다.
      - 정렬할 때 주로 사용한다
      - format 에 대한 정보가 저장된다. 
        이를 변경하면 format 을 다르게 표기할 수 있다.

    - SGA : 
      - 디스크에서 데이터를 읽거나 변경할 때 사용하는 메모리.
        자주 쓰이는 데이터가 미리 올라와있다면 더 빠르게 작업이 가능하다.

  - 운영 시 참고사항
    - nls_session_parameter를 조회하면
      해당 pga의 format 을 확인할 수 있다.



- 세션과 동기화 문제
  - 각 유저는 세션을 연다. 하나의 DB에 여러 유저가 접속할 경우 동기화 문제가 발생할 수 있다. 이를 해결하기 위해 lock 을 걸어야 한다.
  - 이때 lock 을 효율적으로 거는 것이 전체 처리량을 늘리는 데 중요하다. 
  - lock 1단계 : read lock / write lock
    - write에 비해 read는 덜 critical 하고, 횟수가 많다. 
      read 에 lock 을 걸지 않을 경우 일관성은 떨어질 수 있으나 효율을 향상시킬 수 있다.
    - oracle DB는 read에 lock을 걸지 않는다.
      만약 read lock을 걸고 싶다면, 'SELECT ~ FOR UPDATE' 구문을 사용하면 된다.
  - lock 2단계 : where / where x
    - update delete with where 는 행 레벨로 락이 걸린다.
    - update delete without where 는 테이블 레벨로 락이 걸린다.
    - insert 구문은 lock에 상관없이 수행된다.
  - 운영 시 주의사항
    - SQL 을 실행이 지연된다면 lock 이 걸린 건 아닌지 의심해본다
    - 락을 최소화하기 위해 where 을 잘 작성하자



- DB index [[참고]](https://tecoble.techcourse.co.kr/post/2021-09-18-db-index/)

  - 인덱스로 지정된 열은 별도의 b tree를 생성해 저장된다. 

  - 장점으로 조회속도가 빨라지지만
    단점으로 저장공간을 추가적으로 소모한다.

  - 항상 성능이 좋아지는 것은 아니다.
    insert, delete, update 가 발생할 때마다 b tree 를 새로 생성하기 때문이다.
    따라서 유니크한 값의 개수가 많고 변화가 적은 행을 인덱스로 선정하는 것이 좋다.

  - 운영 시 주의사항

    - 특정 칼럼을 인덱스로 설정하기
      - 유니크한 값의 개수가 많고
      - 변화가 적은 행을 인덱스로 선정하는 것이 좋다.

    - LIKE 'A%' 와 LIKE '%A'
      - 인덱스 칼럼을 LIKE를 활용해 조회할 경우 
      - 'A%'는 인덱스를 활용해 빠르게 조회가 가능하다.
      - '%A'는 전체 로우를 탐색해야 하므로 느리다. 사용을 지양해야 한다.



- 권한 관리

  - 실제 서비스를 할 때에는 안전과 보안을 위해 사용자별로 기능별로 권한을 나누는 것이 필요하다.

  - 사용자별로 권한을 나눈다.

    eg) 

    - sys : 서버 관리

      system : 사용자 관리

      scott, hr, oe 등등 : 각 기능

    - system 에서 GRANT와 REVOKE 구문을 활용해 권한을 부여하고 회수할 수 있다.

      hr 에서 scott 에게 hr 테이블의 select 권한을 부여하고 회수할 수 있다.

  - 기능별로 권한을 나눈다.
    - 기능별로 select, create index, drop view 등 다양한 권한이 있다.
    - 보편적으로 함께 부여하는 권한을 묶어서 role로 만들었다.



- join [[참고]](https://schatz37.tistory.com/2)

  - driving table 의 각 행에서
    inner table 이 일치하는 값을 조회해 join 한다.

  - join 성능을 높이려면

    - driving table 이 작아야 한다
    - inner table 의 결합키가 인덱스로 되어 있다면 검색 속도가 빨라진다.

  - 운영 상 참고할 점

    - driving table 선정은 optimizer 가 알아서 수행한다.

    - 결합키로 어떤 칼럼을 선정할 것인지는 개발자가 선택할 수 있다.
      그러므로 join 할 때 결합키를 잘 선정하는 것이 중요하다!

      

## 세부기능

- 뷰

  - 자주 사용하는 테이블, 자주 조인하는 내용을 미리 묶어둔 것이다.

    

- 시퀀스

  - 시퀀스를 생성할 때 동기화 문제를 고려해야 한다.
    백엔드 서버에서 시퀀스를 생성할 경우 동기화 문제가 발생할 수 있어,
    oracle 에서 구현해둔 기능을 활용하는 것이 효율적이다.
  - mysql 의 경우 auto increment 라는 기능을 지원한다.
    oracle 의 경우 create sequence 구문으로 시퀀스를 정의해줄 수 있다.