with open('abb.txt','r') as f1:
    s=[]
    for l in f1.read().split('\n'):
        s.append(l)
ans=[]
for l in s:
    if 'sin(x)/cos(x)' in l:
        k=l.replace('sin(x)/cos(x)','b')
        ans.append('b=cos(x)/sin(x)')
flag=0
for l in s:
    if 'while' in l:
        k=l.replace('100','50')
        ans.append(k)
    elif 'sin(x)/cos(x)' in l:
        k=l.replace('sin(x)/cos(x)','b')
        ans.append(k)
        flag=1
    elif flag==1 and '}' not in l:
        ans.append(l)
    elif '}' in l:
        ans.append(ans[2])
        ans.append(ans[3])
        ans.append('}')
        break

for i in ans:
    print(i)
