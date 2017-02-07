import sys
import traceback


# error handler function for AssertionError types of errors
def handleAssertionError(): 
	_, _, tb = sys.exc_info()
	tb_info = traceback.extract_tb(tb)
	filename, line, func, text = tb_info[-1]
	error = text.split(",")[-1]

	print "An error occured: " + error



class BitNibbles: 
	'''
		The class that converts a number into binary and stores the bits in its object
	'''
	
	def __convert_to_binary(self, number):
		'''
			Private helper method to convert the given integer into list of bits
		'''

		bits = [int(digit) for digit in bin(abs(number))[2:]] # get the list of bits
		
		# pad zeros in the front if required
		while(len(bits) != self.__size ):
			bits = [0] + bits # 

		if(number < 0): # if the number is negative, set the sign bit 		
			bits[0] = 1	
		
		return bits


	def __init__(self, integer, limit=8): # default size of limit is 8 bits
		'''
			Default constructor of the class.
			
			@params			
			integer = the number that needs to be converted to bits
			limit  	= size of the binary number in bits. by default it is 8 bits i.e. 2 nibbles 
		'''

		# private data attributes
		self.__size = limit
		self.__bits = [] # initialize the bits array (List) to empty
		
		# make sure that the limit is a multiple of 4 for booth's multiplication algorithm to work
		assert (limit % 4 == 0), "Nibble has to be of a size that is a multiple of 4"

		# make sure that the integer is within limit:
		assert (abs(integer) < pow(2, limit) // 2), "Integer is not within the provided limit"

		# if both the assertions pass, proceed with object creation and assign the bits
		self.__bits = self.__convert_to_binary(integer)


	def getBits(self):
		'''
			getter method to acquire the converted bits.
		'''

		return self.__bits[:] # to return the value and not the reference to the list

	def getSize(self):
		'''
			getter method to acquire the set size of the number.
		'''

		return self.__size # to return the value and not the reference to the list


class BoothMultiplier:
	'''
		Algorithm class to encapsulate the booth's algorithm multiplier
	'''	

	@staticmethod
	def multiply(num1, num2):
		''' 
			Multiply two numbers using the Booth's binary multiplication algorithm

			@params
			num1  =  the bits object representing the number 1
			num2  =  the bits object representing the number 2
		'''

		# check if the two 
		assert (num1.getSize() == num2.getSize()), "The two numbers must have same bit size"
			
		# if all goes well, proceed with the further algorithm
		bits1 = num1.getBits() # extract the bits for the two numbers
		bits2 = num2.getBits()

		print "The multiplication is to be carried out between: "
		print "No. 1: ", bits1
		print "No. 2: ", bits2


		# define the helper methods required for the algorithm
		def rsa(num):
			'''
				helper method 1 to perform the arithmetic right shift on the binary number
			
				@params
				num = the bitfield for the restricted number
			'''
		
			num.pop(len(num) - 1) # remove the last element of the bitfield
			num = [num[0]] + num
		
			return num[:]

		
		def rsc(num):
			'''
				helper method 2 to perform the circular right shift on the binary number
			
				@params
				num = the bitfield for the restricted number

				@return
				a bitfield of the multiplication of the two numbers
			'''
		
			bit = num.pop(len(num) - 1) # remove the last element of the bitfield
			num = [bit] + num
		
			return num[:]

		def add(n1, n2):
			'''
				helper method 3 to add the bitfields of two binary numbers
				*** Truncates the final carry by default ***			

				@params
				n1 = the bitfield for the restricted number1
				n2 = the bitfield for the restricted number2

				**** Implementation can be improved ****
			'''		
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
				helper method 4 to calculate the 2's complement of the binary number
			
				@params
				num = the bitfield for the restricted number
			'''
			for i in range(len(num)): # flip every bit of the input number
				if(num[i] == 1):
					num[i] = 0
				else:
					num[i] = 1
				
			return add(num[:], ([0 for i in range(len(num) - 1)] + [1])[:]) # add 1 and return

				
		# The actual algorithm loop starts from here: 
		uv = [0 for i in range(2 * len(bits1))] # initialize the uv array
		x = bits1[:] # just renaming it for simplicity's sake
		y = bits2[:] + [0 for i in range(len(bits2))]		
		_y = t2scomp(bits2[:]) + [0 for i in range(len(bits2))] # the -y value
		x_1 = 0 # the x - 1 bit for the required algorithm


		# start the loop for the algorithm
		for i in range(len(x)):

			if(x[-1] == 0 and x_1 == 1):
				# add case
				uv = add(uv[:], y[:])				

			elif(x[-1] == 1 and x_1 == 0):
				# sub case
				uv = add(uv[:], _y[:])			
			
			uv = rsa(uv[:]) # right shift uv array
			x_1 = x[-1] # update the x - 1 value
			x = rsc(x[:])
	
			print "Current Step: ", i + 1
			print uv, "\n"
		
		print "Answer of Multiplication: ", uv
		return uv
