"""
def fun(lst):
    for i in lst:
        print(i)
        
fun([1,2])
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(5))