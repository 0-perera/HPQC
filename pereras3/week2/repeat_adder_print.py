import sys
import time
import csv

def main(): 
	for goals in range(0,2):
		#prints in terminal
		if goals==0:
			goal = 'read file input'
			start_time = time.time()
			input_file = open('input_file.csv', 'a')
			input_file.write('4, 5')
			csv.reader(input_file, delimiter=' ')
			in_arg = input_file[0]
			multiple = input_file[1]
		else:
			goal = 'human input'
			try:
				start_time = time.time()
				# checks if there are the right number of arguments
				# converts the first two arguments to integers
				in_arg = int(sys.argv[1])
				multiple = int(sys.argv[2])
			except: # (argc != 2)
				# raises an error
				raise Exception("Incorrect arguments.\nUsage: python repeat_adder.py [NUM] [NUM]\ne.g.\npython repeat_adder.py 2 3")
		for i in range(in_arg):
			# adds the index to the output
			output = output + multiple
			print("{}\n".format(output))	
			# iterates over all numbers up to the input
		
		# prints the output
		end_time = time.time()
		run_time = end_time - start_time
		print(f'run_time in sec = {run_time}')
		
		output_text = open('/output_times.txt', 'a')
		out_file = open('/output_times.csv', 'a')
		output_text.writelines(f'for {goal} of {in_arg} x {multiple}, the runtime was {run_time}s.\n}')
		output_file.writelines(f'{goal}, {in_arg}, {multiple} ./n')
		output_file.close()
		output_tetx.close()
		
		

if __name__ == "__main__":
        main()
