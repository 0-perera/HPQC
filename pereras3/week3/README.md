
# ~~~~~~~~~~~~~~~~~~~ #
# Part 1: hello_world #
# ~~~~~~~~~~~~~~~~~~~ #

  # hello_mpi.c #
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

  #check

  # hello_mpi_serial.c #
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




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Part 2: MPI exercise breakdown #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Flowchart












# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Part 3: MPI MPI Vector Addition  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
