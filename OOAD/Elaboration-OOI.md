# Elaboration - Object-Oriented Implementation

- Visibility
- Mapping

## Chapter 19. Designing for Visibility

- Class Design
- 코드 구현

### Visibility Between Objects

- In message passing between objects
  - For a sender object to send a message to a receiver object, the receiver must be visible to the sender.
    - The send must have some kind of reference or pointer to the receiver object.

### Visibility

- Visibility is the ability of an object to "see" or "have a reference to" another object.
  - When an object A sends a message to an object B, B must be visible to A
  - The issue of scope: "Is one resource(such as an instance) within the scope of another?"
  - 4 common ways that visibility can be achived from objectA to objectB:
    - Attribute visibility: B is an attribute of A
    - Parameter visibility: B is a parameter of a method of A
      - ---> (dependency)
      - temporary
    - Logical visibility: B is a(non-parameter) local object in a method of A.
    - Global visibility: B is in some way globally visible.(C++, not Java)

### Attribute Visibility

- Attribute visibility from A to B exists, when B is an attribute of A.
  - Relatively permanent visibility, because it persist as long as A and B exist.
  - Very common form of visibility, in object-oriented systems.

### Parameter Visibility

- parameter visibility from A to B exist, when B is passed as a parameter to a method of A
  - Relatively temporary visibility, because it persists only within the scope of the method.
  - The second most common form of visibility in object-oriented systems

### Parameter to Attribute Visibility

- It is common to transform parameter visibility into attribute visibility.

### Logical Visibility

- Logical visibility from A to B exists, when B is declared as a local object within a method of A

  - Relatively temporary visibility, becasue it persists only within the scope of the method.
  - As with parameter visibility, it is common to transform local visibility into attribute visibility

- Two common ways for local visibility:
  - Create a new local instance and assign it to a local variable.
  - Assgin the returning object from a method invocation to a local variable.

### Global Visibility

- Global visibility from A to B exists, when B is global to A.

  - Relatively permanent visibility, because it persists as long as A and B exist.
  - The least common form of visibility in object-oriented systems.

- One way to achieve global visibility is

  - assgin an instance to a global variable, which is possible in some language such as C++, but not others, such as Java.

- The preferred method to achive global visibility is to use the Singleton pattern

## Chapter 20. Mapping Designs to Code

- Mapping or Translation

### Mapping Designs to Code

- The UML artifacts created during the design work(interaction diagrams and DCDs) will be used as input to the code generation process.

- Implementation in an OO language requires writing source code for:

  - class and interface definitions
  - method definitions

- A translation from UML designs to code is requried.
  - from class diagrams to class definitions
  - from interaction diagrams to method bodies.

### Creating Class Definitions from DCDs

- DCDs are sufficient to create a basic class definition in an OO language.

### Creating Methods from Interaction Diagrams

- The sequence of the messages in an interaction diagram translate to a series of statements in the method definitions

### Order of Implentation

- Classes need to be implemented from leat-coupled to most-coupled.

## Quiz

### 다음의 설명 중 올바르지 않은 것을 고르세요. 4번

```
1. UML Package Diagram은 Logical Architecture를 표현한다.
2. UML Deployment Diagram은 Physical Architecture를 표현한다.
3. Layer는 비슷한 기능을 수행하는 Class Package 또는 Subsystem 등을 모아놓은 것이다.
4. Layer는 Physical Architecture로서 UML Deployment Diagram으로만 표현되는 것이 바람직하다.
- Tier Architecture
```

### Visibility에 대한 다음의 설명 중 올바른 것은? 3번

```
1. Visibility는 한 Object가 다른 Object에 정의된 모든 Attributes와 Operations을 볼 수 있는 능력을 의미한다.
2. Object A에서 Object B로 보낼 때, A는 B에게 보여야만 한다.
3. Attribute Visibility는 가장 기본적이고 많이 사용되는 Visibility로서, Class Diagram을 통해서 확인할 수 있다.
4. Parameter Visibility는 Logical Visibility로 쉽게 바꿀 수 있다.
```