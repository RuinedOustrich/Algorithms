import random

def primal():
    n = int(input())
    a = 5
    if a ** (n-1) == 1 % n:
        print("yes")
    else:
        print("no")

primal()
