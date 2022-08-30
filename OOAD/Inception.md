# Inception

- 길어야 1주

## Chapter 4. Inception is Not the Requirements Phase

- Most projects require a short initial step to question about:
  - What is the vision and business case for this project
  - Feasible?
  - Buy and/or build
  - Rough unreliable range of cost is it $10-100K or in the millions?
  - Should we proceed or stop?
- Inception should be short.
  - One week for most projects
  - Most requirements analysis occurs during the elaboration phase, not inception.
- Brief
  - 얇고 넓게
  - Not Casual

### Artifacts Start in Inception

- Vision and Business Model
- Use-Case Model
  - Describe the functional requirements
  - 10% of the use cases
- Supplementary Specification
  - Describe other requirements, mostly non-functional
- Glossary
- Risk List & Risk Management Plan
- Prototypes and proof of concepts
- Phase Plan & Software Development Plan
- Development Case

### How Much UML During Inception?

- Much UML diagramming is not required.
  - Inception has more focus on understanding the basic scope and 10% of the requirements, expressed mostly in text forms

## Chapter 5. Evolutionary Requirements

### Requirements

- Capabilities and conditions to which the system must conform
- Requirement analysis is
  - to find, communicate and organize what is really needed, in a form that is clear both to clients and team memebers.
- In the UP, requirements are analyzed iteratively and skillfully
- The UP encourages skillful elicitation(finding) via techniques such as
  - skillful 하다는 것은 아래의 요구 사항을 만족
    - writing use cases with customers.
    - requirements workshops that include both developers and customers.
    - a demo of the results of each iteration to the customers, to feadback

### Types and Categories of Requirements

- In the UP, requirements are categorized according to the FURPS+ model

  - Functional: features, capabilities, security
    - Use Case Diagram
  - Usability: human factors, help, documentation
  - Reliability: frequency of failure, recoverability, predictability
  - Performance: response times, throughput, accuracy, availability, resoure usage
  - Supportability: adaptability, maintainability, internationalization, configurability

    - Non-Functional: Usability, Reliability, Performance, Supportability
      - Supplementary Specification

  - The "+" in FURPS+ indicates ancillary and sub-factors such as:
    - Implementation: resource limitations, languages and tools, hardware, ...
    - Interface: constraints imposed by interfacing with external systems
    - Operations: for example a physical box
    - Legal: Licensing and so forth

- It is helpful to use FURPS+ categories as a checklist for requirements coverage

### Quality Attributes/Requirements

- Quality attributes/requirements

  - Usability + Reliability + Performance + Supportability
    - 이외에 30 ~ 40가지 Quality factors 존재
  - Also called "Non-functional requirements"

- The quality attributes often have a strong influence on the architecture of a system.

### How Requirements are Organized

- The UP offers several requirements artifacts. (But, they are all optional)

  - User-Case Model
    - A set of typical scenarios of using a system
    - These are primarily for functional(behavioral) requirements.
  - Supplementary Specification

    - Basically, everything is not in the use cases.
    - This artifact is primarily for all non-functional requirements. such as performance or licensing.
    - It is also the place to record functional features not expressed(or expressible) as use cases
      - for examples: a report generation.

  - Glossary
    - It defines noteworthy terms
  - Vision
    - A short executive overview document for quickly learning the project's big ideas.
  - Business Rules
    - It typically describe requirements or policies that transcend one software project.

- Inception
- Requirements Analysis
  - 산출물: SRS
- Design
  - 산출물: SDS
- Coding

## Chapter 6. Use Cases

- Process: Evolutionary Requirements in Iterative Methods
  - Inception과 Elaboration 단계에서 Use-Case Model 정립이 끝남
  - 이후에는 Brief(requirements) 변경 X

### Case Study: Use Cases in the NextGen POS

- Use Cases are developed and refined iteratively
- Use Cases of the NextGen POS at the inception phase

| Brief                                                                                             | Casual                                                                | Fully Dressed                        |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------ |
| Cash In</br>Cash Out</br>Manage Users</br>Start Up</br>Shut Down</br>Manage System Tables</br>... | Process Rental</br>Analyze Sales Activity</br>Manage Security</br>... | Process Sale</br>Handle Returns</br> |

## Chapter 7. Other Requirements

### Other Requirements Artifacts

- Supplementary Specification

  - Captures and identifies other kinds of requirements, such as
    - reports, documentation, packaging, supportability, licensing and so forth
  - 정해진 포맷이 없음

- Glossary

  - Captures terms and definitions; a data dictionary

- Vision

  - Summarizes the "vision" of the project; an executive summary

- Business Rules
  - Capture long-living and spanning rules or policies(such as tax laws), that trnascend one particular application

### Supplementary Specification

- Other requirements, information and constraints not easily captured in the use cases or Glossary, including system-wide "URPS+" quality attributes.

- Elements of the Supplementary Specification include:
  - FRUPS+ requirements
    - functionality
    - usability
    - reliability
    - performance
    - supportability
    - Quality와 관련
  - report
  - hardware and software constraints
    - (operating and networking systems, ...)
  - development constraints
    - process or development tools
  - other design and implementation constraints
  - internationalization concerns(units, languages)
  - documentation(user, installation, administartion) and help
  - licensing and other legal concerns
  - packaging
  - standards
    - technical
    - safety
    - quality
  - operational concerns
    - how do erros get handled
    - how often should backups be done?
  - application specific domain rules
  - information in domain of interest
    - what is the entire cycle of credit payment handling

### Process: Evolutionary Requirements in Iterative Methods

- In Inception
  - Use Case Model
  - Vision
  - Supplementary Specification
  - Glossary
  - Business Rules

## Quiz

### 다음 중 Inception 단계에서 수행되는 활동 또는 결과물이 아닌 것은? 3번

```
1. Client, Architect 등 모든 과제 관련자들이 참가하는 Requirements Workshop을 개최한다.
2. 대부분의 Use-Cases가 Brief 포맷으로 작성된다.
3. 대부분의 Architecturally Risky Requirements가 찾아진다.
4. 필요한 경우 Technical proof-of-concept을 위한 Prototype을 만든다.
```

### 다음의 요구사항에 대한 설명 중 올바르지 않은 것은 무엇인가? 3번

```
1. 요구사항은 일반적으로 크게 기능 요구사항과 비기능 요구사항으로 구분할 수 있다.
2. 비기능 요구사항은 시스템의 품질(Quality)에 큰 영향을 미치므로 Quality Attributes/Requirements라고도 한다.
3. 시스템의 SW Architecture에 영향을 크게 미치는 요구사항은 기능 요구사항이다.
4. UP에서 일반적으로 기능 요구사항은 Use-Cases Model로, 비기능 요구사항은 Supplementary Specification으로 작성된다.
```

### Use-Case에 대한 다음의 설명 중 올바르지 않은 것은? 2번

```
1. Use-Case는 요구사항을 체계적으로 분석하는 방법이다.
2. Use-Case는 비 OOAD 개발시에 사용하면 효과가 상당히 반감된다.
3. Use-Case는 모든 OOAD 개발방법론에서 사용되는 중요한 시작점 중의 하나이다.
4. Use-Case를 이용한 다양한 요구공학(Requirements Engineering) 방법론이 있으나, UP에서는 가장 간단한 수준으로만 Use-Case를 활용한다.
```
