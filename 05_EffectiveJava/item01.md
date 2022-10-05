## 아이템1. 생성자 대신 static factory method를 고려하라

[참고 블로그](https://tecoble.techcourse.co.kr/post/2020-07-16-static-method/)

생성자 Car() 대신, createCar() 같은 메소드를 만들어라. 그리고 <b>static</b> 으로 만들어라



### static method

특징

- 클래스가 컴파일될 때 static 메모리에 올라간다
- 인스턴스를 생성하지 않고도 메소드에 접근할 수 있다. 

장점

- 인스턴스 생성에 비용이 드는 경우 효율적이다. 유틸리티 함수에서 많이 쓰인다. Math.max() 에서 Math 인스턴스를 생성하지 않고도 max 메소드를 쓸 수 있다.

단점

- 메모리에 부담이 갈 수 있다.
- 정적메소드는 상속이 안 된다









