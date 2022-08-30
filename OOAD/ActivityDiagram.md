# Activity Diagram

- Activity diagrams represent the dynamics of the system.
  - shows the flow of actions in system.
  - show:
    - The flow of control from activity in the system
    - Alternative paths through the flow
      - decision을 보여줄 수 있음
    - The parallel, branched and concurrent flow of the sytem.
  - shows no flow of messages from one activity to another.
    - 데이터의 흐름을 볼 수 없다.(-> Data Flow Diagram)
  - shows the flow of operations in methods/functions.

## Activity / Transition

- Activity
  - The core symbol
  - rectangle with rounded ends
  - meaningful name
  - No trigger, 끝나면 넘어감.
- Transition
  - shos the flow(sequence) between activities
  - arrow with open arrow head ->

## Branching
- Guard conditions do not have to be mutually exclusive, but it is advisable that they should be.

## Objects
- Object flows
  - dashed arrow
- Objects
  - rectangle
  - with name with object undefined
  - optionally shows the state of the object in square brackets.

## Swimlanes
- Swimlanes
  - vertical columns: Role
  - labelled with the person, organisation or department responsibile for the activities in that columns
  - 항상 표현할 필요는 없다.

## Activity Diagram vs. Statechart Diagram

- Activity diagram is flow of functions without trigger (event) mechanism, while Statechart Diagram consists of triggered states.
  - Statechart diagram performs actions in response to explicit events.
  - In contrast, Activity diagram does not need explicit events but rather transitions from node to node its graph automatically upon completion of activities.

## Quiz

### 다음 중 Activity Diagram에 대해 바르게 설명한 것은 무엇인가요? 2번

```
1. Activity Diagram은 클래스의 활동을 나타낸 것으로, 하나의 클래스마다 하나씩 작성되어야 한다.
2. Activity Diagram은 시스템 수준에서 작성할 수 있고, 하나의 오퍼레이션 수준에서도 작성할 수 있다.
3. Activity Diagram은 모든 다이어 그램보다 먼저 작성되어야 하는 중요한 설계도이다.
 - Optional
4. Activity Diagram은 복잡해지면 적절히 중첩되어서 표현할 수 있다.
 - Flat only
5. Activity Diagram은 전체 Objects의 상호작용을 한 장에 표현한 것이다.
 - Class Diagram
```

### 다음 중 동시에 실행되는 Activity는 무엇인가요? 2번