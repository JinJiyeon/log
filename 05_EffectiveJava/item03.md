## 아이템03. private 생성자나 열거 타입으로 singleton 임을 보증하라

- [LazyHolder](https://limkydev.tistory.com/67)
- [JVM Load & Initialize class](https://javarevisited.blogspot.com/2012/07/when-class-loading-initialization-java-example.html#axzz7gzb76iIK)
- [Java Inner Class 의 로딩 시점](https://kdhyo98.tistory.com/70)


### 싱글톤을 만드는 방식

- 생성자는 private으로 감춰둔다
- public static 멤버 변수/메소드로 유일한 인스턴스에 접근한다

```java
pubcli class Elvis {
    public static final Elvis INSTANCE = new Elvis();
    private Elvis() {...}
}

// 클래스 로딩될 때에 static 메소드로서 Elvis 생성
// Elvis.INSTANCE 로 접근
```

```java
public class Elvis {
    private static final Elvis INSTANCE = new Elvis();
    private Elvis() {...}
    public static Elvis getInstance() { return INSTANCE; }
}

// 클래스 로딩될 때에 static 멤버 변수로서 Elvis 생성
// Elvis.getInstance 로 접근
```

### 싱글톤을 만드는 방식 (LazyHolder)
- 위 두 방식은 클래스 로딩될 때에 Elvis를 생성한다. Elvis 생성 비용이 큰데 사용하지도 않을 경우, 비효율적일 수 있다.
- Elvis를 사용할 때에 생성하는 로직을 구현하자. 이때에 동시성 문제에 주의해야 한다.

```java
public class Elvis {
    private Elvis() {}
    private static class LazyHolder {
        private static final Elvis INSTANCE = new Elvis();
    }
    private static Elvis getInstance() {
        return LazyHolder.INSTANCE
    }
}
```
- 내부 클래스는 호출될 때 초기화된다!!
    - Loading은 .class로 변환한 파일을 메모리에 적재하는 것이다
    - Initialization은 로딩한 클래스의 static 멤버 변수를 등록하는 것이다
        - 멤버 변수 vs 로컬 변수
    - outer class를 호출하면 -> outer class를 초기화하고 inner class는 로드만 된다.
    - inner class를 호출하면 -> inner class를 초기화한다


- Elvis 클래스를 호출하면 Elvis가 로딩되고 초기화된다
- Elvis가 초기화되면 무엇이 로드/초기화되는가?
    1) LazyHolder는 static inner class 이므로 로드만 된다
    2) LazyHolder는 초기화되지 않았다. 따라서 INSTANCE는 생성되지 않았다
    3) getInstance는 static이므로 로드된다
- INSTANCE는 언제 생성되는가?
    - getInstance를 호출하면 LazyHolder가 호출되고 초기화된다. 이때 static 영역에 INSTANCE가 싱글톤으로 생성된다.
- LazyHolder 는 thread safe한가?
    - if문으로 구현하나 LazyHolder로 구현하나 로직은 비슷하다. static 메모리를 체크하고 없으면 elvis를 생성한다.
    - if문은 동시성 문제가 발생할 수 있고 LazyHolder는 thread safe한가? 왜? cpu는 자바를 코드 한줄씩 수행하나? 코드 한 줄은 lock이 걸리나?


### 싱글톤으로 캐시 구현하기

- 업무에서 순수 자바로 캐시를 구현하는 일이 있었다.
- 캐시를 구현하려면
    - 멤버 ; 저장할 객체, updatedTime
    - 메소드 ; readFromDB, reloadFromDB
