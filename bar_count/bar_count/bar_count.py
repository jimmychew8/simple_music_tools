"""
Calculates the number of seconds of music you have written
given the following paremeters:
    # of bars,
    beats per bar,
    tempo given in beats per minute (bpm)

sample run:

bar_count
"""
import sys
from decimal import *

import click

@click.command()
@click.option('--bars',
              prompt=True,
              help='The number of bars.')
@click.option('--beats_bars',
              prompt=True,
              help='Number of beats per bar.')
@click.option('--beats_minute',
              prompt=True,
              help='Beats per minute (tempo).')
def bars_needed(bars,
                beats_bars,
                beats_minute):
	"""Returns the number of seconds, n bars of music will produce
        given the tempo and time signature.
        """

	seconds = (Decimal(n_bars) *
                   Decimal(beats_bar) /
                   Decimal(beats_minute) * 60)

        print seconds

if __name__ == '__main__':
    bars_needed()
