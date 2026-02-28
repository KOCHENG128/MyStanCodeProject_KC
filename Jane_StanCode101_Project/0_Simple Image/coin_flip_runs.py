"""
File: coin_flip_runs.py
Name: Jane Huang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program find the continuous flip result for the random flips
	if any of continuous H or T flips string exceed num_run, the flip stops
	"""
	print('Let\'s flip a coin')
	num_run = int(input('Number of runs: '))
	flips_count = 0
	all_flips = ''
	previous_flip = ''
	string = ''

	# 第一次flip,特殊處理
	flip = r.randint(0, 1)
	if flip == 0:
		flip = 'T'
	else:
		flip = 'H'
	all_flips += flip
	previous_flip = flip
	string = flip

	# 如果相同，放入同一個盒子flips_count，如果不同，盒子重新累積
	while flips_count < num_run:
		flip = r.randint(0, 1)
		if flip == 0:
			flip = 'T'
		else:
			flip = 'H'
		all_flips += flip
		if flip == previous_flip:
			string += flip
			flips_count = len(string)
			previous_flip = flip
		else:
			string = flip
			previous_flip = flip
			flips_count = len(string)
	print(all_flips)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
