import math

import math

def digits(number, base): #this calculates how many digits are required to represent a number in a given base
	if number == 0:
		return 1
	else:
		logarithm = math.log(number, base)
		if logarithm >= int(logarithm):
			return int(logarithm) + 1
		else:
			return int(logarithm)

base = 2 #base for the analysis
start_num = 0 #smallest number of interest
end_num = 7 #larget number of interest
num_list = list(range(start_num, end_num + 1)) #list of all the numbers of interest
list_length = digits(end_num, base)

def base_rep(number, base): #this generates the representation of a number in a given base
	upper_bound = digits(number, base) #this lest us know the maximum power we have to use with the base
	output = [] #generate an empty list
	length_differential = list_length - upper_bound
	#adding zeros as necessary to make the final output as long as the largest output
	if length_differential > 0:
		counter = length_differential
		while counter > 0:
			output.append(0)
			counter -= 1
	#creating the base representation of the number	
	i_range = reversed(range(0, upper_bound, 1)) #using the upper_bound, we reverse the order to allow for the computation of the base number
	for i in i_range:
		i_val = number // base**i
		output.append(i_val)
		number = number - ((i_val) * (base**i))
	return output

dict_0525 = {x:base_rep(x, base) for x in num_list}
print(dict_0525)