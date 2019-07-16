c = dict()
a =['a','b','c']
for name in a:
    if name == 'b':
	    x = 5
    elif name == 'c':
        x = 10
    else:
	    x  =1
    c[name] = c.get(name,x)
	
tmp =list()
for k,v in c.items():
    tmp.append((v,k))
	
print(tmp)
tmp = sorted(tmp,reverse = False)
print(tmp)
tmp = sorted(tmp, reverse =True)
print(tmp)
tmp.sort()
print(tmp)
print(c)
c  = sorted(c.items())
print(c)