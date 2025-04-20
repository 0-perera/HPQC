#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
// function declarations
int root_task(int uni_size);
void client_task(int my_rank);
void check_uni_size(int uni_size);
void check_task(int uni_size, int my_rank);

// main():
// Ensures that the user gave a numerical input. Then, sets up MPI, 
// to ensure messages can pass between processes. It also identifies 
// the type of processes to ensure that the data goes through the right operation.
int main(int argc, char **argv) 
{
	// declare and initialise error handling variable
	int ierror = 0;

	// declare and initialise the numerical argument variable
	int num_arg = check_args(argc, argv);

	// intitalise MPI
	ierror = MPI_Init(&argc, &argv);
	
	// declare and initialise rank and size varibles
	int my_rank, uni_size;
	my_rank = uni_size = 0;

	

	// gets the rank and world size
	ierror = MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	ierror = MPI_Comm_size(MPI_COMM_WORLD,&uni_size);

		// checks the universe size is correct
	check_uni_size(uni_size);

	// checks what task to do and does it
	check_task(uni_size, my_rank, num_arg);

	// finalise MPI
	ierror = MPI_Finalize();
	return 0;
}

	
int root_task(int uni_size)
{
	// creates and initialies transmission variables
	int recv_message, count, dest, source, tag;
	recv_message = dest = source = tag = 0;
	count = 1;
	MPI_Status status;
	// iterates through all the other ranks
		for (int their_rank = 1; their_rank < uni_size; their_rank++)
		{
			// sets the source argument to the rank of the sender
			source = their_rank;

			// receives the messages
			MPI_Recv(&recv_message, count, MPI_INT, source, tag, MPI_COMM_WORLD, &status);

			// prints the message from the sender
			printf("Hello, I am %d of %d. Received %d from Rank %d\n",
					my_rank, uni_size, recv_message, source);
		} // end for (int their_rank = 1; their_rank < uni_size; their_rank++)
} // end if (0 == my_rank)



void client_task(int my_rank)
{

	int send_message, count, dest, tag;
	dest = tag = 0;
	count = 1;

	send_message = my_rank * 10;

	// sends the message
	MPI_Send(&send_message, count, MPI_INT, dest, tag, MPI_COMM_WORLD);

	// prints the message from the sender
	printf("Hello, I am %d of %d. Sent %d to Rank %d\n",
			 my_rank, uni_size, send_message, dest);
} // end if (uni_size > 1)


// check_uni_size():
// makes sure that there is at least one process (the root)
// before the program keeps running
void check_uni_size(int uni_size)
{
	// sets the minimum universe size
	int min_uni_size = 1;
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


// check_task():
// checks whether the process is the root (if rank == 0) or a client (else) ,  ending num_arg and my_rank
// to root_task() or client_task(), respectively, to ensure that the right task is performed
void check_task(int uni_size, int my_rank)
{
	// checks which process is running and calls the appropriate task
	if (0 == my_rank)
	{
		root_task(uni_size);
	} // end if (0 == my_rank)
	else // i.e. (0 != my_rank)
	{
		client_task(my_rank);
	} // end else // i.e. (0 != my_rank)
}

