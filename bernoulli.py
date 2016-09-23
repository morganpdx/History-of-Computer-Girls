#!/usr/bin/python
# This program attempts to calculate bernoulli numbers by faithfully recreating Ada Lovelace's original sequence of operations diagram

value_of_n = input('Enter a value for n: ')

variable_list = [1.0, 2.0, 1.0] #We start with n = 1 and work up to n = value_of_n

#The total number of variable locations should equal 20 + n 
#Since we've initialized it with 3 variables already, we need to add 17 + value_of_n
var_range = 17 + value_of_n

#Add the appropriate number of variable slots
for x in range(var_range):
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
	[6, '-', 13, 11, [13, 21]], #This should result in B1 during the first pass, where n = 1, and stored in 21 according to diagram
	[7, '-', 3, 1, [10]], #This operation determines if the engine continues processing.  if n = 1, it will equal zero, which means start over at operation 1 (or stop).
	[8, '+', 2, 7, [7]],
	[9, '/', 6, 7, [11]], 
	[10, '*', 21, 11, [12]],
	[11, '+', 12, 13, [13, 22]], #This should result in B3 during the second pass, where n = 2, and stored in 22 according to diagram
	[12, '-', 10, 1, [10]], #This operation determines if the engine continues processing.  if n = 2, it will equal zero, which means start over at operation 1 (or stop).
	[13, '-', 6, 1, [6]],
	[14, '+', 1, 7, [7]], 
	[15, '/', 6, 7, [8]],
	[16, '*', 8, 11, [11]],
	[17, '-', 6, 1, [6]],
	[18, '+', 1, 7, [7]],
	[19, '/', 6, 7, [9]],
	[20, '*', 9, 11, [11]],
	[21, '*', 22, 11, [12]],
	[22, '+', 12, 13, [13]], #This should result in B index n during the second pass, where n > 2, and stored in index 20+ according to diagram
	[23, '-', 10, 1, [10]], #This operation determines if the engine continues processing.  if n > 2, it will equal zero, which means start over at operation 1 (or stop).
	[24, '+', 13, 20 + int(variable_list[ada_index(3)]), [int(20 + variable_list[ada_index(3)])]], # This saves the value of B(index of value_of_n) to variable_list[20+value_of_n]
	[25, '+', 1, 3, [3]] 	#This iterates to the next value of value_of_n
]

#Perform the selected operation, report and save the results
def perform_operation(op_list, start_operation, end_operation):

	operand = op_list[1]
	val1 = variable_list[ada_index(op_list[2])]
	val2 = variable_list[ada_index(op_list[3])]
	destinations = op_list[4]

	for destination in op_list[4]:

		if operand == '+':
			variable_list[ada_index(destination)] = float(val1) + float(val2)

		elif operand == '-':
			variable_list[ada_index(destination)] = float(val1) - float(val2)

		elif operand == '*':
			variable_list[ada_index(destination)] = float(val1) * float(val2)

		elif operand == '/':
			variable_list[ada_index(destination)] = float(val1) / float(val2)

		print "Operation #{0} -- {1} {2} {3} = {4} (indices: {5}, {6}, {7})".format(op_list[0], val1, op_list[1], val2, variable_list[ada_index(destination)], op_list[2], op_list[3], destination)


#todo: Implement looping based on structure in diagram
def loop_operations():

	while variable_list[ada_index(3)] <= value_of_n:
		calculate_numbers(1, 25)

	#Print out final values of B for each index, starting with B index 1 at variable location 21
	for i in range(21, len(operations_list)-1):
		index_number = (2 * (i - 20)) - 1
		print "Value of B, index {0} is {1}".format(index_number, variable_list[ada_index(i)])


def calculate_numbers(start, stop):

	for i in range(start-1, stop):
		perform_operation(operations_list[i], 1, 25)


loop_operations()



