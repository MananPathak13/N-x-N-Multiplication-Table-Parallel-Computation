#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_VALUE 100000000

// Function to count distinct elements in a given range
long countDistinct(long start, long end, long N) {
    bool *found = (bool *)calloc(N + 1, sizeof(bool));
    long count = 0;
    for (long i = 1; i <= N; i++) {
        for (long j = start; j <= end && j <= N; j++) {
            long product = i * j;
            if (product <= N && !found[product]) {
                found[product] = true;
                count++;
            }
        }
    }
    free(found);
    return count;
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Assuming N is passed as a command line argument
    if (argc < 2) {
        if (world_rank == 0) {
            fprintf(stderr, "Usage: %s <N>\n", argv[0]);
        }
        MPI_Finalize();
        return 1;
    }
    long N = atol(argv[1]);
    if (N > MAX_VALUE) {
        if (world_rank == 0) {
            fprintf(stderr, "N should be less than or equal to %d\n", MAX_VALUE);
        }
        MPI_Finalize();
        return 1;
    }

    // Divide the work among processes
    long range_per_process = N / world_size;
    long start = world_rank * range_per_process + 1;
    long end = (world_rank == world_size - 1) ? N : start + range_per_process - 1;

    // Each process counts its range
    long local_count = countDistinct(start, end, N);

    // Reduce all local counts to the root process
    long total_count;
    MPI_Reduce(&local_count, &total_count, 1, MPI_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    // Root process prints the result
    if (world_rank == 0) {
        printf("Total distinct elements in %ld x %ld multiplication table: %ld\n", N, N, total_count);
    }

    MPI_Finalize();
    return 0;
}
