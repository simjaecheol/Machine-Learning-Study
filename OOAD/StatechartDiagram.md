# Statechart Diagram

- Activity Diagram과 그리는 방식과 의미가 반대

## Introduction
- Every object takes a finite number of different states during its life.
- State machine(=Statechart) diagram is used as follows:
  - to model the possible states of a system or object
  - to show how state transitions occur as a consequence of events
  - to show what behavior the system or object exhibits in each state

## State

- States: noes of the state machine
- When a state is active,
  - The object(or system) is in that state.
  - All internal activities specified in this tate can be executed.
    - An activity can consist of multiple actions
- State operations
  - entry
    - Executed when the object enters the state
  - exit
    - Executed when the object exits the state
  - do
    - Executed when the object remains in this state

## Transition

- Change from one state to another
  - Source state
  - Target state
  - Transition
  - Event
  - Guard: 옵션
  - Sequence of actions: 전환시 수행되는 행동들

## Composite State

- Synonyms: complex state, nested state(-> OR state)
- Contains other states -> substates
  - Only one of its substates is active at any point in time.
  - Arbitrary nesting depth of substates.

## Orthogonal State
- Composite state is divided into two or more regions seperated by a dashed line (-> AND State)
  - One state of each region is always active at any point in time.
  - concurrent substates

- Entry: Transition to the boundary of orthogonal state activates the initial states of all regions
  - parallelization node
- Exit: Final state must be reached in all regions to tigger completion event
  - synchronization node: Dead lock checking

## Submachine State(SMS)
- To reuse parts of state machine diagrams in other state machine diagrams
  - Notation: state:submachineState

- As soon as the submachine state is activated, the behavior of the submachine is executed.
  - Corresponds to calling a subroutine in programming languages.

## History State
- To remembers which substate of a composite state was the last active one
  - Activates the "old" substate and all entry activities are conducted sequentially from the outside to the inside of the composite state
- Shallow history state restores the state that is on the same level of the composite state.
  - H
  - 수행 도중 나가면 다시 들어올 때 그 state에 처음부터 시작
- Deep history state restores the last active substate over the entire nesting depth.
  - H*
  - 수행 도중 나간 후 다시 들어올 때 이전 상태를 바로 돌아오는 것

## Quiz

### 다음의 Statechart Diagram에 대한 설명 중 올바르지 않은 것은? 4번

```
1. Statechart Diagram은 시스템 뿐만 아니라 프로세스 및 클래스/객체 수준에서도 작성할 수 있다.
 - operation 수준에서도 가능
2. Statechart Diagram은 모델링 대상 시스템 상태변화를 event[condition]/action 기반의 transition으로 표현한다.
3. Statechart Diagram은 모델링 대상의 Hierarchical Structure를 표현하는데 어려움이 없다.
4. Statechart Diagram을 사용하면 시스템이 주고 받는 events(stimulus/action)를 시간 순서대로 정확히 표현할 수 있다.
```

### 다음의 Statechart Diagram에서, start e1, e2, e10, e9의 순서로 이벤트가 차례대로 발생되는 경우, 도달된 상태는 무엇인가요?

S5 -> S1 -> S1.1 -> S1.2 -> S5 -> H -> S1.1