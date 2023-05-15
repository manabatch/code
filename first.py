from collections import defaultdict
d = defaultdict(list)
f = defaultdict(list)
fo = defaultdict(list)
p = defaultdict(dict)
d = {'E':['TG'],'G':['+TG','e'],'T':['FW'],'W':['*FW','e'],'F':['(E)','c']}
# First Functions
for i,j in d.items():
    z = i
    k = 0
    while k<len(d[z]):
        if 'a'<=d[z][k][0]<='z' or d[z][k][0] in '(+)*' or d[z][k][0]=='e':
            f[i].append(d[z][k][0])
            k+=1
        else:
          
            z=d[z][k][0]
            k = 0
print("First Functions of all Non-Terminals")
for i,j in f.items():
    print(i,'==>',set(j))