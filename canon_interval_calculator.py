
# A program that gives intervals in a canon.
# The program prints horizontal intervals between melodies.


import sys
import string


def transpose(interval, melody):
	"""
	Returns a list containing a melody tranposed up or down
	at the specified interval.
	"""

	melody = [int(note) for note in list(melody)]

	
	for i in range(len(melody)): 

		melody[i] += interval - 1 # Scale degrees is not 0 indexed.


	return melody


def generate_melodies(melody, offset_interval):
	"""
	Yields melodies at the offset interval.
	"""

	for i in range(len(melody)):

		offset_melody = (i * offset_interval * '0') + melody


		yield offset_melody


def interval(melody, melody_2):
	"""
	Takes two string lists as arguments. 
	Yields an integer interval value.
	"""

	for i in range(len(melody)):


		if int(melody[i]) >= int(melody_2[i]):

			if int(melody_2[i]) == 0:

				interval = int(melody[i])

			else:

				interval = abs(int(melody[i]) - int(melody_2[i])) + 1


		if int(melody[i]) < int(melody_2[i]):

			if int(melody[i]) == 0:

				interval = int(melody_2[i])

			else:

				# Multiple by -1 if you want to see intervals below.
				interval = abs(int(melody[i]) - int(melody_2[i])) + 1


		yield interval


def main():
	"""
	Compares intervals between the melody and offset melody. 
	Prints the melody, offset melody, and intervals.
	"""
	for count, offset_melody in enumerate(generate_melodies(sys.argv[1], int(sys.argv[2]))):


		print sys.argv[1] + count * '0'


		print offset_melody


		total_intervals = ''


		for j in interval(list(sys.argv[1] + count * '0'), offset_melody):


			total_intervals += str(j)

		print '-' * len(total_intervals)


		print total_intervals


if __name__ == '__main__':

	if len(sys.argv) != 3:

		# Represent the canon in scale degrees as in the example below.
		print 'Enter a canon. example: 3222_2111_1777_7666, and offset value'

	else:

		main()
