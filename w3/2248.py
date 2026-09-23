n1, n2 = map(int, input().split())
ns1 = set(map(int, input().split()))
ns2 = set(map(int, input().split()))

com = ns1 & ns2
ncom = len(com)
print(ncom)
lcom = list(com)
lcom.sort()
if ncom == 0:
    pass
else:
    for i in lcom:
        print(i, end=" ")
