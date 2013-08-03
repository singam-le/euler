from array import array
def multDigits(n):
    l = []
    while (n):
        l.append(n%10)
        n=n/10
    return reduce (lambda x,y: (x)+(y*y), l,0)

start=99999
alloc = 81*16*8
print alloc
ar = array('i', [0]*alloc)
k=1

def getItem(val):
    q,m = divmod(val,16)
    #print "in", q, val, alloc
    if q >= alloc: print "bigger", q, alloc,val
    return ar[q] & k<<m

def setItem(val):
    q,m = divmod(val,16)
    ar[q] = ar[q] | k<<m

for i in xrange(99,start,1):
    start = i
    while(start):
        #print start
        if not getItem(start):
            setItem(start)
            start=multDigits(start)
        else:
            if start==89: print i
            break





