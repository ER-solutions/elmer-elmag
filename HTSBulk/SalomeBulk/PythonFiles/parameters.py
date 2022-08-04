# AUTHORS: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 01/02/2022
# Units: SI otherwise indicated


folderDict = {
    'hdf': parentPathDirectoryName+'/'+'HdfFiles'+'/',
    'dat': parentPathDirectoryName+'/DataFiles/',
    'med': parentPathDirectoryName+'/MedFiles/',
    'unv': parentPathDirectoryName+'/UnvFiles/'
}
listOfExtentions = list(folderDict.keys())

colorDict = {
    'black': (0.0, 0.0, 0.0),
    'blue': (0.0, 0.3, 1.0),
    'cyan': (0.65, 0.35, 1.0),
    'darkblue': (0.0, 0.0, 0.85),
    'red': (1.0, 0.0, 0.0),
    'darkred': (0.65, 0.0, 0.0),
    'purple': (0.0, 0.8, 0.8),
    'orange': (1.0, 0.6, 0.15),
    'salmon': (1.0, 0.33, 0.5),
    'brown': (0.5, 0.5, 0.0),
    'green': (0.0, 0.666667, 0.0),
    'darkgreen': (0.0, 0.45, 0.0),
    'gray': (0.6, 0.6, 0.6),
    'darkgray': (0.35, 0.35, 0.35)
}


# GEOMETRIES #
# Used in the geometric groups to define submesh refinment
numberOfSubmeshToBeRefined = 1
# solid name: (material, color)
solidDict = {
    'bulk': ('SC', colorDict['black']),
    'air': ('air', colorDict['blue'])
}

# face name: color
faceDict = dict()
for k in list(solidDict.keys())[0:numberOfSubmeshToBeRefined]:
    faceDict[k+"Boundary"] = colorDict['red']
faceDict["airBoundary"] = colorDict['blue']

# edge name: color
edgeDict = {
    'axis': colorDict['black']
}


# PARAMETERS #
GlobalFileName = 'bulk'

# Main files to be run:
runTools = 0
runGeometries = 1
runAssembly = 1
runVisualization = 1
runMeshing = 0
# Visualization (debugging phase):
isIntermediateSolidViewWanted = 0
areToolsViewWanted = 0
# Groups:
areSolidGroupsWanted = 1
areFaceGroupsWanted = 1
areEdgeGroupsWanted = 0
areSubmeshGroupsWanted = 0
areMeshGroupsWanted = 0


# PARTITION/COMPOUND #
# Partition (= 1) or compound (= 0):
# for assembly depending on the geometries, compound or bag of independent
# geometries, partition or union of geometries comparting faces.
# The groups of geometry are not the same between compounds and partitions
# (see geometricGroups.py).
isMakePartitionWanted = 1
# Glue faces:
# Independent of partition or compound, it allows to merge coincident faces.
# If the solids are in physicial contacts, it is necessary to glue the faces
# to obtain the most accurate result. For compounds, some of the groups of
# geometry may be changed (see geometricGroups.py).
isMakeGlueFacesWanted = 1


# MESH DEFINITION #
# Tolerance for the glue faces algorithm:
tolerance = 1e-6
# Error on mesh to be used by Code_Aster:
errorOnMeshTolerance = 1e-6


# GEOMETRIC CONSTRUCTION #
# Planar surfaces for face construction:
isPlanarWanted = 1
# Direction of arc for construction: Clockwise (= 0), counter-clockwise (= 1)
rotation = 0


# DIMENSIONS OF GEOMETRIES #
# definition of basic unit system
# inch to meter: 0.0254, millimeter to meter: 0.001, etc., or on user
scaling = 0.001
listOfParameterValues = [scaling]

# SOLIDS
# Solid001: SC bulk
bulk1Radius = scaling*15
listOfParameterValues.append(bulk1Radius)

bulk1Height = scaling*15
listOfParameterValues.append(bulk1Height)

# Solid002: air
airRadius = scaling*30
listOfParameterValues.append(airRadius)

airHeight = scaling*30
listOfParameterValues.append(airHeight)


pass
