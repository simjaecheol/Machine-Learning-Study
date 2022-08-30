# Component Diagram

## UML components
- UML components organize a system into manageable, reusable, and swappable pieces of software.
- Development view in Kruchten's 4+1 view model
  - Describes how your system's parts are organized into modules and components.
  - Help you manage layers within your system's architecture
    - Logical view
    - Process view
    - Physical view
    - Development view
    - Use case view

- The UML component can do:
  - The same things a class can do
  - Components can have ports and show internal structure
  - Components are accessed through interfaces

- The UML Notation for Components
  - A component is drawn as a rectangle with the << component >> stereotype.
  - An optional tabbed rectangle icon in the upper righthand corner

- Components interact with each other through interfaces.
  - Provided interface: Interface that the component realizes(provided services)
    - Output: lollipop
  - Required interface: Interface that the component needs to function(expected services)
    - Input: fork

### UML Notations for Interfaces

- 3 standard ways to show provided and required interfaces in UML
  - Ball and socket symbols
  - Stereotype notation
  - Text listing

### Showing Components Working Together

- If a component has a required interface, then it needs another class or component in the system that provides it.
- At a higher-level view, this is a dependency relation between the component.

### Classes to Realize a Component

- Component realization
  - A component often contains and uses other classes to implement its functionality.
- 3 ways to show component realization:

### Parts of a Class

- When showing the internal structure of a class, you draw its parts or items contained by component, inside the containing class.
  - Parts are specified by the role they play in the containing class.
- A part is a set of instances that may exist in an instance of the containing class at runtime.

### Delegation and Assembly Connectors
- 컴포넌트 내부에서 연결되는 종류에 따라 분류
- Delegation connectors show how interfaces correspond to internal parts.
  - 외부에 보여지는 인터페이스
- Assembly connectors show that a component requires an interface that another component provides.
  - 내부 컴포넌트 끼리

## Quiz

### Component Diagram의 Components와 Deployment Diagram의 Compoents의 차이점은 무엇인가요?

```
Component Diagram의 Components는 일반적으로 source file이나 개발 중인 elements이다. 하지만 Deployment Diagram의 Components는 Processor 위에서 동작하는 runtime components로서, Components Diagram에 있는 Components의 instance이다.
```
