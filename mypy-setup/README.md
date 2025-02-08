## mypy setup

- mypy only lints what you specify - so if you don't write types and whatnot, it's not going to lint those

## helpful docs

- mypy cli args: https://mypy.readthedocs.io/en/stable/command_line.html#the-mypy-command-line
- https://stackoverflow.com/questions/57785471/why-does-mypy-think-library-imports-are-missing
  - basically if you're using 3rd party libs and missing stubs - easiest thing to do is just ignore it
