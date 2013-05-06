#!/usr/bin/env python2.6

import bitWorker

# Test displayBinary
print "-- displayBinary"
bitWorker.displayBinary(22)
print "(0 to 10):"
for a in range(0,10):
    bitWorker.displayBinary(a)

print "-- getBit"
# Test getBit
bitWorker.getBit(0, 99)
bitWorker.getBit(3, 17)
print "(0 to 4):"
for i in range(0,4):
    bitWorker.getBit(i, 10)

print "-- getPartialValue"
# Teest getPartialValue
bitWorker.getPartialValue(1, 0, 11)
bitWorker.getPartialValue(1, 4, 67)
bitWorker.getPartialValue(3, 6, 117)
bitWorker.getPartialValue(1, 3, 22)
print "(0 to 4):"
for i in range(0,4):
    bitWorker.getPartialValue(0, i, 11)
