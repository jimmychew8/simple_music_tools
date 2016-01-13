This repository  
Search
Pull requests
Issues
Gist
 @jimmychew8
 Unwatch 1
  Star 0
  Fork 0 jimmychew8/simple_music_tools
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
simple_music_tools/ 
metric_modulation_generator.py
 or cancel
    
 Edit new file   Preview
"""
A metric modulation scheme. 
Takes in the following as arguments in order as follows:
	starting tempo,
	ending tempo,
	maximum subdivision
	maxium deviation (# of +/- bpms the resultant bmp can deviate 
		inclusively within)
Subdivisions are denoted as such:
	1=quarter,
	2=eigth,
	3=triplet,
	4=16th,
	5=quintuplets,
	6=sextuplets
	7=septuplets
	8=octuplets 
***
sample run:
python metric_modulation_generator.py 54 162 4 0
end: 162 start: 54
ratio:  0.333333333333
(3 1) = (1 1) || dev: 0.0 bpm
(3 2) = (1 2) || dev: 0.0 bpm
(1 1) = (1 3) || dev: 0.0 bpm
(2 1) = (2 3) || dev: 0.0 bpm

The above console is interpreted as follows:
	3 quarter notes in the previous bpm = 1 quarter note in the new bpm
	3 eight notes in the previous bpm = 1 eight in the new bpm
"""

import sys
from decimal import *


def generate_modulation(start_tempo, end_tempo, max_sub, max_dev):
	"""Returns a tuple that meet the metric modulation criteria in
	the following form:
		(previous subdivision, 
		# previous subdivision, 
		new subdivision, 
		# new subdivision, 
		error)."""


	change_ratio = Decimal(start_tempo) / Decimal(end_tempo)

	print 'end:', end_tempo, 'start:', start_tempo
	print 'ratio: ', float(change_ratio)


	for num_new_sub in range(max_sub):


		for new_sub in range(max_sub):


			for num_prev_sub in range(max_sub):


				for prev_sub in range(max_sub):

					try:

						# Eliminate common multiples
						if num_new_sub == new_sub and num_new_sub != 1: 

							pass

						elif num_prev_sub == prev_sub and num_prev_sub != 1:

							pass

						elif num_prev_sub % prev_sub == 0 and prev_sub != 1: 

							pass

						elif num_new_sub % new_sub == 0 and new_sub != 1:

							pass


						else:

							generated_ratio = Decimal(float(num_prev_sub) \
							 / float(prev_sub)) * Decimal(float(new_sub) \
							 / float(num_new_sub))

							dev = generated_ratio * Decimal(start_tempo) \
							- end_tempo


							if abs(dev) <= max_dev:

								# In case you prefer this format.
								# print '({} {}) = ({} {}) || dev: \
								# {}'.format(
									# num_prev_sub, 
									# rhythm_denom[prev_sub],
									# num_new_sub,
									# rhythm_denom[new_sub],
									# int(dev)
									# )

								print '({} {}) = ({} {}) || dev: {} bpm'.format(
									num_prev_sub, 
									prev_sub,
									num_new_sub,
									new_sub,
									float(dev)
									)

					except ZeroDivisionError:

						pass


def main():
	"""Main program."""
	generate_modulation(
		int(sys.argv[1]), 
		int(sys.argv[2]), 
		int(sys.argv[3]), 
		int(sys.argv[4])
		)


if __name__ == '__main__':

	rhythm_denom = { 
			  1 : 'quarters',
			  2 : 'eigths',
			  3 : 'triplets',
			  4 : 'sixteenths',
			  5 : 'quintuplets',
			  6 : 'sextuplets',
			  7 : 'septuplets',
			  8 : 'octuplets'
	}

	if len(sys.argv) != 5:

		print 'Enter: starting tempo, ending tempo, max subdivision \
		(1=quarter, 2=eigth, 3=triplet, etc), maxium deviation'

	else:

		main()
