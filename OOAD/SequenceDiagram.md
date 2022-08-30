# Sequence Diagram
## Interaction Diagrams

- Interaction Diagrams illustrate how objects interact via messages.
  - Dynamic object modeling
  - Sequence diagram
  - Communication diagram
  - Timing diagram
  - Interaction Overview diagram

### Sequence and Communication Diagram

- Sequence Diagram
  - model the collaboration of objects based on a time sequence.
- Communication Diagram
  - focus on showing the collaboration of objects rather than time sequence.
  - 번호가 없는 것이 system operation

### Basic Communication Diagram Notations

- Link and Message
  - A connection path between two objects indicating some form of possible navigation and visibility between the objects
  - All messages flow on the same line and many messages may flow along a link
    - Each message between objects is represented with a message expression and small arrow indicating the direction of the message.
    - A sequence number is added to show the sequential order of message in the current thread of control.

### Basic Sequence Diagram Notations

- Lifeline boxes and lifelines
  - execution specification
- Messages
- Lifeline box
  - Represent the participants(roles) in the interaction, informally and partically
    - object(s), class, subsystem, component, etc.

### 3 Types of Messages
- Synchronous message
  - Sender waits until it has received a response message before continuing.
  - An execution specification is inserted at target.
- Asynchronous message
  - Sender continues without wating for a response message.
- Response message
  - May be ommitted if content and location are obvious

### Message Syntax

return = message(parameter: parameterType) : returnType

- For example:
  - d = getProductDescription(id)
  - d = getProductDescription(id: itemID)
  - d = getProductDescription(id: itemID) : ProductDescription

### Other Types of Messages

- Found message
  - Sender of a message is unknown or not relevant.
- Lost message
  - Receiver of a message is unknown or not relevant
- Time-consuming message
  - Message with duration: Express that time elaspses between the sending and the receipt of a message
  - Usually messages are assumed to be transmitted without any loss of time.

### Singleton Objects

- There is only one instance of a class instantiated: a singleton object
  - Implying to the Singleton design pattern
  - 표기: box 안 오른쪽 상단부에 1로 작성

### Instance Creation

- To create an instance of a class
  - The UML mandates dashed line.
  - The message name create is not required; anything is legal.
    - But, it's a UML idiom.
  - create되는 객체 box가 화살표와 연결되어야함

### Object Destruction

- To show explicit destruction of an object
  - The << destory >> stereotyped message, with the large X and short lifeline indicates explicit object destruction.

### Combined Fragments and Operators

- 12 predefined types of operators
  - Model various control structures with frames
    - Frames: region or fragments of the diagrams, which has an operator and a guard
  - Frame are nested.

- Branches and loops
  - alt Fragment
    - To model alternative sequences
    - Similar to switch statement in Java
      - Guards are used to select the one path to be executed.
    - Guards
      - Modeled in square brackets
      - default: true
      - predefined: [ else ]
    - Guards have to be disjoint to avoid non-deterministic behavior.
  - opt Fragment
    - To model an optional sequences
    - Simliar to if statement without else branch
      - Exactly one operand
      - Actual execution at runtime is dependent on the guard
  - loop Fragment
    - To model repeatedly-executed sequences
      - Exactly one operand
    - Keyword loop followed by the minimal/maximal number of iterations
      - (min..max) or (min, max)
      - default: (*) .. no upper limit
    - Guard
      - Evaluated as soon as the minimum number of iterations has taken place
      - Checked for each iteration within the (min, max) limits
      - If the guard evaluates to false, the execution of the loop is terminated.
  - break Fragment
    - similar to exception handling
      - Exactly one operand with a guard
    - If the guard is true:
      - Interactions within this operand are executed.
      - Remaining operations of the surrounding fragment are omitted.
      - Interaction continues in the next higher level fragment.

| Operator | Purpose |
| --- | --- |
| alt | Alternative interaction |
| opt | Optional interaction |
| loop | Repeated interaction |
| break | Exception interaction |

- Concurrency and order
  - seq Fragment
    - Default order of events
    - Weak sequencing:
      - Events on different lifelines from different operands may come in any order.
      - Events on the same lifelines from different operands are ordered such that an event of the first operand comes before that of the second operand.
  - strict Fragment
  - par Fragment
  - critical Fragment

| Operator | Purpose |
| --- | --- |
| seq | Weak order |
| strict | Strict order |
| par | Concurrent interaction |
| critical | Atomic interaction |

- Filters and assertions
  - ignore Fragment
  - consider Fragment
  - assert Fragment
  - neg Fragment

| Operator | Purpose |
| --- | --- |
| ignore | Irrelevant interaction |
| consider | Revalnt interaction |
| assert | Asserted interaction |
| neg | Invalid interaction |

### Interaction References

- Integrates one sequence diagram in another sequence diagram
  - sd

### Iteration Over a Collection
- Sending the same message to each object to iterate over all members of a collection(such as list or map)
  - The selector expression(as lineItems[i] in the lifeline) selects one object from a group
  - Lifeline participants should represent one object, not a collection.

### What is the Relationship between Interaction and Class Diagrams?

- From interaction diagrams, class diagrams can be generated iteratively
  - When we draw interaction diagrams, a set of classes and their methods emerge.
  - Two complementary dynamic and static views are drawn concurently and iteratively.
  - OOD에서도 중요한 역할
    - Sequence에서 클래스 다이어 그램을 그릴 때 참조

## Quiz

### UML Interaction Diagrams에 대한 다음의 설명 중 올바른 것은? 1번

```
1. Interaction Diagram은 4가지 다이어그램에 대한 통칭이며, 실제로 그릴수 있는 다이어그램은 아니다. (O)
2. Sequence Diagram은 Communication Diagram보다 더 Expressive Power가 강력하다. (X) - 동일
3. Communication Diagram은 Sequence Diagram보다 더 Expressive Power가 강력하다. (X) - 동일
4. Interaction Overview Diagram은 더 큰 시나리오를 하나의 Interaction Diagram으로 그리는 방법이다. (X)
```

- 4. 더 큰 시나리오를 여러 개의 Interaction Diagram으로 그리는 방법.
- 4. 더 큰 시나리오를 하나의 Flow chart로 그리는 방법

### 다음의 Sequence Diagram의 Message에 대한 설명 중 올바르지 않은 것은? 4번

```
1. Synchronous Message는 Sender가 메시지를 보낸 후, Response Message가 올 때까지 기다린다.(O)
2. Asynchronous Message는 Sender가 메시지를 보낸 후, Response Message를 기다리지 않는다.(O)
3. Response Message는 생략이 가능하다.(O)
4. 일반적으로 수평선으로 그려진 Message는 전송시간을 적게 소비하는 Message이다.(X)
```

### 다음의 Sequnce Diagram에서 해석이 불가능한 메시지 전송순서를 고르세요. 4번

