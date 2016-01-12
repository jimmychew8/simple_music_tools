"""Takes in n command line arguments. Each integer represents 
the number of counts in a cycle. Prints simulation. Last argument 
specifies bar length. 

Sample run:

  rhythm_cycle_simulator.py 5 7 9 4
  
|X---|-X--|--X-|---X|----|X---|-X--|--X-|---X|----|X---|-X--|--X-|--
|X---|---X|----|--X-|----|-X--|----|X---|---X|----|--X-|----|-X--|--
|X---|----|-X--|----|--X-|----|---X|----|----|X---|----|-X--|----|--

A cycle of 5 counts on the first line, a cycle of 7 counts on the second,
a cycle of 9 counts on the third, in a bar lenght of 4 counts.

"""

import sys

def cycle(count, bar_length, length_string=54):
	"""Returns a string of X, 0, and |. X denotes the start of 
	the cycle occuring at an interval count. | is the start of
	a new bar."""

	cycle = ''


	for i in range(length_string):

		if i % bar_length == 0:

			cycle += '|'

		if i % count == 0:

			cycle += 'X'

		else:

			cycle += '-'


	return cycle


def main():
	"""Main program."""

	for i in range(num_concurrent_cycles):

		if i == 0:

			pass

		else:


			print cycle(int(sys.argv[i]), bar_length)


if __name__ == '__main__':

	num_concurrent_cycles = len(sys.argv) - 1
	bar_length = int(sys.argv[-1])

	main()
