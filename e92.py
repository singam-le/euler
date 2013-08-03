from array import array
def multDigits(n):
    l = []
    while (n):
        l.append(n%10)
        n=n/10
    return reduce (lambda x,y: (x)+(y*y), l,0)


num = set()
start = 85
alloc = start * 10
ar = array('B', 'a'*alloc)
for i in xrange(0, alloc):
    ar[i] &= 0
k=1
def getIndex(val):
    q,m = divmod(val,8)
    print q, m
    ar[q] = ar[q] | k<<m

while(start):
    print start
    if not ar[start]:
        getIndex(start)
        ar[start] = start
        start=multDigits(start)
    else:
        print "shanx .. done", start
        start = 0





