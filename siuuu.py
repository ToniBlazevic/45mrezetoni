
#1#
"""
a=int(input("Unesi broj:"))
while a>0:
    if a%2==0:
        print(a)
    a=a-1
"""
#2#
"""
a=int(input("Unesi broj:"))
while a>0:
    if a%2==1:
        print(a)
    a=a-1
"""
#3#
"""
a=int(input("Unesi broj:"))
for i in range(0,a,2):
    if i%2==0:
        print(i)
"""
#30#
"""
a=int(input("Unesi broj:"))
parni=0
neparni=0
while a>0:
    n=int(input("Unesi broj:"))
    if n%2==0:
        parni+=n
    else:
        neparni+=n
    a=a-1
print("Zbroj parnih:",parni)
print("Zbroj neparnih:",neparni)
    
"""
#35#
a=int(input("Unesi broj:"))
n=int(input("Unesi broj:"))
mini=big=n
for i in range(a-1):
    n=int(input("Unesi broj:"))
    if n<mini:
        mini=n
    if n>big:
        big=n
print("Največi je",big)
print("Najmanji je",mini)
        

    
    
















    
