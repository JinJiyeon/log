# Operation 관련 스터디 기록



### 🏆미션

관심있는 주제들을 깊이있게 파보자



### 🧑🏻‍💻과제 리스트

- Kafka
- CI/CD
- java



### 🎯기록사항

기본정보 : 목적 / 관련 개념 / 기간 / Reference

상세정보 : 주요내용 / 주안점 & 강점 / 어려웠던 점



#### [01_Docker 배포](./01_Docker/README.md)

- 목적 : 배포 환경을 도커 이미지로 만들어서 관리하자
- 기간 : 2022/06/15 ~ 2022/06/17
- 단계
  - single container 이미지를 빌드하여 배포하자
  - multiple container를 docker-compose로 배포하자



#### [02_k8s 배포](./02_k8s/README.md)

- 목적 : 분산처리 환경에서 배포를 관리하자
- 기간 : 2022/06/20 ~ 2022/06/23
- 단계
  - MSA를 운영할 때에, 가장 좋은 아키텍쳐에 대해 고민해보자
  - deployment 로 무중단 서비스를 운영해보자
  - service 로 pod 외부의 통신을 가능하게 하자
  - ingress 로 application layer 의 네트워크 환경설정을 해주자
  - helm chart 로 k8s 관리를 용이하게 하자



#### [03_DB 아키텍쳐와 튜닝](./03_DB/README.md)

- 목적 : 효율적인 SQL 코드를 구현하자
- 기간 : 2022/08/01 ~ 2022/08/05
- Ref
  - 책 <오라클로 배우는 데이터베이스 입문>
- 주안점
  - oracle DB의 아키텍쳐를 분석한다 (eg. lock, memory, index, join)
  - 같은 결과 다른 성능인 두 코드를 비교한다
  - 운영에 필요한 세부 기능을 학습한다





#### [04_Linux 서버 관리](./04_Linux/README.md)

- 목적 : 리눅스 서버에 대해 이해하자
- 기간 : 2022/08/08 ~ 2022/08/14
- Ref
  - 책 <UNIX/Linux 시스템 관리자를 위한 쉘 스크립트 활용 가이드>


#### [05_EffectiveJava](./05_EffectiveJava/README.md)

- 목적 : 자바 언어의 특징을 이해하자
- 기간 : 2022/09/28 ~
- 방식 : 3인 스터디로 매주 아이템 3개씩.
- Ref
  - 책 <Effective Java>