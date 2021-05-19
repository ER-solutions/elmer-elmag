# NOTES!!!

FOR RUNNING THE CASES YOU NEED THE LATEST (https://github.com/ElmerCSC/elmerfem/commit/824778ae6b0ba788cff3b8aecf0c474fdcf5648e) FROM: https://github.com/ElmerCSC/elmerfem/tree/CoilSolverGUI 
This is needed because the normalized current is regularized and the patch for that is in the aforementioned branch.

Run in bash mode: bash run.sh or ./run.sh

# Electromagnetic and thermal model of a superconducting coil connected to an external circuit.

Background: Superbenb design made of 4 coils to wave the beam of electron for a light source application.

The model includes the coupling with external circuits. A quencch is initiated inside one of the coils.
