"""Simple patch that gives you the number of seconds of music you have written given the tempo and time signature.

  sample run:
  
  python bars_to_time.py 16 4 60
  
  64.00000000000000000000000002"""

import sys
from decimal import *


def bars_needed(n_bars, beats_bar, beats_minute):
	"""Returns the number of seconds, n bars of music will produce given the tempo and time signature."""

	seconds = Decimal(n_bars) * Decimal(beats_bar) / Decimal(beats_minute) * 60
	

	return seconds


if __name__ == '__main__':


	if len(sys.argv) != 4:

		print 'Enter arguments: number bars, beats/bar, beats/minute'

	else:
		
		print bars_needed(sys.argv[1], sys.argv[2], sys.argv[3])
