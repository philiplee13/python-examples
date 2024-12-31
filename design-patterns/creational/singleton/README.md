## Singleton

### Use Cases

- This is often used to solve one of two problems
  - ensuring that a class only has one instance
    - We would want to ensure that a class has a single instance is to control access to a shared resource (files, db, etc)
  - providing a global access point to that instance
    - allows access to the object from anywhere in the program
  - Singleton is usually implemented have 2 steps in common
    - Making the default constructor private - preventing objects being created using `New`
    - Creating a static method that acts as the constructor -> this basically calls the private constructor and saves the object in a static field, all following calls returns the cached object

### Helpful info

- in specific to python [dunder methods](https://realpython.com/python-magic-methods/#creating-objects-with-__new__)
