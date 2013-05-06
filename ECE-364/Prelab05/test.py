import sys, os

for line in sys.stdin:
    line=line.strip()
    Data=line.split()

    B=[]
    for item in range(1,len(Data)-1):
        A=()
        A=[(Data[item],Data[item+1])]
        B+=A
    print B
