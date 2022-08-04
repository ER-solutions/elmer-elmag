# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 11/29/2012


# Solids:
if areSolidGroupsWanted:
    print(' *** Solids: ')
    for i in range(0, len(listOfSolids)):
        listOfSolidGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['SOLID']))
    # SOL001: racetrack 1
    k = 0
    listOfTemporarySolidIDs = [2]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL002: racetrack 2
    k = k+1
    listOfTemporarySolidIDs = [94]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL003: coil 1
    k = k+1
    listOfTemporarySolidIDs = [186]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL004: coil 2
    k = k+1
    listOfTemporarySolidIDs = [208]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL005: core
    k = k+1
    listOfTemporarySolidIDs = [230, 354, 344, 372, 368, 358, 382]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL006: air
    k = k+1
    listOfTemporarySolidIDs = [392]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])

# Faces:
if areFaceGroupsWanted:
    print(' *** Faces:')
    if listOfFaces:
        for i in range(0, len(listOfFaces)):
            listOfFaceGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['FACE']))
        k = 0
        # FAC001: air boundary
        # k = k+1
        listOfTemporaryFaceIDs_air = [394]
        for j, v in enumerate(listOfTemporaryFaceIDs_air):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])

# Edges:
if areEdgeGroupsWanted:
    print(' *** Edges:')
    if listOfEdges:
        for i in range(0, len(listOfEdges)):
            listOfEdgeGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['EDGE']))
        # EDG001: axis
        k = 0
        listOfTemporaryEdgeIDs_axis = [402]
        for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
            geompy.AddObject(listOfEdgeGroups[k], v)
        print(listOfEdgeNumbers[k]+': '+listOfEdges[k])

# Submesh:
if areSubmeshGroupsWanted:
    print(' *** Submeshed solids: coils')
    submeshSolidGroup = geompy.CreateGroup(assembly, geompy.ShapeType['SOLID'])
    geompy.UnionList(submeshSolidGroup, listOfSolidGroups[0:numberOfCoils])

    print(' *** Submeshed faces: air boundary')
    submeshFaceGroup = geompy.CreateGroup(assembly, geompy.ShapeType['FACE'])
    for j, v in enumerate(listOfTemporaryFaceIDs_air):
        geompy.AddObject(submeshFaceGroup, v)

    print(' *** Submeshed edges: axis')
    submeshEdgeGroup = geompy.CreateGroup(assembly, geompy.ShapeType['EDGE'])
    for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
        geompy.AddObject(submeshEdgeGroup, v)


pass
