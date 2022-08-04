# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 01/02/2022
# Units: SI otherwise indicated


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+': '+listOfSolids[len(listForAssembly)])

# Vertexes #
vertex001 = geompy.MakeVertex(0., 0., -1.1*bulk1Height)
vertex002 = geompy.MakeVertex(0., 0., 1.1*bulk1Height)

# Edges #
edge001 = geompy.MakeEdge(vertex001, vertex002)

# Volume #
# solid002 = geompy.MakeSphereR(airRadius)
solid002 = geompy.MakeCylinderRH(airRadius, airHeight)
solid002 = geompy.MakeTranslation(solid002, 0., 0., -0.5*airHeight)
solid002 = geompy.MakeCut(solid002, geompy.MakeCompound(listForAssembly))

# List of geometries #
listOfsolid002 = [solid002, edge001]
listForAssembly.append(solid002)
listForAssembly.append(edge001)

# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid002, 'view002: air'))


pass
