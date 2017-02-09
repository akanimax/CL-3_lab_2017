from Models.BusinessLogic.BoothMultiplier import * # import the elements of the api


''' old ApiUsage '''
#try: 

#	# no need to print the result, as the function already logs some statements to the console
#	# also returns the bitfield of the multiplication of the mentioned two numbers
#	BoothMultiplier.multiply( # the method multiply of BoothMultiplier class requires two bitNibbles
#		BitNibbles(5, 4), # a nibble of size 4 bits with value 5 
#		BitNibbles(3, 4)  # a nibble of size 4 bits with value 3
#	)
#
#except AssertionError:
#	handleAssertionError() # method in the api for handling the errors


''' 
	Updated ApiUsage 
	
	You can easily observe the improvements in the ease of use of the Api now
'''




# case 1: 
BoothMultiplier.multiply(BitNibbles(3), BitNibbles(5)) # as easy as this now
# output of the above code is as follows:
'''
The multiplication is to be carried out between: 
No. 1:  [0, 0, 1, 1]
No. 2:  [0, 1, 0, 1]
Current Step:  1
[1, 1, 0, 1, 1, 0, 0, 0] 

Current Step:  2
[1, 1, 1, 0, 1, 1, 0, 0] 

Current Step:  3
[0, 0, 0, 1, 1, 1, 1, 0] 

Current Step:  4
[0, 0, 0, 0, 1, 1, 1, 1] 

Answer of Multiplication:  [0, 0, 0, 0, 1, 1, 1, 1]

''' 
# 3 x 5 = 15 i.e. [0, 0, 0, 0, 1, 1, 1, 1]




# Now, no more need to take care about the sizes of the two numbers. Any two numbers can be multiplied
BoothMultiplier.multiply(BitNibbles(128), BitNibbles(2))
# output of the above code is as follows: 
'''
The multiplication is to be carried out between: 
No. 1:  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
No. 2:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
Current Step:  1
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  2
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  3
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  4
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  5
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  6
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  7
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  8
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  9
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  11
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  12
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] 

Answer of Multiplication:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

'''
# 128 x 2 = 256 i.e. [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]




# A special mention for this case here: 
# if one number is -ve and other is +ve, the answer is +ve
BoothMultiplier.multiply(BitNibbles(-17), BitNibbles(2))
# output of the above code is as follows:
'''
The multiplication is to be carried out between: 
No. 1:  [1, 1, 1, 0, 1, 1, 1, 1]
No. 2:  [0, 0, 0, 0, 0, 0, 1, 0]
Current Step:  1
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  2
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0] 

Current Step:  3
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0] 

Current Step:  4
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] 

Current Step:  5
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0] 

Current Step:  6
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0] 

Current Step:  7
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0] 

Current Step:  8
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0] 

Answer of Multiplication:  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]

'''
# here, -17 x 2 = -34. Now, in our system, -34 is represented as the 2's complement of +34.
# the answer given by the system is: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
# its 2's complement is: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
# this is exactly equal to: 34. So, the original answer indeed represents -34.
