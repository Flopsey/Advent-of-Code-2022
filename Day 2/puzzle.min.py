s=t=0
a,p=ord,print
f=open('input')
for l in f:
  o,c=l[::2]
  o,c=a(o)-65,a(c)-88
  r=(o+c-1)%3
  s+=c+1+((c-o+1)%3)*3
  t+=r+1+((r-o+1)%3)*3
p(s)
p(t)
