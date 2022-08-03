### AUTHORS: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 05/11/2021

### NB: list of solid, face etc. numbers correspond to numbered groups to be used in Elmer-CSC, Cast3M, SYRTHES, Code_Aster, for example. File names are used to upload existing files and generate files.


############################
### AUTOMATIC GENERATION ###
############################
### Not to be filled in, used by the code for automatic processing.

### SOLIDS ###
### Conduction solids
### Initialization of the conduction solid groups to be used in external solver:
listOfSolidGroups = list()
### Initialization of the conduction solid group Salome identification to be used during printing:
listOfSolidGroupIDs = list()
### Initialization of the list of conduction solids to be assembled (see assembly.py)
listForAssembly = list()
### Numbering and names of solid for the visualization and to be passed to the solver:
listOfSolidNumbers = list()
for i in range(0, len(listOfSolids)):
  listOfSolidNumbers.append("SOL"+"{0:03d}".format(i+1))
listOfSolidMeshGroups = list()

### FACES ###
### Boundary conditions for conduction solids:
### Initialization of the conduction face groups:
listOfFaceGroups = list()
### Initialization of the conduction face groups:
listOfFaceGroupIDs = list()
### Numbering of conduction faces and names to be passed to solver:
listOfFaceNumbers = list()
for i in range(0, len(listOfFaces)):
  listOfFaceNumbers.append("FAC"+"{0:03d}".format(i+1))
listOfFaceMeshGroups = list()


### SUB-GEOMETRIES ###
### Wires and edges:
listOfEdgeGroups = list()
listOfEdgeGroupIDs = list()
listOfEdgeNumbers = list()
for i in range(0, len(listOfEdges)):
  listOfEdgeNumbers.append("EDG"+"{0:03d}".format(i+1))
listOfTempraryEdgeIDs = list()
### List of meshes to be retrieved:
listOfEdgeMeshes = list()
listOfEdgeMeshGroups = list()


### GEOMETRY PROPERTIES ###
### Properties of geometries to be saved in "../DataFiles/basicProperties.dat" (see properties.py)
dictionaryOfBasicProperties = dict()
### define the precision of the float to be printed out.
floatPrecision = "{0:.3g}"


################
### NOTEBOOK ###
################
### Register the various defined parameters. Automatic generated.

notebook = salome_notebook.notebook
for i, value in enumerate(listOfParameterNames):
    notebook.set(value, listOfParameterValues[i])


#################
### DATA FILE ###
#################
### Create a data files. Automatically generated from definition of parameters.

### File listing parameters for Gmsh ###
myFile001 = open(pathDirectoryNameOfDataFiles+'data.dat', 'w')
for i, value in enumerate(listOfParameterNames):
    myFile001.write("$ "+value+"="+str(listOfParameterValues[i])+';\n')
myFile001.close()
print("* Creation of data file: data.par")

### Creation of readMe.txt file, listing the geometries and the corresponding material ###
myFile002 = open(pathDirectoryNameOfDataFiles+'readMe.txt', 'w')
myFile002.write('********************\n')
myFile002.write('*** SALOME MODEL ***\n')
myFile002.write('********************\n\n')
myFile002.write('*** AUTHOR: Frederic Trillaud\n')
myFile002.write('*** DATE: '+str(date.today())+'\n\n')
myFile002.write('*** INTRODUCTION: Correspondence solid ids and actual geometries including the material for each geometry.\n\n')
myFile002.write('*** Solids ***\n')
for i, v in enumerate(listOfSolidNumbers):
  myFile002.write(v+' = '+listOfSolids[i]+", material: "+listOfMaterials[i]+'\n')
myFile002.write('\n*** Faces ***\n')
for i, v in enumerate(listOfFaceNumbers):
  myFile002.write(v+' = '+listOfFaces[i]+'\n')
myFile002.write('\n*** Edges ***\n')
for i, v in enumerate(listOfEdgeNumbers):
  myFile002.write(v+' = '+listOfEdges[i]+'\n')
myFile002.close()
print("* Creation of information file: readMe.txt")


########################
### BASIC GEOMETRIES ###
########################

### Origin ###
OOO = geompy.MakeVertex(0, 0, 0)

#### Main coordinates (Cartesian) ###
VX = geompy.MakeVectorDXDYDZ(1, 0, 0)
VY = geompy.MakeVectorDXDYDZ(0, 1, 0)
VZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

### Basic planes ###
planeVXVZ = geompy.MakePlane2Vec(VX, VY, 1)
planeVYVZ = geompy.MakePlane2Vec(VY, VX, 1)
planeVXVY = geompy.MakePlane2Vec(VX, VZ, 1)
planes = geompy.MakeCompound([planeVXVY, planeVXVZ, planeVYVZ])


pass
