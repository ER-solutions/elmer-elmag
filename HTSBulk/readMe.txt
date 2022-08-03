Multiphysics problem: magnetostatic, static elasticity and thermal analysis

If salome is used to generate the geometry and mesh:
“assembly.unv” built in Salome platform (Salome-ThermoMagnetic) and copied over to the Elmer-CSC case folder

Translation from *.unv to Elmer mesh:
ElmerGrid 8 2 assembly.unv -out MESH --autoclean

Solve without GUI (replace case.sif.ol by its corresponding case.sif):
ElmerSolver case.sif

If Gmsh is used to create the mesh:
Translation from Gmsh mesh *.msh to Elmer-CSC mesh format:
ElmerGrid 14 2 assembly.msh -out MESH --autoclean

Creation of entities.sif in subfolder with name of mesh (mesh.names) to get the correspondence between the mesh groups and the bodies defined in Elmer-CSC

2 User-defined Functions (UDF) was implemented (see Fortran90):
dissipation-REBCO.F90: compute the heat disturbance and the subsequent heat generation
thermalConductivity-REBCO.F90: provide the thermal conductivity tensor
elecricConductivity-REBCO.F90: provide the electrical conductivity

1 User-Defined Solver (UDS) was implemented:
regularizatio-Q.F90: filter the dissiaption to remove unrealistic points.  Steady State Min Iterations = 2 to loop at least once over the heat solver and the filter

compileUDF.sh allos to compile all the external UDF at once. Run it before running the solver.
