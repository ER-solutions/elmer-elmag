# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 12/09/2013


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Vertexes
vertex001 = geompy.MakeVertex(0., -1.5*coreCoilRadius, 0.)
vertex002 = geompy.MakeVertex(0., 1.5*coreCoilRadius, 0.)

# Edges
edge001 = geompy.MakeEdge(vertex001, vertex002)

# Volume
solid006 = geompy.MakeSphereR(airRadius)
solid006 = geompy.MakeCut(solid006, geompy.MakeCompound(listForAssembly))


# List of geometries #
listOfsolid006 = [solid006, edge001]
listForAssembly.append(solid006)
listForAssembly.append(edge001)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid006, "view006: air"))


pass
