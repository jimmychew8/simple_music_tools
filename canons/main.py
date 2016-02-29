
import sys
import string


def transpose(self, interval, melody):
    """
    Returns a list containing a melody tranposed up or down
    at the specified interval.
    """

    melody = [int(note) for note in list(melody)]


    for i in range(len(melody)):

            melody[i] += interval - 1 # Scale degrees is not 0 indexed.


    return melody


def generate_melodies(self, melody, offset_interval):
    """
    Yields melodies at the offset interval.
    """

    for i in range(len(melody)):

        offset_melody = (i * offset_interval * '0') + melody


        yield offset_melody


def interval(self, melody, melody_2):
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


def compare(melody, offset_value):
    """
    Takes in a string representation of a melody, and an offset
    value to which a second string is placed. Subtracts the first
    melody from the second melody to compare the interval difference. Returns the interval difference."""
    for count, offset_melody in enumerate(generate_melodies(melody), int(offset_value))):

            print melody + count * '0'


            print offset_melody


            total_intervals = ''


            for j in interval(list(melody + count * '0'), offset_melody):


                    total_intervals += str(j)

            print '-' * len(total_intervals)


            print total_intervals
