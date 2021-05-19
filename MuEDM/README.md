# NOTES!!!

Run in bash mode: bash run.sh or ./run.sh

# Electromagnetic model of MuEDM barrel model.

Background: Trapping of muon using a magnetic field and an electrostatic field.

The current density is impressed in the coils manually which impairs the use of the coilSolver and the addition of an "Electric Conductivity" in the material section. A fix is considered for the CoilSolver to get it work for long thin solenoid.

The current idea is to determined the best current density distribution using the existing coils to get a fairly homogeneous field at the center of the magnet with the following characteristics: the magnetic flied along z = +/-0.75 m is about 99.9% of the field at z=0.
