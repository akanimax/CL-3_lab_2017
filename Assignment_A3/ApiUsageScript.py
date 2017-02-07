from Models.BusinessLogic.BoothMultiplier import * # import the elements of the api

try: 

	# no need to print the result, as the function already logs some statements to the console
	# also returns the bitfield of the multiplication of the mentioned two numbers
	BoothMultiplier.multiply( # the method multiply of BoothMultiplier class requires two bitNibbles
		BitNibbles(5, 4), # a nibble of size 4 bits with value 5 
		BitNibbles(3, 4)  # a nibble of size 4 bits with value 3
	) 

except AssertionError:
	handleAssertionError() # method in the api for handling the errors



# output of the above code is as follows:
'''
The multiplication is to be carried out between: 
No. 1:  [0, 1, 0, 1]
No. 2:  [0, 0, 1, 1]
Current Step:  1
[1, 1, 1, 0, 1, 0, 0, 0] 

Current Step:  2
[0, 0, 0, 0, 1, 1, 0, 0] 

Current Step:  3
[1, 1, 1, 0, 1, 1, 1, 0] 

Current Step:  4
[0, 0, 0, 0, 1, 1, 1, 1] 

Answer of Multiplication:  [0, 0, 0, 0, 1, 1, 1, 1]

'''
