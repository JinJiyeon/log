## 아이템02. 생성자에 매개변수가 많다면 Builder를 고려하라

python의 `def method(name=required, color=red)` 를 자바에서 구현하려면 Builder 패턴이 좋다.

빌더 패턴 = 점층적 생성자 패턴 + 자바빈즈 패턴





### 기존 패턴의 한계

- 점층적 생성자 패턴
  - 매개변수 유무에 따라 생성자를 다 만든다 (2^n)
  - 매개변수의 변수 타입이 같을 경우 문제는 더욱 복잡해진다
- 자바빈즈 패턴
  - 필드에 기본값을 생성해둔다. `setField(int val)`로 필드에 값을 할당한다.
  - 기본값을 세팅해둘 수 없다. 동시성 문제가 발생할 수 있다.





### 빌더 패턴

- 기본값을 세팅해둘 수 있다
- 재귀적으로 인스턴스를 호출하면서 값을 세팅해나간다. 
  점층적 생성자 패턴에서는 2^n개를 만들어야 했는데 👉 생성자 1개 with n줄이면 해결된다!

```java
public class NutritionFacts {
  private final int servingSize;
  private final int servings;
  private final int calories;
  private final int fat;
  private final int sodium;
  private final int carbohydrate;
  
  public static class Builder {
    // 필수값
    private final int servingSize;
    private final int servings;
    
    // 기본값
    private int calores = 0;
    private int fat = 0;
    private int sodium = 0;
    private int carbohydrate = 0;
    
    // 기본 생성자
    public Builder(int servingSize, int servings) {
      this.servingSize = servingSize;
      this.servings = servings;
    }
    
    public Builder calories(int val) {
      calories = val; return this;
    }
    public Builder fat(int val) {
      fat = val; return this;
    }
    public Builder sodium(int val) {
      sodium = val; return this;
    }
    public Builder carbohydrate(int val) {
      carbohydrate = val; return this;
    }
    
    public NutritionFacts build() {
      return new NutritionFacts(this);
    }
  }
  
  private NutritionFacts(Builder builder) {
    servingSize = builder.servingSize;
    servings = builder.serving;
   	calories = builder.calories;
    fat = builder.fat;
    sodium = builder.sodium;
    carbohydrate = builder.carbohydrate;
  }
}
```





### this

1) 자신의 참조값을 전달한다
   `this.name = name` 이나 Builder의 `return this` 가 여기에 해당
2) 같은 이름의 생성자
   `this(name, color, 0, 0)`