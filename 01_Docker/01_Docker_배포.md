## 01 Docker 배포

- Docker란?
  - 환경설정 배포 & 설치를 쉽게 해주는 프로그램!
  - 프로그램을 실행할 때 필요한 OS, 패키지, 라이브러리 등을 이미지로 만들어서 관리한다
  - 프로세스를 격리해서 가상환경을 만든다. 가상화 OS를 만드는 것보다 더 가볍고 빠르다.



- build

  - 배포 환경을 이미지로 만들려면 CLI / Dockerfile / Docker-compose 세가지 방법이 있다.

    - Dockerfile은 yaml 파일로 {베이스 이미지, 실행할 명령어, 실행할 파일} 등을 지정할 수 있다.
    - Docker-compose 는 여러 개의 컨테이너를 띄울 때에 사용한다.

  - YAML 문법

    

  [Dockerfile 예시](./03_Docker/Dockerfile)

  [Docker-compose 예시](./03_Docker/docker-compose.yaml)



- pull
  - 로컬이나 도커 허브에서 이미지를 다운로드한다.
  - 다운로드한 이미지를 바탕으로 가상환경을 만드는데, 이것을 컨테이너라고 한다.
  - 도커 커맨드 or Dashboard 를 활용해서 이미지와 컨테이너를 관리한다.



- 컨테이너 간 통신
  - network를 생성하고 통신할 컨테이너를 넣어준다.
  - IP 주소는 컨테이너 이름이 DNS 서버에 등록된다.



- 사용 상 주의점
  - Docker-compose build 를 안하면 이전에 빌드된 이미지만 사용한다