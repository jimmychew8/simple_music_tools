"""Simple musical canon simulator. Without transpositions.

Takes in a following arguments in the order as follows:
	1) string denoted a rhythmic scheme as argument and
	2) number of counts in a bar.
	
The first argument is your canon. Here are examples of how you may represent
the canon from the command line: purely rythmically, ie X--X-X--X--X, or 
by pitch, ie EDCDEEEeDDDdEGG_EDCDEEEEDDEDCccc. The second argument is your 
barring structure. If you want your canon to be in 4/4, enter 4. For 5/4, 
enter 5.

"""


import sys


def canon(rhythm_scheme, count):
	"""Yields the rhythmic scheme displaced by each step organized by
	each bar count with a | symbol to denote bar count."""

	for offset in range(len(rhythm_scheme)):

		r = ' ' * offset + rhythm_scheme

		yield '|'.join(r[i:i+count] for i in range(0, len(r), count))


def main():
	"""Main program."""

	timeline = sys.argv[1]
	count = int(sys.argv[2])

	for i, rhythm in enumerate(canon(timeline, count)):

		
		original_barred = '|'.join(timeline[i:i+count] for i in range(0, len(timeline), count))

		if i < 10:


			print i, original_barred

			print ' ', rhythm

			print ''

		else:

			print i, original_barred

			print '  ', rhythm

			print ''



if __name__ == '__main__':

	if len(sys.argv) != 3:

		print 'Enter 2 arguments: rhythmic scheme, count per bar.'

	if len(sys.argv[1]) > 100:

		print 'Timeline too long.'

	else:

		main()
