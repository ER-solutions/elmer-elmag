# AUTHORS: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 12/09/2013
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
# Used in the geometric groups to define submesh refinment over coils
numberOfCoils = 4
# solid name: (material, color)
solidDict = {
    'racetrack1': ('SC', colorDict['orange']),
    'racetrack2': ('SC', colorDict['orange']),
    'coil1': ('SC', colorDict['orange']),
    'coil2': ('SC', colorDict['orange']),
    'core': ('iron', colorDict['gray']),
    'straps': ('G10', colorDict['green']),
    'air': ('air', colorDict['blue'])
}

# face name: color
faceDict = {
    'racetrack1Boundary': colorDict['orange'],
    'racetrack2Boundary': colorDict['orange'],
    'coil1Boundary': colorDict['orange'],
    'coil2Boundary': colorDict['orange'],
    'fixedTemperature4K': colorDict['blue'],
    'fixedTemperature50K': colorDict['red'],
    'heatRadiation': colorDict['salmon'],
    'airBoundary': colorDict['gray']
}

# edge name: color
edgeDict = {
    'axis': colorDict['black']
}


# PARAMETERS #
GlobalFileName = 'superbend-quench'

# Main files to be run:
runTools = 1
runGeometries = 1
runAssembly = 1
runVisualization = 1
runMeshing = 1
# Visualization (debugging phase):
isIntermediateSolidViewWanted = 0
areToolsViewWanted = 0
# Groups:
areSolidGroupsWanted = 1
areFaceGroupsWanted = 1
areEdgeGroupsWanted = 1
areSubmeshGroupsWanted = 1
areMeshGroupsWanted = 1


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

# Miscellaneous:
gap = scaling*46
listOfParameterValues.append(gap)

# SOLIDS
# Solid001 and 2: racetracks
racetrackWidth = scaling*33
listOfParameterValues.append(racetrackWidth)

racetrackThickness = scaling*50
listOfParameterValues.append(racetrackThickness)

racetrackLength = scaling*80
listOfParameterValues.append(racetrackLength)

racetrackInnerRadius = scaling*20
listOfParameterValues.append(racetrackInnerRadius)

# Solid003 and 4: circular coils
coilWidth = scaling*16
listOfParameterValues.append(coilWidth)

coilThickness = scaling*46
listOfParameterValues.append(coilThickness)

coilInnerRadius = scaling*0.5*208
listOfParameterValues.append(coilInnerRadius)

# solid005: core
coreDX = scaling*500
listOfParameterValues.append(coreDX)

coreDY = scaling*269
listOfParameterValues.append(coreDY)

coreDZ = scaling*348
listOfParameterValues.append(coreDZ)

chamfer_D1 = scaling*50
listOfParameterValues.append(chamfer_D1)

chamfer_D2 = scaling*50
listOfParameterValues.append(chamfer_D2)

# solid006: straps
coreLegDX = scaling*17
listOfParameterValues.append(coreLegDX)

coreLegDY = scaling*10
listOfParameterValues.append(coreLegDY)

coreLegDZ = scaling*68
listOfParameterValues.append(coreLegDZ)

coreLegLength = scaling*550
listOfParameterValues.append(coreLegLength)

coreLegDistance = scaling*168
listOfParameterValues.append(coreLegDistance)

# Solid007: air
airRadius = 1.25*coreLegLength
listOfParameterValues.append(airRadius)

# TOOLS
# Tool007:
coreInnerHoleDX = scaling*270.0
listOfParameterValues.append(coreInnerHoleDX)

coreInnerHoleDY = scaling*400.0
listOfParameterValues.append(coreInnerHoleDY)

coreInnerHoleDZ = scaling*146.0
listOfParameterValues.append(coreInnerHoleDZ)

coreCoilRadius = scaling*0.5*257.5
listOfParameterValues.append(coreCoilRadius)


pass
