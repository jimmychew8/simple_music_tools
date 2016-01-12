# simple_music_tools
I'll be adding some very simple 'calculator' type programs to help out with music composing in python 2.7.
1) Bar count gives you the amount of music in time (in seconds) you have written given the bar and time signature. Sample run: 

  python bars_to_time.py 16 4 60
  
  64.00000000000000000000000002

2) Rhythm cycle simulator sample run: 

  rhythm_cycle_simulator.py 5 7 9 4
  
|X---|-X--|--X-|---X|----|X---|-X--|--X-|---X|----|X---|-X--|--X-|--
|X---|---X|----|--X-|----|-X--|----|X---|---X|----|--X-|----|-X--|--
|X---|----|-X--|----|--X-|----|---X|----|----|X---|----|-X--|----|--

A cycle of 5 is displayed on the first line, a cycle of 7 on the second, a cycle of 9 on the third line in a 
bar structure of 4 counts. 
