n=next
def p(i):
    return ord(i)-(38+int(('`'<i<'{')*58))
s=0
f=open('input')
for l in f:
 l = l[:-1]
 m=len(l)//2
 s+=p((set(l[:m])&set(l[m:])).pop())
print(s)
s=0
f=open('input')
for g in zip(*([iter(f)]*3)):
    g=map(set,map(str.strip,g))
    s+=p((n(g)&n(g)&n(g)).pop())
print(s)
