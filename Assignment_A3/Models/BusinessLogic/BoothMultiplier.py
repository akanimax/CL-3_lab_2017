from BitFieldsOperations import * # the library created by botman present in the same package


''' The following error handler function is no longer required as there are no more assertion errors being thrown from the code below'''
# error handler function for AssertionError types of errors
#def handleAssertionError():
#	'''
#		Helper method for the api to be used to handle the various types of assertion errors that might be thrown
#	'''
#	_, _, tb = sys.exc_info()
#	tb_info = traceback.extract_tb(tb)
#	filename, line, func, text = tb_info[-1]
#	error = text.split(",")[-1]
#
#	print "An error occured: " + error



class BitNibbles:
	'''
		The class that converts a number into binary and stores the bits in its object
	'''

	def __convert_to_binary(self, number):
		'''
			Private helper method to convert the given integer into list of bits
		'''

		bits = [int(digit) for digit in bin(abs(number))[2:]] # get the list of bits

		# nibble size optimisation of the bitfield
		while(len(bits) % 4 != 0):
			bits = [0] + bits # add a 0 in the front

		# if the first bit is 1, we have to still add 4 more 0s
		if(bits[0] == 1):
			bits = [0 for i in range(4)] + bits

		# if the number is negative, represent it in the 2's complement form
		if(number < 0):
			bits = t2scomp(bits[:])

		return bits


	def __init__(self, integer): # default size of limit is 8 bits
		'''
			Default constructor of the class.

			@params
			integer = the number that needs to be converted to bits
			limit  	= size of the binary number in bits. by default it is 8 bits i.e. 2 nibbles
		'''

		# convert the number from decimal to a binary bitfield
		bitfield = self.__convert_to_binary(integer)

		# private data attributes
		self.__size = len(bitfield) // 4 # a reference to the current size of the bitfield in number of nibbles
		self.__bits = bitfield # assign the bitfield to the bits



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
			num1  =  the BitNibbles object representing the number 1
			num2  =  the BitNibbles object representing the number 2
		'''
		# extract the bits for the two numbers
		bits1 = num1.getBits()
		bits2 = num2.getBits()

		# equalize the lengths of the bitfields for the two numbers
		bits1, bits2 = bitLenEqualize(bits1[:], bits2[:])


		# verbose log statements for the console
		print "\n\nThe multiplication is to be carried out between: "
		print "No. 1: ", bits1
		print "No. 2: ", bits2


		# The actual algorithm starts from here:
		# some more comments added for readability

		# refer the video link -> https://www.youtube.com/watch?v=1aTR9WQFFtM
		# for more information. I have used the same names for the variables used in the video.

		# the uv array keeps the final answer
		uv = [0 for i in range(2 * len(bits1))] # initialize the uv array to all 0s


		# number 1 for the multiplication (multiplicand)
		x = bits1[:] # just renaming it for simplicity's sake (as used in the video)


		# number 2 for the multiplication (multiplier)
		y = bits2[:] + [0 for i in range(len(bits2))] # again name changed and size adjusted
		# although, the add function now adjusts the size, I have still kept it like this


		# the -ve of the the second number that needs to be added in some cases
		_y = t2scomp(bits2[:]) + [0 for i in range(len(bits2))] # basically, the -y value

		# the (x - 1) bit required for the algorithm.
		x_1 = 0 # always initialized to 0


		# start the loop for the algorithm
		for i in range(len(x)):

			# if the last bit of x is 0 and (x-1) bit is 1, take this action
			if(x[-1] == 0 and x_1 == 1):
				# case when y value is to be added to the answer (uv)
				uv = add(uv[:], y[:])

			# if the last bit of x is 1 and (x-1) bit is 0, take this action
			elif(x[-1] == 1 and x_1 == 0): # this cannot be simple else, because there are two more cases (0, 0) and (1, 1)
				# case when y value is to be subtracted (add 2's complement of the y value)
				uv = add(uv[:], _y[:])


			# in every case, this has to be always performed

			# arithmetic right shift uv array by 1
			uv = rsa(uv[:], 1)

			# update the x - 1 value
			x_1 = x[-1]

			# circular right shift the x value by 1
			x = rsc(x[:], 1)

			# verbose log statements
			print "Current Step: ", i + 1
			print uv, "\n"

		# verbose log statements
		print "Answer of Multiplication: ", uv
		return uv
