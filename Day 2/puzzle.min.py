a,b=ord,lambda c,d:d+1+(d-a(c))%3*3
print(*map(sum,zip(*((b(c,a(d)-88),b(c,(2+a(c)+a(d))%3))for c,d in map(str.split,open('input'))))),sep="\n")
