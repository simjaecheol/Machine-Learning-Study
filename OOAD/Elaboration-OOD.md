# Elaboration - Object-Oriented Analysis

## Chapter 12. Requirements to Desgin Iteratively

### Iteratively Analysis and Design

- In iterative development, a transition from requirements/OOA to design/implementation occur in each iteration.

## Chapter 13. Logical Architecture and UML Package Diagrams

### Software Architecture

- "A software architecture is the set of signficant decisions about the organization of a software system,
  - the selction of the structural elements and ther interfaces by which the system is composed, together with behavior as specified in the collaborations among those elements
  - the composition of these structure and behavioral elements into progressivly larger subsystems,
  - and the architectural style that guids this organization - these elements and ther interfaces, their collaborations, and their composition."
    - Booth, G, Rumbaugh, J and Jacobson, I 1999

### Logical Archituecture

- large-scaled organization of the softwrare classes into packages, subsystems, and layers.

  - no decision about how these elements are deployed accross different operating system processes or across physical computers in a network.
    - 실제 Architucture: the deployment architecture(-> UML Deployment Diagram)

- **UML Package Diagrams** illustrate the logical archituecture.

  - Can also be summarized as Views in a Software Architecture Document(AD)

- **Layer**
  - A very coarse-grained grouping of classes, packages, or subsystems that has cohesive responsibility for a major aspect of the system.
  - Organized such that "higher" layers call upon services of "lower" layers.
  - Can be depicted easily with UML package diagrams

### Layered Architecture

- Typical layers in object-oriented systems:

  - User Interface layer
  - **Application Logic and Domain Objects** layer
    - SW objects representing domain concepts that fulfill application requirements
  - Technical Service Layer
    - General purpose objects and subsystems that provide supporting technical services, such as interfacing with a database or error logging.
    - Usually application-independent and reusable across several systems.

- Layer types
  - UI
  - **Business Logic** - our focus
  - Kernel or OS

### Applying UML: Package Diagrams

- UML package diagram are often used to illustrate the logical architecture of a system.

### Mapping Code Organization to Layers and UML Packages

- Most popular OO languages provide support for packages

### Connections Between SSDs, System Operations and Layers

- In a well-designed layered architecture,
  - The UI layer objects will forward or delegate the request from the UI layer(system operations) on to the domain layer for handling.
  - The messages sent from the UI layer to the domain will be the message illustrated on the SSDs.

## Chapter 14. On to Object Design

- Static Model: Class Diagram
- Dynamic Model: Sequence Diagram

### Designing Objects: Static vs. Dynamic

- Staic models

  - help design the definition of packages, class names, attributes, and method signatures(but not method bodies).
    - UML class diagram

- Dynamic model

  - help design the logic, the code, or the mothod bodies.
    - UML interaction diagram(sequence diagram, communication diagram)

- Relationship between static and dynamic modeling:
  - Spend a short period of time on interaction diagrams, then switch to a wall of related class diagrams.

### Staic Object Modeling

- People new to UML tend to think that the important diagram is the static view class diagram
  - static and dynamic modeling are all important equivalently.
  - The most common static object modeling is with UML class diagrams.

- Static UML Tools
  - **Class Diagram**
  - **Package Diagram**
    - Logical
  - Deployment Diagram
    - H/W, Physical

### Dynamic Object Modeling

- Most useful design work happends while drawing the UML dynamic-view interaction diagrams
  - During dynamic object modeling(such as drawing sequence diagrams), we really think the exact details of what objects need to exist and how they collaborate via messages and methods

- Dynamic UML Tools:
  - Interaction diagrams(Sequence diagram)
  - Statechart diagram
    - Control
  - Activity diagram
    - Business Logic

### Object-Oriented Design Skill over UML Notation Skill

- The **object design skills** are matter, not knowing how to draw UML
  - Since, Drawing UML is a reflection of making decisions about the design.

- Fundamental object design requires knowledge of:
  - Principles of responsibility assignment(GRASP)
    - 아무것도 없는 상태에서 시작
    - 9개의 샘플
    - 초심자용
  - Design patterns of GoF
    - 23 디자인 패턴
    - System reuse을 위해

## Chapter 15. UML Interaction Diagrams

## Chapter 16. UML Class Diagam

## Quiz

### 다음의 Object Design에 대한 설명 중 올바르지 않은 것은? 3번

```
1. Static 모델은 클래스나 패키지를 정의하는데 도움이 되며, 클래스 다이어그램, 패키지 다이어그램 등이 해당된다.
2. Dynamic 모델은 메소드나 로직등을 정의하는데 도움이 되며, Interaction 다이어그램, Statechart 다이어그램 등이 해당된다.
3. 클래스 다이어그램으로부터 스켈레톤 코드를 생성하고 구현을 시작하므로, Static 모델이 가장 중요한 Object Model이다.
4. UP 기반의 OOAD에서는 현 Iteration에서 개발할 Use Case에 대해서, Interation Diagram과 Class Diagram을 반복적이고 점증적으로 작성한다.
```

### UML Interaction Diagrams에 대한 다음의 설명 중 올바른 것은? 1번

```
1. Interaction 다이어그램은 4가지 다이어그램에 대한 통칭이며, 실제로 그릴 수 있는 다이어그램은 아니다.
2. Sequence 다이어그램은 Communication 다이어그램보다 더 Expressive Power가 강력하다.
3. Communication 다이어그램은 Sequence 다이어 그램보다 더 Expressive Power가 강력하다.
4. Interaction Overview Diagram은 더 큰 시나리오를 하나의 Interaction Diagram으로 그리는 방법이다.
- Flowchar(Activity Diagram)으로 그리는 방법
```

### UML Object Model에는 Static Model과 Dynamic Model 두 종류가 있습니다. 각각을 대표하는 UML diagram은 무엇인가요? 또 이 두 모델이 서로 어떤 관계를 가지면서 어떻게 사용되는지 설명하세요.

```
Static: Class Diagram
Dynamic: Sequence Diagram

Class Diagram으로 스켈레톤을 만든 후 Sequence Diagram을 사용하여 Operation의 기능을 채운다.
```