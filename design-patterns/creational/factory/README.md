## Factory Pattern

### Use cases

- So given a common interface, you use a factory to actually create the concrete implementations
  - So one possible example of this would be a `BankAccount` interface
    - followed by concrete implementations of the following
      - `Personal`
      - `Business`
      - `Investment`
  - Each of these `BankAccount` will share common properties and common methods
    - We can then extend each of these accounts if we need to

### When to use factory

- If we ever have complex if/else/elif conditions to determine which object to create, that may be an indicator to refactor
- If we have multiple implementations for the same feature, or have similar features under a common interface
