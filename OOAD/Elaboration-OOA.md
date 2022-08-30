# Elaboration - Object-Oriented Analysis

- OOA -> OOD -> OOI -> OOT - RW(Requirement Workshop)
- Domain Models / Use Case Models / Operation Contracts

- Inception is a short(only one week) step to elaboration including:
  - A short requirement workshop
  - Most actors, goals, and use cases named
  - Most use cases written in brief format(10~20 % are written in fully dressed detail)
  - Most influential and risky requirements identified
  - Version one of the Vision and Supplementary Specification written
  - Risk list
  - Technical proof-of-concept prototypes and other investigations to explore the technical feasibility of special requirements
  - User interface-oriented prototypes to clarify the vision of functional requirements
  - Recommendations on what components to buy/build/reuse, to be refined in elaboration
  - High-level candidate architecture and components proposed
  - Plan for the first iteration
  - Candidate tools list

## Chapter 8. Iteration 1 Basics

### On to Elaboration

- Elaboration is the initial series of iterations during which:
  - The core, risky software architecture is programmed and tested
    - propose는 inception 단계에서도 진행
  - The requirements are discovered and stabilized(fixed).
  - The major risks are mitigated or retired.
    - Architecture
    - Client

### Implemnt Requirements Incrementally

- Incremental development for the same use case across iterations
  - The requirements for the iteration-1 are subsets of the comple requirements or use cases

### UP Artifacts Start in Elaboration

- These will not be compled in one iteration; rather will be refined over series of iteration
  - iteration: 3주

| Artifact                            | Comment                                                                                                                                                                                      |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Domain Model (OOA)                  | This is visualization of the domain concepts; it is similary to a</br>static information model of the domain entities                                                                        |
| Design Model (OOD)                  | This is the set of diagrams that describes the logical design.</br>This includes software class diagrams, object interaction diagrams, package diagrams and so forth</br>                    |
| Software Architecture Document      | A learning and that summarizes the key architectural issues and</br>thier resolution in the desgin. It is a summary of the </br>outstanding design ideas and their motivation in the system. |
| Data Model                          | This includes the database schemas, and the mapping</br> strategies between object and non-object representation.                                                                            |
| Use-Case Storyboards, UI Prototypes | A description of the user interfaces, paths of navigation, usability</br>models, and so forth.                                                                                               |

- Software Architecture Documentation
  - Elaboration에서 시작

### The Relationship of UP Artifacts in One Iteration

- Domain Model
- Use-Case Model
  - Use Caes
  - SSD
- Design Model

## Chapter 9. Domain Models

- The UP Domain Model is usually both started and completed in the elaboration phase.

### Domain Model

- Domain model is a visual representation of conceptual classes or real-situation objects in a domain

  - The most importance classic model in OO analysis
  - Can act as a source of inspiration for designing software objects and classes
  - Visual dictionary of the noteworthy abstractions, domain vocabulary, and information contents of the domain
  - Not represents software objects

- Domain modjel is illustrated with class diagrams

  - no operations
  - attributes only
  - domain objects(or conceptual classes)
  - associations between conceptual classes
  - attributes of conceptual classes

- Domain model is a kind of preliminary version of class diagram, if we are well used to the application domain
  - 전제 조건: 이미 도메인 모델에 대한 충분한 지식이 있을 경우

### What Create a Domain Model?

- Two reasons to create a domain model

  - Getting to know the domain during elary elaboration iterations, understanding the concepts involved and their relationships
  - Inspiring the software classes of the domain layer in the design model.
    - This prevents software from being far away from the reality of the doamin.
    - lower representation gap: Use software class names in the domain layer inspired from names in the domain model, with object having domain-familiar information and responsibilities.

- Class Diagram의 Association 선만 사용

### Domain Model is Not Software Objects

- A UP domain model is not of software objects such as:
  - Software classes(i.e. C++ or Java classes)
  - Elements representing artifacts related to the implementation of the system(e.g. a dataclass or a window)
  - Methods(operations)

### Lower Representation Gap

- OOA - OOD

### How to Create a Domain Model

- Same as the way of creating class diagrams.

  - Find conceptual classes and draw them in a UML class diagram
  - Add associations and attributes to conceptual classes.

- Identification of Noun Phrases
  - Identify the nouns and noun phrase in a textual description of the domain, and consider them as candidate conceptual classes and attributes.

### Is the Doamin Model Correct?

- There is no such thing as a single correct domain model.

  - All models are approximations of the domain we are attempting to understand
  - 이해 당사자 간의 도메인 모델은 모두 다르다.

- The domain model is a primary tool of understanding and communication among a particular group
  - Correct << Useful

## Chapter 10. System Sequence Diagram

### System Sequence Diagram

