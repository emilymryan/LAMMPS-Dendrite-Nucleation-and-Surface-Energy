#! /bin/bash -l
#$ -l h_rt=120:00:00
#$ -P ryanlab
#$ -m bea
#$ -j y
#$ -N nucl
#$ -o /projectnb/ryanlab/mmorey/LAMMPS_NUCLEATION/results/final/$JOB_NAME.o$JOB_ID
#$ -e /projectnb/ryanlab/mmorey/LAMMPS_NUCLEATION/results/final/$JOB_NAME.e$JOB_ID
#$ -pe mpi_16_tasks_per_node 64
module load openmpi/3.1.1
module load python3/3.6.5

lmp=/projectnb/ryanlab/mmorey/mylammps/src/lmp_mpi

dname1=wettingangle_180_19Apr24_${JOB_ID}
output=/projectnb/ryanlab/mmorey/LAMMPS_NUCLEATION/results/${dname1}
dname=${output}
mkdir -p ${dname}

mpirun -np $NSLOTS ${lmp} -in input.lmp -var dname ${dname}

exit

