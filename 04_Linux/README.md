## [04_Linux 서버 관리](./04_Linux)

- 목적 : 리눅스 서버에 대해 이해하자
- 기간 : 2022/08/08 ~ 2022/08/14
- Ref
  - 책 <UNIX/Linux 시스템 관리자를 위한 쉘 스크립트 활용 가이드>



## 아키텍쳐

- 접근 권한과 chmod

  - 접근 권한

    🔴 🟡🟡🟡 🔵🔵🔵 🟣🟣🟣

    - 🔴 : 파일의 유형, 🟡 : user, 🔵 : group, 🟣 : others

    - 파일의 유형 : { d : directory, l : link, - : normal file }

    - 권한의 유형 : { r : read, w : write, x : exec }

    - 권한을 8 bit로 표현하기도 한다.

      eg) `drwxr-xr-x` : 0755, `-rw-r--r--` : 0644

      

  - 명령어

    ```linux
    # 접근권한 확인
    ls -l /test_directory | less
    
    # 권한을 바꾸고 싶을 때 chmod
    chmod u+x, go+r test_file
    
    # 기본값을 바꾸고 싶을 때 umask
    umask 0022
    ```

    

  - 특수 권한

    - setuid, setgid, sticky bit 가 있다.
      exec 자리에 x 대신 s, s, t로 표시된다.
      bit로 표현하면 4000, 2000, 1000 이다.
    - setuid
      - 프로그램을 실행하면 소유자 id로 잠시 변경된다.
      - root 만 접근할 수 있는 파일이나 명령에, 일반 사용자로 접근하고 싶을 때 사용한다.
    - sticky bit
      - 누구나 사용할 수 있지만, 파일 삭제와 이름 변경은 root 만 할 수 있다.

  - 명령어

    ```linux
    # setuid가 4000인 파일 찾기
    find /test_route -type f -perm 4000
    sudo find /test_route -user root -perm 4000
    
    # setuid 설정하기
    sudo chmod u+s test_file
    ```

    

- file descriptor와 redirection

  - file descriptor 

    - 각 프로세스는 descriptor 를 갖고 있다.

    - 기본적으로 { 0: stdin, 1: stdout, 2: stderr }를 갖고 있고 추가된다.

  - 꺽쇠의 방향과 개수

    - command > file : 덮어쓰기

    - comman >> file : 이어쓰기
    - command < file : 불러오기

  - 명령어

    ```linux
    echo hello > test_file
    ls -l | grep zip >> test_file
    cat < test_file
    ```



- 주요 명령어
  - find : 파일 찾기
  - grep : regex 로 파일 찾기
  - sed : 스트리밍 편집기
  - awk : 리눅스의 pandas



## 실습

- 주의사항
  - sh는 #!/bin/sh 로 시작해야 한다.
  - sh는 = 전후에 공백없이 입력해야 한다.
  - awk 'condition {action}'
  - 변수 확장 ' ' (X),  " " (O)

- 시스템 관리
  - 0501) 대용량 파일이 존재하는지 점검하기
  - 0502) user 계정 잠금하기
  - 0503) 재부팅 시 해당 시점으로 복구하기

- 시스템 보안
  - 0601) setuid + root 소유인 파일 찾기
    