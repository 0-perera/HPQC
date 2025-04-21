#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

// declares the functions that will be called within main
// note how declaration lines are similar to the initial line
// of a function definition, but with a semicolon at the end;
int check_args(int argc, char **argv);
void initialise_vector(int vector[], int size, int initial);
void print_vector(int vector[], int size);
int sum_vector(int vector[], int size);
void check_uni_size(int uni_size);

int main(int argc, char **argv)
{
  // declare and initialise error handling variable
  int ierror = 0;
  int my_rank, uni_size;
  
  // intitalise MPI
	ierror = MPI_Init(&argc, &argv);
	// declare and initialise the numerical argument variable
	int num_arg = check_args(argc, argv);

  // gets the rank and world size
	ierror = MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
	ierror = MPI_Comm_size(MPI_COMM_WORLD, &uni_size);

  // checks the universe size is correct
	check_uni_size(uni_size);

	// checks what task to do and does it
	check_task(uni_size, my_rank, num_arg);

	// finalise MPI
	ierror = MPI_Finalize();
	return 0;
}


//root_task():
// Collects the messages sent by the clients and sum them 
// all together, printing the final result

int root_task(int uni_size)
{

	// creates and initialies transmission variables
	int recv_message, count, source, tag;
	recv_message = source = tag = 0;
	count = 1;
	MPI_Status status;

  // creates and intiialises the variable for the final output
	int output_sum = 0;
	
	// iterates through all the other ranks
	for (source = 1; source < uni_size; source++)
	{
		// receives the messages
		MPI_Recv(&recv_message, count, MPI_INT, source, tag, MPI_COMM_WORLD, &status);
		// adds the values to a running tally
		output_sum += recv_message;

    // prints the sum
	  printf("Sum: %d\n", output_sum);
    return output_sum;
	} // end for (source = 1; source < uni_size; source++)



// client_task(): 
// sends to the root a value (num_arg)  and its position (my_rank) in the MPI communicator
void client_task(int my_rank, int num_arg)
{
	// creates and initialies transmission variables
	int send_message, count, dest, tag;
	send_message = dest = tag = 0;
	count = 1;

  int my_size = num_arg /2;
  if (my_rank == 1){
    my_size += (num_arg % 2);
  }
	// sets the destination for the message
	dest = 0; // destination is root
  
  // int my_vector[num_arg]; // suffers issues for large vectors
	int* my_vector = malloc (num_arg * sizeof(int));
	// and initialises every element to zero
	initialise_vector(my_vector, num_arg, 0);
	
  
  	// sums the vector
	int my_sum = sum_vector(my_vector, num_arg);

	// prints the sum
	printf("Sum: %d\n", my_sum);
  // creates the message

	// sends the message
	MPI_Send(&my_sum, count, MPI_INT, dest, tag, MPI_COMM_WORLD);
	// if we use malloc, must free when done!
	free(my_vector);

	return 0;
}




// defines a function to sum a vector of ints into another int
int sum_vector(int vector[], int size)
{
	// creates a variable to hold the sum
	int sum = 0;

	// iterates through the vector
	for (int i = 0; i < size; i++)
	{
		// sets the elements of the vector to the initial value
		sum += vector[i];
	}

	// returns the sum
	return sum;
}

// defines a function to initialise all values in a vector to a given inital value
void initialise_vector(int vector[], int size, int initial)
{
	// iterates through the vector
	for (int i = 0; i < size; i++)
	{
		// sets the elements of the vector to the initial value
		vector[i] = i + 1;
	}
}

// defines a function to print a vector of ints
void print_vector(int vector[], int size)
{
	// iterates through the vector
	for (int i = 0; i < size; i++)
	{
		// prints the elements of the vector to the screen
		printf("%d\n", vector[i]);
	}
}

// defines a function that checks your arguments to make sure they'll do what you need
int check_args(int argc, char **argv)
{
	// declare and initialise the numerical argument
	int num_arg = 0;

	// check the number of arguments
	if (argc == 2) // program name and numerical argument
	{
		// declare and initialise the numerical argument
		num_arg = atoi(argv[1]);
	}
	else // the number of arguments is incorrect
	{
		// raise an error
		fprintf(stderr, "ERROR: You did not provide a numerical argument!\n");
		fprintf(stderr, "Correct use: %s [NUMBER]\n", argv[0]);

		// and exit COMPLETELY
		exit (-1);
	}
	return num_arg;
}

// check_task():
// checks whether the process is the root (if rank == 0) or a client (else) ,  ending num_arg and my_rank
// to root_task() or client_task(), respectively, to ensure that the right task is performed
void check_task(int uni_size, int my_rank, int num_arg)
{
	// checks which process is running and calls the appropriate task
	if (0 == my_rank)
	{
		root_task(uni_size);
	} // end if (0 == my_rank)
	else // i.e. (0 != my_rank)
	{
		client_task(my_rank, num_arg);
	} // end else // i.e. (0 != my_rank)
}



void check_uni_size(int uni_size)
{
	// sets the minimum universe size
	int min_uni_size = 2;
	// checks there are sufficient tasks to communicate with
	if (uni_size >= min_uni_size)
	{
		return;
	} // end if (uni_size >= min_uni_size)
	else // i.e. uni_size < min_uni_size
	{
		// Raise an error
		fprintf(stderr, "Unable to communicate with fewer than %d processes.", min_uni_size);
		fprintf(stderr, "MPI communicator size = %d\n", uni_size);

		// and exit COMPLETELY
		exit(-1);
	}
}
