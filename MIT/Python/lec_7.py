
# examples of structured code
# 
#import math

# Get base
#inputOK = False
#while not inputOK:
#	base = input('Enter base: ')
#	if type(base) == type(1.0): inputOK = True
#	else: print('Enter base must be a floating point number')

# Get Height
#inputOK = False
#while not inputOK:
#	height = input('Enter height: ')
#	if type(height) == type(1.0): inputOK = True
#	else: print('Enter Height must be a floating point number')

#hyp = math.sqrt(base * base + height * height)

#print "Base: " + str(base) + " , height " + str(height) + " , hyp: " + str(hyp) 

import math

def getFloat(requestMsg, errorMsg):
	inputOK = False
	while not inputOK:
		val = input(requestMsg)
		if type(val) == type(1.0): inputOK = True
		else: print(errorMsg)
	return val

base = getFloat('Enter base: ', 'Error: base must be a float')
height = getFloat('Enter height: ', 'Error: height must be a float') 

hyp = math.sqrt(base * base + height * height)

print "Base: " + str(base) + " , height " + str(height) + " , hyp: " + str(hyp) 
