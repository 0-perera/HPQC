#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv) 
{
	clock_t on = clock();
	// creates and initialises the variables
	int i, input, output, multiple;
	i = input = output = multiple = 0;

	// checks if there are the right number of arguments
	if (argc == 3)
	{
		// converts the first argument to an integer
		input = atoi(argv[1]);
		multiple = atoi(argv[2]);
	}
	else //(argc != 3)
	{
		// raises an error
		fprintf(stderr, "Incorrect arguments.  Usage: repeat_adder [NUM] [NUM]\ne.g. \n repeat_adder 2 3\n");
		// and crashes out
		exit(-1);
	}
	
	// iterates over all numbers up the input
	for (i = 0; i < input; i++)
	{
		// adds the index to the output
		output = output + multiple;
	}
	printf('heyo');
	// prints the output
	printf("%d\n", output);
	return 0;
	clock_t off = clock();
	run_time = (double)(off - on) / CLOCKS_PER_SEC);
	printf("Elapsed: %f seconds\n", run_time);
}
