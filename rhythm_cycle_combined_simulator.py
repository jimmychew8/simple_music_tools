# Expends the previous rhythm cycle patch. 
# Adds a combined cycle feature
# that reveals the composite rhythm.

import sys


def cycle(count, bar_length, length_string=104):
	"""
	Returns a string representation of a single cycle.
	'X' denotes a rhythmic hit, '-'' indicates a rest.'|'' 
	represents the start of a new bar.
	"""

	cycle = ''

	for i in range(length_string):

		if i % bar_length == 0:

			cycle += '|'

		if i % count == 0:

			cycle += 'X'

		else:

			cycle += '-'


	return cycle


def combine_cycles(lists_of_cycles):
	"""
	Takes in a list of lists of all cycles and prints a 
	cycle that indicates any instance when there was a hit
	amongst the cycles.
	"""

	combined_cycle = ['-' for i in range(len(lists_of_cycles[0]))]


	for cycle in lists_of_cycles:

		for i in range(len(cycle)):

			if cycle[i] == '|':

				combined_cycle[i] = '|'

			elif cycle[i] == 'X':

				combined_cycle[i] = 'X'


	combined_c = ''


	for i in combined_cycle:


		combined_c += i


	print 'Combined Cycle:'


	print combined_c


	return None



def main():

	cycles = []

	for i in range(num_concurrent_cycles):


		if i == 0: # Get ride of first sys argument.


			pass


		else:


			print cycle(int(sys.argv[i]), bar_length)


			cycles.append(list(cycle(int(sys.argv[i]), bar_length)))



	combine_cycles(cycles)


if __name__ == '__main__':


	if len(sys.argv) < 2:


		print 'Enter, counts per rhythmic cycle (as many as you want), barring structure.'


	else:

		num_concurrent_cycles = len(sys.argv) - 1
		bar_length = int(sys.argv[-1])

		main()
