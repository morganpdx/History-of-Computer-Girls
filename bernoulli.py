#!/usr/bin/python
# This program attempts to calculate bernoulli numbers by faithfully recreating Ada Lovelace's original sequence of operations diagram

value_of_n = input('Enter a value for n: ')

variable_list = [1.0, 2.0, 1.0] #We start with n = 1 and work up to n = value_of_n

#The number of variable locations should equal 20 + n.  Since we've initialized it with 2 variables already, range should be 18 + n:
for x in range(17 + value_of_n):
	variable_list.append(0.0)

print('Number of variable slots: ' + str(len(variable_list)))


# All Ada's indexes are 1 based, so for ease of recording subtract 1 from all indexes listed in the diagram
def ada_index(index):
	return index - 1


#Line number, operation, operand 1, operand 2, index to store result(s) 
operations_list = [
	[1, '*', 2, 3, [4, 5, 6]],
	[2, '-', 4, 1, [4]],
	[3, '+', 5, 1, [5]],
	[4, '/', 5, 4, [11]],
	[5, '/', 11, 2, [11]],
	[6, '-', 13, 11, [13]], 
	[7, '-', 3, 1, [10]],
	[8, '+', 2, 7, [7]],
	[9, '/', 6, 7, [11]], #This should result in B1 during the first pass, where n = 1, and stored in 21 according to diagram
	[10, '*', 21, 11, [12]],
	[11, '+', 12, 13, [13]], 
	[12, '-', 10, 1, [10]],
	[13, '-', 6, 1, [6]],
	[14, '+', 1, 7, [7]], #This should result in B3 during the second pass, where n = 2, and stored in 22 according to diagram
	[15, '/', 6, 7, [8]],
	[16, '*', 8, 11, [11]],
	[17, '-', 6, 1, [6]],
	[18, '+', 1, 7, [7]],
	[19, '/', 6, 7, [9]],
	[20, '*', 9, 11, [11]],
	[21, '*', 22, 11, [12]],
	[22, '+', 12, 13, [13]],
	[23, '-', 10, 1, [10]],
	[24, '+', 13, 24, [24]],
	[25, '+', 1, 3, [3]] 	#This should result in B to the 2n-1 during each subsequent pass, where n > 2, and stored in location(20 + n) 
]

#Perform the selected operation, report and save the results
def perform_operation(op_list):

	operand = op_list[1]
	val1 = variable_list[ada_index(op_list[2])]
	val2 = variable_list[ada_index(op_list[3])]
	destinations = op_list[4]

	for destination in op_list[4]:

		if operand == '+':
			variable_list[ada_index(destination)] = val1 + val2

		elif operand == '-':
			variable_list[ada_index(destination)] = val1 - val2			

		elif operand == '*':
			variable_list[ada_index(destination)] = val1 * val2

		elif operand == '/':
			variable_list[ada_index(destination)] = val1 / val2

		print('#' + 
			str(op_list[0]) + 
			': ' + 
			str(val1) + 
			' ' + op_list[1] + ' ' +
			str(val2) + 
			' = ' + 
			str(variable_list[ada_index(destination)]) + 
			'(indices: ' + 
			str(op_list[2]) + 
			', ' + 
			str(op_list[3]) + 
			', ' + 
			str(destination) + 
			')')


def calculate_numbers():
	i = 0
	while i < len(operations_list):
		perform_operation(operations_list[i])
		i = i + 1


calculate_numbers()



