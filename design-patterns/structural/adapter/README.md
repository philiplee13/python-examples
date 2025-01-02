## Use Cases

- Allows objects with incompatiable interfaces to collaborate
- Let's say that we're getting data from a given source in `XML` and we need to display it using a library that accepts `JSON`

  - we can't just directly transfer the data from the source to the destination, there needs to be some sort of manipulation in the middle

- The adapter gets an interface, compatiable with one of the existing objects
- Then using this interface -> the existing object can safely use the adapters methods
- When using the methods -> the adapter passes the request to the second object, but in a format that it understands

## When to use

- When we want to use an existing class - but it's interface isn't compatiable with the rest of your code
  - Serves as a middle layer (like a translator)
- When we want to reuse existing subclasses that all lack some sort of common functionality that can't be added to the parent class
  - Put the missing functionality into an adapter -> then wrap the subclasses with the adapter
  - However - for this to work -> the target classes all need a common interface and the adapter fields should follow that interface
  - Looks similar to the `Decorator` pattern
