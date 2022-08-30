## Dependency

- Models weakest possible relationships between classes
  - A class needs to know aobut another class to use objects of that class briefly.
  - Not used often in class diagram, but does in component diagram
  - 점선

## Association

- Models possible relationships betwen instances of classes
  - When objects of one class work with objects of another class for some prolonged amount of time.
  - Binary Association
    - Connects instances of two classes with one another
    - Navigability
        - An object knows its partner objects and can therefore access their visible attributes and operations
        - Indicated by open arrow head or cross
        - Undefined: Binary
  - n-ary Association
    - More than two partner objects are involved in the relationship.
      - No nvigation directions

### Ways to Show UML Attributes

- Attributes can be shown in three ways
  - Attribute text
    - visibility name: type multiplicity = default {property-string}
  - Association line
    - a navigability arrow
    - multiplicity
    - a role name
  - both together

### Attribute Text vs. Association Lines for Attributes

- Use the attribue text notation for data type objects, while the association line notation for others
  - Both are semantically equal.
  - But, showing an association line to another class box in the diagram gives visual emphasis.

### Association Class

- Association class
  - Assign attributes to the relationship between classes rather than to a class itself.
  - Treat an association itself as a class, and model it with attirbutes, operations, and other features.
    - Illustrated with a dashed line from the association to the association class.
    - Necessary when modeling n:m Associations

### Singleton Classes

- Singleton class has only one instance of the class.
  - "singleton" instance
  - In a UML diagram, it is marked a '1' in upper right corner of the name compartment
  - The Singleton design pattern
    - For monitoring

### Active class

- An active object runs and controls on its own **thread** of execution
  - The class of an active object is an active class
  - In the UML, it may be shown with double vertical lines on the left and right sides of the class box.
  - In Java, Runnable

### Interfaces
- The UML provides several ways to show interface implementation.
  - Formally called interface realization
  - 3 Notations:
    - Socket + lollipop notation
      - Usually used in Component Diagram
    - Dependency line notation
      - Usually used in Component Diagram
    - Interface implementation

## Aggregation

- Special forms of association
  - Used to express that a class is part of another class
- Properties of the aggregation association:
  - Transitive: if B is part of A and C is part ob B, C is also part of A
  - Asymmetric: it is not possible for A to be part of B and B to be part A simultaneously.

- Two types:
  - Shared aggregation
    - 다른 클래스에서 사용 중이라면 삭제 X
  - Composition
    - 사용하고 있는 클래스가 삭제될 경우 Composition 클래스도 삭제

### Shared Aggregation

- Expresses a weak belonging of the parts to a whole
  - Parts also exist independently of the whole.

- Multiplicity at the aggregating end may be > 1.
  - One element can be part of multiple other elements simultaneously.
  - Spans a directed acyclic graph.
  - Syntax: Hollow diamond at the aggregating end

- Example:
  - Student is part of Lab Class
  - Course is part of Study Program.

### Composition

- Existence dependency between the composite object and its parts
  - One part can be contained in at most one composite object at one specific point in time.
  - If the composite object is deleted, its parts are also deleted.
  - Multiplicity at the aggregating end is max: 1
    - The composite objects form a tree.
  - Syntax: Solid diamond at the aggregating end.
- Example:
  - Beamer is part of LectureHall which is part of Building.

## Generalization

- Everything of a general class are passed on to its subclasses.
  - Every instance of a subclass is simultaneously an indirect instance of the superclass.
  - Subclass inherits all characteristics(attributes and opertions), associations, and aggregations of the superclass except private ones.
  - Subclass may have futher characteristics, associations, and aggregations.
- Genralizations are transitive.

### Generalization - Abstact Class

- Used to highlight common characteristics of their subclasses.
- Used to ensure that there are no direct instances of the superclass
  - Only its non-abstract subclasses can be instantiated.
- Notation: keyword {abstract} or class name in italic font.

### Generalization - Multiple Inheritance
- UML allows multiple inheritance.
  - A class may have multiple superclasses.
  - Not allowed for JAVA programming language.

## Creating a Class Diagram

- Not possible to completely extract classes, attributes and associations from a natural language text automatically
- Guidelines
  - Nouns often indicates classes.
  - Adjectives indicates attribute values.
  - Verbs indicate opertations
- Example: "The library management system stores users with their unique ID, name and address as well as books with their title, author and ISBN number"
  - Usecase Diagram -> Class Diagram

## Quiz 

### Class에 대한 다음의 설명 중 올바르지 않은 것은? 4번

```
1. Attribute의 default visibility는 (-): Private 이다.
2. Operation의 default visibility는 (+): Public 이다.
3. 모든 Private Attribute에 대해서는 getter와 setter operations을 항상 만들어야 한다.
4. 모든 Attributes과 Operations은 Visibility(+/-)가 항상 표시되어야 한다.
```

### Generalization(Inheritance)에 대한 다음의 설명 중 올바르지 않은 것은? 1번

```
1. Everything of a general class are passed on to its subclasses.
2. Every instance of a subclasses is simultaneously an indirect instance of the superclass.
3. Subclass inherits all characteristics(attributes and operations), associations, and aggregations of the superclass except private ones.
4. Subclass may have futher characteristics, associations, and aggregations.
```

### 다음의 클래스 다이어그램의 정보를 가장 잘 해석한 것은? 1번

```
1. 모든 책은 그림과 챕터로 구성될 수 있다.
2. 대부분의 책은 그림으로 구성되어 있지만 일부는 챕터로 구성된다.
3. 대부분의 책은 챕터로 구성되어 있지만 일부는 그림으로 구성된다.
4. 모든 책은 그림과 챕터로 구성되어야 한다.
5. 책과 그림 챕터는 다 동등한 개념이다.
```
