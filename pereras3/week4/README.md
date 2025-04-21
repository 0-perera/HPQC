
## MPI_Send():
- nlocks send until the message has been copied
Hello, I am 3 of 4. Sent 30 to Rank 0
Hello, I am 1 of 4. Sent 10 to Rank 0
Hello, I am 2 of 4. Sent 20 to Rank 0
Hello, I am 0 of 4. Received 10 from Rank 1
Hello, I am 0 of 4. Received 20 from Rank 2
Hello, I am 0 of 4. Received 30 from Rank 3

## MPI_Ssend():
- blocks the program until the receiver gets the message, ensuring synchronisation
Hello, I am 0 of 4. Received 10 from Rank 1
Hello, I am 0 of 4. Received 20 from Rank 2
Hello, I am 0 of 4. Received 30 from Rank 3
Hello, I am 1 of 4. Sent 10 to Rank 0
Hello, I am 3 of 4. Sent 30 to Rank 0
Hello, I am 2 of 4. Sent 20 to Rank 0

## MPI_Bsend():
- place the message on a buffer and send it while running the rest, therefore the receiver and the sender are not sync.
Hello, I am 1 of 4. Sent 10 to Rank 0
Hello, I am 2 of 4. Sent 20 to Rank 0
Hello, I am 3 of 4. Sent 30 to Rank 0
Hello, I am 0 of 4. Received 10 from Rank 1
Hello, I am 0 of 4. Received 20 from Rank 2
Hello, I am 0 of 4. Received 30 from Rank 3

## MPI_Rsend():
- sends expecting the receiver is available
Hello, I am 1 of 4. Sent 10 to Rank 0
Hello, I am 0 of 4. Received 10 from Rank 1
Hello, I am 3 of 4. Sent 30 to Rank 0
Hello, I am 2 of 4. Sent 20 to Rank 0
Hello, I am 0 of 4. Received 20 from Rank 2
Hello, I am 0 of 4. Received 30 from Rank 3

