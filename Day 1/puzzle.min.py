p=print
def t(i):
 s=0
 for l in i:
  l=l[:-1]
  if l == "":
   yield s
   s = 0
  else:
   s += int(l)
f=open('input')
s=sorted([*(t(f))])
p(s[-1])
p(sum(s[-3:]))
