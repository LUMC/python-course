# Exceptions

Read two numbers (`a` and `b`) from the command line (`input()`) and
compute `a/b`.

- Check what happens when `b` is `0`.
- Try to catch the exception raised when `b` is `0` and prompt the user with a
  corresponding message.





try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("Can't divide by zero")
