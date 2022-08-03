############
### BASH ###
############

### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### PLACE: Instituto de Ingenieria, UNAM
### DATE (English): 07/30/2020

#! /bin/bash

### Variables ###
echo " "
echo "*** COMPILATION OF UDF (FORTRAN90) ***"
cd ./Fortran90

echo " "
echo "  *** COMPILATION: electricConductivity-REBCO.f90 ***"
echo " "
elmerf90 -o electricConductivity-REBCO.so electricConductivity-REBCO.F90
echo " "
echo "  *** DONE ***"
echo " "
echo "  *** COMPILATION: thermalConductivity-REBCO.f90 ***"
echo " "
elmerf90 -o thermalConductivity-REBCO.so thermalConductivity-REBCO.F90
echo " "
echo "  *** DONE ***"
echo "  *** COMPILATION: dissipation-REBCO.f90 ***"
echo " "
elmerf90 -o dissipation-REBCO.so dissipation-REBCO.F90
echo " "
echo "  *** DONE ***"
echo " "
echo "  *** COMPILATION: regularization.f90 ***"
echo " "
elmerf90 -o regularization-Q.so regularization-Q.F90
echo " "
echo "  *** DONE ***"

cd ..
echo " "