- System sequence diagram(SSD)

  - A picture that shows the events that external actors generate, their order, and inter-system events, for one particular scenario of a use case.
    - the external actors that interact directly with the system.
    - the system(as a **black box**)
    - the system events that the actors generate
  - Use sequence diagram notation
  - Depict system behavior in terms of what the system does, not how it does it
  - Used as input to object design -> System operations

- Use cases describe how external actors interact with the software system we are interested in creating.
  - Druing this interaction, an actor generates system events to a system, usually requesting some system operation to handle the event.

### Applying UML Sequence Diagrams

- The UML does not define something called "System Sequence Diagrams".

  - Use general UML sequence diagram notation.
  - The term "system" in SSDs is used to emphasize the application of the UML sequence diagram to systems viewed as black boxes.
  - An SSD shows system events for one scenario of a use case.

- System Operation을 찾아내는 과정

- Use Case Model
  - Use Case Diagram + SSD

### System Operation

- System operations
  - Operations that the system as black box component offers in its public interface
  - Show system events, which the SUD should have system operations to handle the system events.
  - System interfaces: The entire set of system operations across all use cases

### Guidline: How to Name System Events and Operations?

- System events should be expressed at the abstract level of intention rather than in terms of the physical input device.

- Example: scan(itemID) vs. enterItem(itemID)
  - The enterItem name is better, since it communicates intention rather than the input device.

### Process: Iterative and Evolutionary SSD

- The UP doesn't mention explicitly SSDs, but we can use them.

  - since the UP is very frexible, allowing any useful technique to be applied in the context.

- Most SSDs are created during elaboration, when it is useful to
  - Identify the details of the system events to clarify what major operations which the system must be designed to handle.
  - write system operation contracts, and possibly to support estimation.

## Chapter 11. Operation Contracts

- Optional, But 중요
- Operation + Contract
  - System Operation 검증 기준(Contract)
- Elaboration Phase가 끝날 때쯤 생성

### Operation Contract

- Operation Contracts
  - Use a **pre- and post- condition** form to describe detailed changes to objects in a domain model, as the result of a system operation.
  - Usually used in a Design Model for object methods.
  - Also used in a domain model as contracts of high-level system operations.

### Postconditions

- Postconditions describe changes in the state of objects in the domain model.
  - Not actions to be performed during the operation
  - Rather, Observations about the domain model objects that are true when the operation has finished(-> past tense)
    - Instance Creation and Deletion
    - Associations Formed and Broken
    - Attribute Modification
  - Only necessary when the outcome of a system operation is not clear from the use case description.
    - It will be helpful when there are situations where the details and complexity of required state change are awkward or too detailed to capture in use cases.

## Quiz

### 다음은 Elaboration 단계에 대한 설명이다. 올바르지 않은 것은? 4번

```
1. The core, risky software architecture is programmed and tested.
2. Most requirements are discovered and stabilized.
3. The major risks are mitigated or retired.
4. High-level candidate SW architecture is proposed.
```

### 다음의 도메인 모델에 대한 설명 중 올바른 것을 모두 고르세요. 2, 3번

```
1. 도메인 모델은 디자인 클래스 다이어그램의 일종이다.
2. 도메인 모델을 그림으로서 앞으로 개발할 SW가 어떤 환경에서 사용될 지를 가늠할 수 있다.
3. 도메인 모델은 나중에 SW로 구현되지 않은 다양한 Conceptual Classes(Object)가 포함된다.
4. 도메인 모델이 준비되면 Correctness 여부를 정확하게 검사한 후에 사용해야 한다.
```

### 다음의 System Sequence Diagram에 대한 설명 중 올바른 것을 고르세요. 1번

```
1. 시스템은 블랙박스 컴포넌트로 간주하고 분석한다.
2. 외부 Actor와 시스템 간의 모든 Interaction을 System Operation으로 선정한다.
- 들어오는 것만 시스템 오퍼레이션이다.
3. 시스템이 각 시스템 오퍼레이션에 대해서 어떻게 내부적으로 동작할 것인가도 고려해서 분석한다.
4. UML 2.0을 구성하는 중요한 다이어그램 중 하나이다.
```

### Operation Contract에 대한 다음의 설명 중 올바르지 않은 것은? 3번

```
1. Describe detailed changes to objects in a domain model, as the result of a system operation.
2. Postcondition은 도메인 모델을 기준으로 Objects 상태가 어떻게 변하는가를 기술한다.
3. 가능하면 모든 시스템 오퍼레이션에 대해서 오퍼레이션 컨트랙트를 만드는 것이 좋다.
4. Elaboration 단계 이후에는 크게 유용하지 않다.
- 자세하게 서술하지만 얼마나 유용한지 검증 X
```