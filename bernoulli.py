#!/usr/bin/python
# This program attempts to calculate bernoulli numbers based on Ada Lovelace's original sequence of operations diagram

value_of_n = input('Enter a value for n: ')

variable_list = [1.0, 2.0, float(value_of_n)]
for x in xrange(1,22):
	variable_list.append(0.0)


# All Ada's indexes are 1 based, so for ease of recording subtract 1 from all indexes listed in the diagram
def ada_index(index):
	return index - 1


#Line number, operation, operand 1, operand 2, index to store result (optional other locations to store same result)
operations_list = [
	[1, '*', variable_list[ada_index(2)], variable_list[ada_index(3)], 4, 5, 6],
	[2, '-', variable_list[ada_index(4)], variable_list[ada_index(1)], 4],
	[3, '+', variable_list[ada_index(5)], variable_list[ada_index(1)], 5],
	[4, '/', variable_list[ada_index(5)], variable_list[ada_index(4)], 11],
	[5, '/', variable_list[ada_index(11)], variable_list[ada_index(2)], 11],
	[6, '-', variable_list[ada_index(13)], variable_list[ada_index(11)], 13],
	[7, '-', variable_list[ada_index(3)], variable_list[ada_index(1)], 10],
	[8, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[9, '/', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[10, '*', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[11, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[12, '-', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[13, '-', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[14, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[15, '/', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[16, '*', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[17, '-', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[18, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[19, '/', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[20, '*', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[21, '*', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[22, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[23, '-', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[24, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4],
	[25, '+', variable_list[ada_index(2)], variable_list[ada_index(3)], 4]
]

#Perform the selected operation, report and save the results
def perform_operation(operand, val1, val2, destination):
	if operand == '+':
		print('Adding ' + str(val1) + ' and ' + str(val2))
		variable_list[destination] = val1 + val2

	elif operand == '-':
		print('Subtracting ' + str(val1) + ' and ' + str(val2))
		variable_list[destination] = val1 - val2

	elif operand == '*':
		print('Multiplying ' + str(val1) + ' and ' + str(val2))
		variable_list[destination] = val1 * val2

	elif operand == '/':
		print('Dividing ' + str(val1) + ' and ' + str(val2))
		variable_list[destination] = val1 / val2

	print('Storing result in ' + str(destination) + ': ' + str(variable_list[destination]))


def calculate_numbers():
	for op in operations_list:
		if len(op) > 4:
			for n in range(4, len(op)):
				perform_operation(op[1], op[2], op[3], op[n])


calculate_numbers()


