## 02_k8s 배포

### 아키텍쳐
- 가정 : API 서버, MySQL 서버 두 개의 MSA가 있다
- 노드가 죽을 위험에 대비하기 위해, MSA 별로 container - pod - deployment - service 를 분리한다
- 두 MSA 간 통신 : Service 간에 통신한다. hostname 필드에 지정된 값으로 DNS 서버에서 IP 값을 구한다
- 고객과 전체 서비스간 연결 : Ingress 에 하위 url에 대해 매칭할 service 를 지정할 수 있다

### 기능
- pod : 이미지 기반으로 실행한 컨테이너를 담고 있다
- controller : pod의 운영 전략에 따라 알맞은 컨트롤러를 선택한다
    - deployment : 무중단 운영
    - job : 배치 처리
    - cronjob : 크론잡 처리
- service : pod 외부로의 통신을 처리한다. 
- ingress : application layer 의 네트워크 환경설정을 해준다. domain 설정, 보안 설정 등을 할 수 있다.

### helm chart 
- 이전 
  - pod, controller, service, ingress 별로 yaml 파일을 작성했었다. 
  - 변경할 내용이 있다면 해당 yaml 파일에 접근해야 한다.
  - 다른 사람이 yaml 파일의 내용을 파악하기가 어렵다.
    
- 이후
  - values.yaml과 다른 yaml 파일이 golang을 활용해 연동되어 있다.
  - values.yaml만 수정하면 된다.
    

### 주의할 점
- 아키텍쳐
    - 상용 서비스 버전
      - ingress
        - db service : db pod - dp deployment
        - web service : web pod - web deployment
    - 간단한 버전
      - ingress - service : pod of fastapi with sqlite - deployment
    

- 통신 시 IP
    - docker : container_name 을 IP 주소로 활용함 👉 cotainer_name
    - k8s : pod 내 통신 👉 localhost
    - k8s : pod 밖 통신 👉 service 의 hostname : pod port  
    

- name과 label
    - name : 리소스의 이름. 단순한 명칭. 
    - label : 오브젝트를 구분하는 카테고리 id
    - service, deployment 가 관리하는 pod 의 label로 잘 연결해주자
    
    

    