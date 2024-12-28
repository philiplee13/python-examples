## Builder Pattern

### Use Cases

- A creational design pattern that lets us construct complex objects "step by step"
- Imagine that we have a `Meal`
  - that meal can have multiple aspects to it
    - drink
    - entree
    - side
    - dessert
  - we can try to solve this by having multiple constructors in the `Meal`
    - but that will lead to some pretty ugly constructors (where not all parameters are being used)
  - we can instead break out the parts that we need into individual items, and "build"
