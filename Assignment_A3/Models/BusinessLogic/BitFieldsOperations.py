'''
	This library keeps the implementations of some of the binary oprations frequently performed on the bitfields

	************************************************************************************************************
	**** The main assumption for this library to work properly is that the bitfield lengths are already nibble
	**** size optimised. Some functions may work properly, but most may fail. So, make sure they are in the req-
	**** uired format
	************************************************************************************************************
'''


# as suggested by (@Murtaza Raja view --> https://github.com/murtraja) :)
def bitLenEqualize(num1, num2):
	'''
		method to equalize the number of bits in both numbers
			
		@params
		num1 = the bitfield for the restricted number 1
		num2 = the bitfield for the restricted number 2
	'''
	sign1 = num1[0]; sign2 = num2[0] # extract the sign bits of the two numbers
	
	# unset the two bits for both the numbers
	num1[0] = 0
	num2[0] = 0 
	
	# pad the number with lesser length to be equal to the onther one
	while(len(num1) != len(num2)):
		if(len(num1) < len(num2)):
			# add a nibble to the first number
			num1 = [0 for i in range(4)] + num1

		else: 
			# add a nibble to the second number
			num2 = [0 for i in range(4)] + num2

	# before returning the bitfields, retrun their origingal sign bits back to them
	num1[0] = sign1
	num2[0] = sign2

	return num1[:], num2[:]

def rsa(num, times):
	'''
		method to perform the arithmetic right shift on the binary number
			
		@params
		num = the bitfield for the restricted number
		times = number of times the shifting needs to be performed
	'''
	assert (times > 0), "you cannot shift a number -ve number of times"

	for i in range(times):	# perform the shift times number of times
		num.pop(len(num) - 1) # remove the last element of the bitfield
		num = [num[0]] + num
		
	return num[:]



def rsc(num, times):
	'''
		method to perform the circular right shift on the binary number
			
		@params
		num = the bitfield for the restricted number
		times = number of times the shifting needs to be performed

		@return
		a bitfield of the multiplication of the two numbers
	'''
	assert(times > 0), "you cannot shift a number -ve number of times"
	
	for i in range(times):
		bit = num.pop(len(num) - 1) # remove the last element of the bitfield
		num = [bit] + num
		
	return num[:]



def add(n1, n2):
	'''
		method to add the bitfields of two binary numbers
		*** Truncates the final carry by default ***			

		@params
		n1 = the bitfield for the restricted number1
		n2 = the bitfield for the restricted number2

		**** Implementation can be improved ****
	'''	

	# use the bitLenEqualize function to equalize the number of bits of the two numbers
	n1, n2 = bitLenEqualize(n1[:], n2[:]) 

	# carry on with the addition part
	bsum = [0 for i in range(len(n1))]; carry = 0		
			
	for i in reversed(range(len(n1))): # a complete hardwired implementation of binary addition
		if(n1[i] == 0 and n2[i] == 0): 
			if(carry == 0): 
				bsum[i] = 0	
			else: 
				bsum[i] = 1
				carry = 0

		elif(n1[i] == 0 and n2[i] == 1):
			if(carry == 0): 
				bsum[i] = 1	
			else: 
				bsum[i] = 0
		 				
		elif(n1[i] == 1 and n2[i] == 0): 
			if(carry == 0): 
				bsum[i] = 1	
			else: 
				bsum[i] = 0
		
		elif(n1[i] == 1 and n2[i] == 1): 
			if(carry == 0): 
				bsum[i] = 0
				carry = 1	
			else: 
				bsum[i] = 1
			
	return bsum[:]



def t2scomp(num): 
	'''
		method to calculate the 2's complement of the binary number
			
		@params
		num = the bitfield for the restricted number
	'''
	for i in range(len(num)): # flip every bit of the input number
		if(num[i] == 1):
			num[i] = 0
		else:
			num[i] = 1
				
	return add(num[:], ([0 for i in range(len(num) - 1)] + [1])[:]) # add 1 and return


