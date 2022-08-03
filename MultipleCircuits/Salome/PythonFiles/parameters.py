### AUTHORS: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 05/11/2021
### Units: SI otherwise indicated

### NB: list of solid, face etc. numbers correspond to numbered groups to be used in Elmer-CSC, Cast3M, SYRTHES, Code_Aster, for example. File names are used to upload existing files and generate files.


#################
### MATERIALS ###
#################
### Identify materials to solids according to ordering in list. see the list of "listOfConductiveSolids" for solid identification. The lsit should contain as much material as there are solids
listOfMaterials = ['SC', 'SC', 'SC', 'yoke', 'air']

#############
### LISTS ###
#############

### COLORS ###
cDict = {
'black':(0,0,0),
'blue':(0,0.3,1),
'cyan':(0.65,0.35,1),
'darkblue':(0,0,0.85),
'red':(1,0,0),
'darkred':(0.65,0,0),
'purple':(0,0.8,0.8),
'orange':(1,0.6,0.15),
'salmon':(1,0.33,0.5),
'brown':(0.5,0.5,0),
'green':(0,0.666667,0),
'darkgreen':(0,0.45,0),
'gray':(0.6,0.6,0.6),
'darkgray':(0.35,0.35,0.35)
}

### CONDUCTION SOLIDS ###
### File names to be called upon in main.py to create the corresponding solids (used to get the *.py for the main.py file: solidxxx_listOfConductiveSolidFileNames[i].py is loaded to create the geometry listOfConductiveSolidFileNames[i], xxx is a 3 digit number filled in from left with 0 if below 100):
listOfSolids = ['coil1', 'coil2', 'coil3', 'core', 'air']
### Definition of solid colors (each solid may have its own color for visualization):
listOfSolidColors = [cDict['orange'], cDict['orange'], cDict['orange'], cDict['gray'], cDict['blue']]


### FACES ###
### Faces for boundary conditions for conductive solids
### Face names. Boundary conditions:  imposed heat fluxes on flex 1 and 2 cross-section and imposed temperature on CCD package 2 upper surface.
listOfFaces = ['coil1Boundary', 'coil2Boundary', 'coil3Boundary', 'airBoundary']
### Definition of face colors
listOfFaceColors = [cDict['orange'], cDict['orange'], cDict['orange'], cDict['blue']]


### SUB-GEOMETRIES ###
### List of shape types to create groups for mesh/geometry purposes. Shape types: points, wires, faces, shells or solids.
### The groups are useful for futher geometry or mesh processing as they appear in the view panel and can be referred to

### Wires and edges
listOfEdges = ['axis']
### Definition of edge colors
listOfEdgeColors = [cDict['black']]


##########################
### GENERAL PARAMETERS ###
##########################

### CONVERSION ###
### inch to meter: 0.0254, millimeter to meter: 0.001, etc., or on user definition of basic unit system
scaling = 0.001; listOfParameterValues = [scaling]; listOfParameterNames = ['scaling']

### VISUALIZATION ###
### Intermediate solid creations
isIntermediateSolidViewWanted = 0
### Tool views in OCC
areToolsViewWanted = 0

### GROUPS ###
### Solids
areSolidGroupsWanted = 1
### Faces
areFaceGroupsWanted = 1
### Sub-Geometries
areEdgeGroupsWanted = 1
### Submeshes
areSubmeshGroupsWanted = 1
### Meshes
areMeshGroupsWanted = 1

### PARTITION/COMPOUND ####
### Partition (= 1) or compound (= 0):
### for assembly depending on the geometries, compound or bag of independent geometries, partition or union of geometries comparting faces. The groups of geometry are not the same between compounds and partitions (see geometricGroups.py).
isMakePartitionWanted = 1
### Glue faces:
### Independent of partition or compound, it allows to merge coincident faces. If the solids are in physicial contacts, it is necessary to glue the faces to obtain the most accurate result. For compounds, some of the groups of geometry may be changed (see geometricGroups.py).
isMakeGlueFacesWanted = 1

### MESH DEFINITION ###
### Tolerance for the glue faces algorithm
tolerance = 1e-6
### Error on mesh to be used by Code_Aster
errorOnMeshTolerance = 1e-6

### GEOMETRIC CONSTRUCTION ###
### Planar surfaces for face construction
isPlanarWanted = 1
### Direction of arc for construction
### Clockwise (= 0), counter-clockwise (= 1)
rotation = 0


################################
### DIMENSIONS OF GEOMETRIES ###
################################
### Include a list of values corresponding to given parameters. Generation of parameter lists for data saving and notebook generation.

### SOLIDS ###
### Solid001: circular coil 1
coilWidth = scaling*50; listOfParameterValues.append(coilWidth); listOfParameterNames.append('coilWidth')
coilThickness = scaling*50; listOfParameterValues.append(coilThickness); listOfParameterNames.append('coilThickness')
coilInnerRadius = scaling*200; listOfParameterValues.append(coilInnerRadius); listOfParameterNames.append('coilInnerRadius')
coilSeparation = 0.25*coilThickness; listOfParameterValues.append(coilSeparation); listOfParameterNames.append('coilSeparation')
coil1Position_z = 0.5*coilThickness+coilSeparation; listOfParameterValues.append(coil1Position_z); listOfParameterNames.append('coil1Position_z')

### Solid002: circular coil 2
coil2Position_z = -coil1Position_z-0.5*coilThickness; listOfParameterValues.append(coil2Position_z); listOfParameterNames.append('coil2Position_z')

# Solid004: magnetic core
coreRadius = coilInnerRadius+coilWidth; listOfParameterValues.append(coreRadius); listOfParameterNames.append('coreRadius')
coreHeight = 1.3*(3*coilThickness+2*coilSeparation); listOfParameterValues.append(coreHeight); listOfParameterNames.append('coreHeight')
corePosition_z = -0.5*coreHeight; listOfParameterValues.append(corePosition_z); listOfParameterNames.append('corePosition_z')

### Solid005: air
airRadius = 2*max(coreHeight,coilInnerRadius+coilWidth); listOfParameterValues.append(airRadius); listOfParameterNames.append('airRadius')


### TOOLS ###


pass
