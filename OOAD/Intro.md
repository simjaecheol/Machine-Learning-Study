# Object Oriented Analysis and Design Introduction

## Chapter 1. Object-Oriented Anaysis and Design

- Object-Oriented Analysis (OOA)
  - Discover the domain concepts/objects (the objects of the problem domain)
    - Use Case Diagram
    - Domain Diagram

- Object-Oriented Design (OOD)
  - Define software objects(static)
    - Class Diagram
  - Define how they collbaborate to fulfill the requirements(dynamics)
    - Sequence Diagram
- Use Case Diagram -> Domain Model -> Sequence Diagram -> Class Diagram

### UML

- "The Unified Modeling Lauguage(UML) is a visual language for specifying, constructing, and documenting the artifacts of systems."
- 3 ways(Levels) to apply use UML
  - Sketch
    - Conceptual perspective
    - Informal and incomplete diagrams are created to explore difficult parts of the problem or solution space
      - Intercommunication medium
      - Inception
      - 정확하지 않음 - OOA(Use Case / Domain Model)
  - Blueprint
    - Specification perspective
    - Relatively detailed design diagrams are used for code generation.
      - 정확해야함
      - OOD (Statechart Model)
  - Programming language
    - 요즘은 잘 안씀
    - Implementation perspective
    - Complete executable specification of a software system in UML
      - Executable code will be automatically generated.
      - Still under development in terms of theory, tool robustness and usability.

### What the UML is Not?

- UML is not an Object-Oriented analysis and design developing process.
  - 단순 모델링 Language이다.
  - UML is not a systematic way to develop software systems.

- UML will not teach you an Object-Oriented way of thinking.
  - OOAD-Thanking: 시스템을 구성하는 오브젝트들끼리 콜라보레이션, 커뮤니케이션을 통해서 시스템의 오퍼레이션을 realization하게 하는 Thinking
  - It will not tell you how to design object structures or behaviors.
  - It will not tell you whether your design is good or bad.

## Chapter 2. Iterative, Evolutionary, and Agile - UP(Unified Process)

### Software Development Process and the UP

- **Software development process**
  - A systematic apporach to building, deploying and possibly maintaining software

- **Unified Process(UP)**: a popular iterative software development process for building object-oriented systems
  - Iterative with fixed-length iterations(mini waterfalls of about 3 weeks)
  - Inspired from Agile(i.e. opposite from waterfall)
  - Flexible(can be combined with practices from other OO processes)
    - Unified: 기존의 모든 프로세스들을 Unified함
  - <u>A de-facto industry standard</u> for developing OO software

### Risk-Driven and Client-Driven Iterative Planning

- The UP encourages a combination of risk-driven and client-driven iterative planning.
  - To identify and drive down the high risks and
  - To build visible features that clients care most about.

- <u>Risk-driven iterative development</u> includes more specifically the practice of <u>architecture-centric iterative development</u>.
  - Early iterations focus on building, testing, and stabilizing the core architecture.

### The UP Phases

- A UP project organizes the work and iterations across 4 major phases.
  - Inception
    - approximate vision, business case, scope, vague cost estimates
  - Elaboration
    - refined version, iterative implemetation of the core architecture, resolution of high risks, identification of most requirements and scope, more realistic estimates.
    - 얇고 넓게 리스크 분석
    - 아키텍쳐, 클라이언트, UI/UI - prototype(5 ~ 10%)
    - Usecase가 바뀌는 건 Elaboration Stage에서만 가능
  - Construction
    - iterative implementation of the remaining lower risk and easier elements, and preparation for development.
  - Transition
    - beta tests, deployment.

### The UP 9 Disciplines

- Business Modeling
- Requirements
- Design
- Implementation
- Test
- Deployment
- Configuration & Change Management
- Project Management
- Environment

### The UP Development Case

- Development Case:
  - An artifact(output) in the Environment discipline
  - Documenting the choice of practices and UP artifacts for a project
  - Inception 1 / Elaboration 1 ~ 7 / Construction / Transition 
  - r: 수정 가능
  - Architecture Design: Elaboration Phases
  - Construction에서는 수정 불가능

### The Relationship of UP Artifacts in One iteration

- Domain Model
- Use-Case Model
  - Use-Case Diagram
  - Use-Case Text
  - System Sequence Diagram
- Design Model
  - Sequence Diagram
  - Class Diagram

- 이를 잘 만들려면 Object Oriented Analysis & Design Thinking이 필요!


### The UP Practices
- The central idea to UP practices:
  - A short timeboxed iterative, evolutionary and adaptive development
- Additional best practices and key concepts
  - Tackle high-risk and high-value issues in early iterations
    - Risk driven, Client driven
  - Continuously engage users for evaluation and feedback
    - Client driven
  - Build a cohesive core architecture in early iterations
    - Architecture centric
  - Continuously verify quality; test early, often and realistically
  - Apply use cases where appropriate
    - 각 단계를 시작하기 전에 필요로 한 use-case를 구현
  - Do some visual modeling(with the UML)
  - Carefully manage requirements(configuration manangement)


## Chapter 3. Case Studies

### What is Covered in the Case Studies?

- Genarally, applications include
  - UI elements
  - Core application logic
  - OS, database access and collaboration with external SW/HW components

## Quiz

### 다음 중 UP에서 중요하게 생각하는 Best Practice나 Key Concepts이 아닌 것은 무엇인가요? 2번

```
1. Tackle high-risk and high-value issues in early iterations
2. Make a project plan in detail from start to finish
3. Continuously engage users for evaluation and feedback
4. Build a cohesive, core architecture in early iterations
```

### 다음 UP에 대한 설명 중 올바른 것은? 4번

```
1. We must define most of the requirements before starting design or implementation
2. Inception = requirements, elaboration = design, and construction = implementation
3. The purpose of elaboration is to fully and carefully define models, which are translated into code during construction
4. Inception does not require much UML diagramming.
```

### UP Environment Discipline에서 작성되는 Artifact로서, 진행할 프로젝트에서 생성할 UP Artifacts와 사용할 Practices의 선택 결과를 정리한 Artifact는 무엇인가요? Development Case