# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/26/2019


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Outer face #
# Vertex
vertex001 = geompy.MakeVertex((-1)*racetrackLength/2, (-1)*(racetrackWidth+racetrackInnerRadius), 0.0)
vertex002 = geompy.MakeVertex(racetrackLength/2, (-1)*(racetrackWidth+racetrackInnerRadius), 0.0)
vertex003 = geompy.MakeVertex(racetrackLength/2+racetrackWidth+racetrackInnerRadius, 0.0, 0.0)
vertex004 = geompy.MakeVertex(racetrackLength/2, racetrackWidth+racetrackInnerRadius, 0.0)
vertex005 = geompy.MakeVertex((-1)*racetrackLength/2, racetrackWidth+racetrackInnerRadius, 0.0)
vertex006 = geompy.MakeVertex((-1)*racetrackLength/2-racetrackWidth-racetrackInnerRadius, 0.0, 0.0)

vertexCenter001 = geompy.MakeVertex(racetrackLength/2, 0.0, 0.0)
vertexCenter002 = geompy.MakeVertex((-1)*racetrackLength/2, 0.0, 0.0)

# Edges
listEdges = list()
listEdges.append(geompy.MakeEdge(vertex001, vertex002))
listEdges.append(geompy.MakeArcCenter(vertexCenter001, vertex002, vertex003, rotation))
listEdges.append(geompy.MakeArcCenter(vertexCenter001, vertex003, vertex004, rotation))
listEdges.append(geompy.MakeEdge(vertex004, vertex005))
listEdges.append(geompy.MakeArcCenter(vertexCenter002, vertex005, vertex006, rotation))
listEdges.append(geompy.MakeArcCenter(vertexCenter002, vertex006, vertex001, rotation))

# Wire
wire_1 = geompy.MakeWire(listEdges, tolerance)

# Face
face_1 = geompy.MakeFace(wire_1, isPlanarWanted)

# Volume
solid002_1 = geompy.MakePrismDXDYDZ(face_1, 0., 0., racetrackThickness)

# Inner face #
# Vertex
vertex001 = geompy.MakeVertex((-1)*racetrackLength/2, (-1)*racetrackInnerRadius, 0.0)
vertex002 = geompy.MakeVertex(racetrackLength/2, (-1)*racetrackInnerRadius, 0.0)
vertex003 = geompy.MakeVertex(racetrackLength/2+racetrackInnerRadius, 0.0, 0.0)
vertex004 = geompy.MakeVertex(racetrackLength/2, racetrackInnerRadius, 0.0)
vertex005 = geompy.MakeVertex((-1)*racetrackLength/2, racetrackInnerRadius, 0.0)
vertex006 = geompy.MakeVertex((-1)*racetrackLength/2-racetrackInnerRadius, 0., 0.0)

vertexCenter001 = geompy.MakeVertex(racetrackLength/2, 0., 0.0)
vertexCenter002 = geompy.MakeVertex((-1)*racetrackLength/2, 0., 0.0)

# Edges
listEdges = list()
listEdges.append(geompy.MakeEdge(vertex001, vertex002))
listEdges.append(geompy.MakeArcCenter(vertexCenter001, vertex002, vertex003, rotation))
listEdges.append(geompy.MakeArcCenter(vertexCenter001, vertex003, vertex004, rotation))
listEdges.append(geompy.MakeEdge(vertex004, vertex005))
listEdges.append(geompy.MakeArcCenter(vertexCenter002, vertex005, vertex006, rotation))
listEdges.append(geompy.MakeArcCenter(vertexCenter002, vertex006, vertex001, rotation))

# Wire
wire_2 = geompy.MakeWire(listEdges, tolerance)

# Face
face_2 = geompy.MakeFace(wire_2, isPlanarWanted)

# Volume
solid002_2 = geompy.MakePrismDXDYDZ(face_2, 0., 0., racetrackThickness)
solid002 = geompy.MakeCut(solid002_1, solid002_2)
solid002 = geompy.MakeTranslation(solid002, 0., 0., -(0.5*gap+racetrackThickness))

# List of geometries #
listOfSolid002 = [solid002]
listForAssembly.append(solid002)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid002, "view002:racetrack_2"))


pass
