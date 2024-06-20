# N-x-N-Multiplication-Table-Parallel-Computation
This project implements a parallel program in C using MPI (Message Passing Interface) to compute the number of distinct elements in an N by N multiplication table. It is designed for execution on a supercomputer and can handle multiplication tables with up to 100,000,000 values.

**Requirements**
MPI library (e.g., MPICH, OpenMPI)
C compiler (e.g., GCC)
(Optional) Conda environment setup
Installation
To set up the project, clone this repository or download the source files to your local machine or supercomputer environment.

**Compilation**
Use an MPI compiler wrapper to compile the program. For example, with MPICH or OpenMPI:

mpicc -o mpi_mult_table mpi_mult_table.c

**Execution**
Run the program using mpiexec or an equivalent command on your supercomputer. For example:

mpiexec -n <number_of_processes> ./mpi_mult_table <N>
where <number_of_processes> is the number of parallel processes you want to use, and <N> is the size of the multiplication table (N x N).

**Configuration**
No additional configuration is needed. Make sure MPI is correctly installed and configured in your environment.

**Usage Example**
To compute the number of distinct elements in a 10,000 x 10,000 table using 4 processes:

mpiexec -n 4 ./mpi_mult_table 10000       
Contributing
Contributions to this project are welcome. Please send pull requests or issue reports via GitHub or email me at path7107@mylaurier.ca

**License**
This project is open source and available under the MIT License.
