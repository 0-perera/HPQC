import sys
import time
from pathlib import Path

def main(): 
	print('fine')
	start_time = time.time()
	output = 0
	try:
		# checks if there are the right number of arguments
		# converts the first two arguments to integers
		in_arg = int(sys.argv[1])
		multiple = int(sys.argv[2])
	except: # (argc != 2)
		# raises an error
		raise Exception("Incorrect arguments.\nUsage: python repeat_adder.py [NUM] [NUM]\ne.g.\npython repeat_adder.py 2 3")
	
	# iterates over all numbers up to the input
	for i in range(in_arg):
		# adds the index to the output
		output = output + multiple
	
	# prints the output
	print("{}\n".format(output))
	end_time = time.time()
	run_time = end_time - start_time
	return run_time
cwd = Path.cwd()
fn = '/home/ug/pereras3/HPQC/pereras3/week2'
print(fn)
output_file = open(fn+'/output_times.txt', 'a')
if __name__ == "__main__":
        output_file.write(main())
output_file.close()
