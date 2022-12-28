""" Local Scope
Value can be accessed inside the function only """
"""
def fun():
    x=7;y=8;z=9
    print(x+y)
fun()
"""

""" Global Scope of a Variable , can be accessed by anyone """
# """ 
a=2
def bm():
    a=4
    b=3;c=5
    print(a)
    print(b)
print(a)
bm()
print(a)
# """