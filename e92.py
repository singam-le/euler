from array import array
# return sq. of all digits in num (n)
def multDigits(n):
    l = []
    while (n):
        l.append(n%10)
        n=n/10
    return reduce (lambda x,y: (x)+(y*y), l,0)

# return 1 of index location if already occupied
# location of bit array
def getItem(val):
    q,m = divmod(val,16)
    return ar[q] & 1<<m

# set the index of the location in the bit array 1
def setItem(val):
    q,m = divmod(val,16)
    ar[q] = ar[q] | 1<<m

def e92Calc():
    start=999999
    print alloc

    for i in xrange(85,start+1,1):
        start = multDigits(i)
        # initialize the bit array
        ar = array('i', [0]*alloc)
        while(start):
            if not getItem(start):
                setItem(start)
                start=multDigits(start)
            else:
                if start==89: 
                    print i
                break    

# here the 81 is sq. of max digit i.e 9
# 6 is no. of digits in num
# 16 is the size of int in array. to convert to bit array
alloc = 81*6/16 + 1
ar = array('i', [0]*alloc)
if __name__ == '__main__':
    e92Calc()


