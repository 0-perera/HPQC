

# Part 1: hello_world 

  ## hello_mpi.c 
- 2 process
  - real    0m0.394s
  - user    0m0.098s
  - sys     0m0.080s
  - user + sys = 0m0.178 << real
- 4 process
  - real    0m0.391s
   - user    0m0.133s
   - sys     0m0.128s
   - user + sys = 0m0.261 < real
- 8 process
  - real    0m0.403s
  - user    0m0.202s
  - sys     0m0.239s
  - user + sys = 0m0.441 > real

  the greater the loop, the running time will increase meaningfully.

  ## hello_mpi_serial.c #
- 2 process
  - real    0m0.004s
  - user    0m0.002s
  - sys     0m0.000s
  - user + sys = 0m0.002 < real
- 4 process
  - real    0m0.003s
  - user    0m0.002s
  - sys     0m0.000s
  - user + sys = 0m0.002 < real
- 8 process
  - real    0m0.003s
  - user    0m0.002s
  - sys     0m0.000s
  - user + sys = 0m0.002 < real

It is observe that using a parrallel code reduced the running time by an order of 2 ciphers. The difference of runtime is also smaller between the scenarios presented.


# Part 2: MPI exercise breakdown 
-  Flowchart





# Part 3: MPI MPI Vector Addition 

## vector_serial.c
- output for 10:
  - real    0m0.002s
  - user    0m0.002s
  - sys     0m0.000s
- output for 10 000:
  - real    0m0.002s
  - user    0m0.001s
  - sys     0m0.001s
- - output for 10 000 000:
  - real    0m0.086s
  - user    0m0.062s
  - sys     0m0.024s

for each ouput, the code was run a few times, and it was observed that user + sys was always near to real time, sometimes a bit smaller, greater or equal. However, is also observed how the bigger the vector the slower the code, but with an exponential behaviour since there was a step of 10^3 between the 3 cases, and for the vector 10 and 10^4, the code runtime was similar while for 10^8 was much  greater.


## vector_parallel.c

 create the parallel version
