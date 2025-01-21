__author__ = 'Chris'



s1 = "abcdefg"
s2 = s1
s2 += "h"
print s1[2:5]
print s1[-3:]

L1 = list ("abc")
L1.append (["d"])
print L1

x=8
y = -1
if x > 5:
    print "a"
elif y < 0:
    print "b"
else:
    print "c"

def set_n (x):
    n=x

n = "first"
set_n ("second")
print n