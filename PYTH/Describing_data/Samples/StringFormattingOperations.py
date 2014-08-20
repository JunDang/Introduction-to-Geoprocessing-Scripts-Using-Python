######################################################################
## StringFormattingOperations.py
## Author: Esri Instructor
## Date: <Date>
## Purpose:  Show examples using the str.format() method on a string
## to perform string formatting operations.
######################################################################

# Format strings using the str.format() method
print "{} eggs and {}".format("Green", "Ham")

print 'XCoord: {0}, YCoord: {1}'.format(-115.68, 34.36)

a, b, i = "Jane", "Mary", 6
print "{} will meet with {} at {} PM".format(a, b, i)

# Change the order of the string with index positions
print "{}, {}, {}".format("a", "b", "c")
print "{2}, {1}, {0}".format("a", "b", "c")
