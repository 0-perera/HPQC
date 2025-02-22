import sys
import time

def main(): 
	for i in range(0,4):
		#prints in terminal
		if i==0:
			start_time = time.time()
			input_file = open('input_file.csv', delimeter=',')
			in_arg = input_file[0]
			multiple = input_file[1]
			for i in range(in_arg):
				# adds the index to the output
				output = output + multiple
				print("{}\n".format(output))
		else:
			try:
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

			
			
		elif i==2:
		
		# prints the output
		
		end_time = time.time()
		run_time = end_time - start_time
		if i==0:
			print(f'run_time in sec = {run_time}')
		if i==1:
			cwd = Path.cwd()
			fn = '/home/ug/pereras3/HPQC/pereras3/week2'
			print(fn)
			output_file = open(fn+'/output_times.txt', 'a')
			

if __name__ == "__main__":
        main()
