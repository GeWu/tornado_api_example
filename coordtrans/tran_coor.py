import os

d = "11632088,4006698%11632060,4006692"
output = os.popen('./a.out gcj02ll bd09ll %s' % d)
print output.read()
