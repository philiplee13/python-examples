## Concurrency

- Concurrency is helpful when programs are running into I/O bound problems or CPU bound problems
- I/O bound problems are like
  - talking to external resources, slow networks, etc
- CPU bound problems are like

  - multiple computations or CPU intensive problems

- It's important to think about what the bottle neck of a given program is -> using asyncio for CPU bound processes may actually slow it down
- In general -> for IO problems using asyncio / threading, for CPU intensive use multiprocessing
  - use asyncio first if you can, threading if you must
