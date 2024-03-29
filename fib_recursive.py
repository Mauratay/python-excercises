def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# 1. A function can call other functions or even itself. When a function calls itself, this situation is known as recursion, and the function which calls itself and contains a specified termination condition (i.e., the base case - a condition which doesn't tell the function to make any further calls to that function) is called a recursive function.

# 2. You can use recursive functions in Python to write clean, elegant code, and divide it into smaller, organized chunks. On the other hand, you need to be very careful as it might be easy to make a mistake and create a function which never terminates. You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.
