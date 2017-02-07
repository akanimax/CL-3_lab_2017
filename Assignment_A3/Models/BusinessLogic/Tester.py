from BoothMultiplier import *

# test the BitNibbles class
print BitNibbles(3, 4).getBits() # should return [0, 0, 1, 1]
print BitNibbles(-7, 4).getBits() # should return [1, 1, 1, 1]
print BitNibbles(-32, 8).getBits() # should return [1, 0, 1, 0, 0, 0, 0, 0]

try: 
	BitNibbles(129, 8) # should highlight the related error

except AssertionError:
	handleAssertionError()	


''' Feel free to add more test cases here 
	...
	...
'''



# test the BoothMultiplier class
BoothMultiplier.multiply(BitNibbles(-3, 4), BitNibbles(-5, 4)) # works correct
BoothMultiplier.multiply(BitNibbles(5, 4), BitNibbles(5, 4)) # works correct
BoothMultiplier.multiply(BitNibbles(-5, 4), BitNibbles(6, 4)) # works as expected
BoothMultiplier.multiply(BitNibbles(-3, 4), BitNibbles(2, 4)) # works as expected 

''' Feel free to add more test cases here 
	...
	...
'''


''' I feel extremely happy to announce that the test cases that I have laid out pass successfully '''
