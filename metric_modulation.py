"""
A simple metric modulation calculator for music.

sample run: 

python metric_modulation.py 60 3 2 5 2
change: 1.666666666666666666666666667
new tempo: 36.0

In the original tempo of 60 bpm, two of the triplet subdivision
equal two of the quintuplet subdivision in the new tempo of 36 bpm.
The new beat is 5/3 longer than the original.

The arguments should be given in the order as follows:
	previous tempo, 
	previous subdivion,
	number of previous subdivions, 
	new subdivision,
	number of new subdivions

*****

beats per minute (bpm)
t0 = previous bpm
t1 = new bpm

bpm = 1 min / time for each beat

	c = fraction change between the 2 bpm's
	c = (number of previous subdivision / previous subdivision) 
	* (new subdivision / number of new subdivion)

time for each beat = c * (1 min / t0)

"""


import sys
from decimal import *


def modulate(previous_bpm, 
	previous_subdivision, 
	num_of_previous_subdivisions, 
	new_subdivision, 
	num_of_new_subdivisions):
	"""Returns the new bpm (tempo) given the previous 
	bpm. The previous and new subdivisions are intenger value 
	specified as follows: 2=eight, 3=triplet, 
	4=sixteenth, 5=quintuplet, etc."""

	change = (Decimal(num_of_previous_subdivisions) / Decimal(previous_subdivision) \
		* (Decimal(new_subdivision) / Decimal(num_of_new_subdivisions)))

	print 'change:', change


	return float(1 / (Decimal(change) * (1 / Decimal(previous_bpm))))


def main():
	"""Main program."""

	print 'new tempo:', modulate(
			int(sys.argv[1]), 
			int(sys.argv[2]), 
			int(sys.argv[3]), 
			int(sys.argv[4]), 
			int(sys.argv[5])
			)


if __name__ == '__main__':

	message = 'Enter: previous tempo, previous subdivion, \
	number of previous subdivions, new subdivision, \
	number of new subdivions.'

	if len(sys.argv) != 6:

		print message

	else:
		
		main()
