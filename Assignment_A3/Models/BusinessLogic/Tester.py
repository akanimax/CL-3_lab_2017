from BoothMultiplier import *

# A Naive test suite for this package.


# test the BitNibbles class
print BitNibbles(3).getBits() # should return [0, 0, 1, 1]
print BitNibbles(-7).getBits() # should return [1, 1, 1, 1]
print BitNibbles(-32).getBits() # should return [1, 0, 1, 0, 0, 0, 0, 0]

''' Feel free to add more test cases here 
	...
	...
'''



# test the BoothMultiplier class
BoothMultiplier.multiply(BitNibbles(-3), BitNibbles(-5)) # works correct
BoothMultiplier.multiply(BitNibbles(5), BitNibbles(5)) # works correct
BoothMultiplier.multiply(BitNibbles(-5), BitNibbles(6)) # works as expected
BoothMultiplier.multiply(BitNibbles(-3), BitNibbles(2)) # works as expected 

''' Feel free to add more test cases here 
	...
	...
'''


''' I feel extremely happy to announce that the test cases, I have laid out, pass successfully '''
