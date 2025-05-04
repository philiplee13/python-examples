## Exceptions and error handling

https://realpython.com/python-raise-exception/#raising-exceptions-and-the-assert-statement

- within try catch methods - if you're raising exceptions, don't overwrite the exception
- raise to halt program execution
- be mindful of when you use try-catch and think of when you want the program to halt + give feedback
- if you have multiple exceptions - starting from 3.11 use `ExceptionGroups`
