def double1(x):
    return 2 * x

def double2(x):
    print 2 * x

def double3(x):
    return 2 * x
    print 2 * x

def double4(x):
    print 2 * x
    return 2 * x

print "Now let us see what actually prints"
print "double1", double1(2)
print "double2", double2(2)
print "double3", double3(2)
print "double4", double4(2)
