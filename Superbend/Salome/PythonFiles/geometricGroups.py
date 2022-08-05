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
    listOfTemporarySolidIDs = [2] #5
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL002: racetrack 2
    k = k+1
    listOfTemporarySolidIDs = [94] #97
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
    listOfTemporarySolidIDs = [230, 470, 446, 456, 460, 432, 442]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL06: straps
    k = k+1
    listOfTemporarySolidIDs = [576, 480, 648, 552, 624, 528, 600, 504]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL007: air
    k = k+1
    listOfTemporarySolidIDs = [672] # 675
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])

# Faces:
if areFaceGroupsWanted:
    print(' *** Faces:')
    if listOfFaces:
        for i in range(0, len(listOfFaces)):
            listOfFaceGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['FACE']))
        # FAC001: racetrack 1
        k = 0
        listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[k], geompy.ShapeType['SHELL'], True)
        geompy.UnionList(listOfFaceGroups[k], listOfTemporaryFaceIDs)
        geompy.addToStudyInFather(assembly, listOfFaceGroups[k], 'racetrack1Boundary')
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC002: racetrack 2
        k = k+1
        listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[k], geompy.ShapeType['SHELL'], True)
        geompy.UnionList(listOfFaceGroups[k], listOfTemporaryFaceIDs)
        geompy.addToStudyInFather(assembly, listOfFaceGroups[k], 'racetrack2Boundary')
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC003: coil 1
        k = k+1
        listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[k], geompy.ShapeType['SHELL'], True)
        geompy.UnionList(listOfFaceGroups[k], listOfTemporaryFaceIDs)
        geompy.addToStudyInFather(assembly, listOfFaceGroups[k], 'coil1Boundary')
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC004: coil 2
        k = k+1
        listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[k], geompy.ShapeType['SHELL'], True)
        geompy.UnionList(listOfFaceGroups[k], listOfTemporaryFaceIDs)
        geompy.addToStudyInFather(assembly, listOfFaceGroups[k], 'coil2Boundary')
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC005: fixed temperature - 4.5 K (iron)
        k = k+1
        listOfTemporaryFaceIDs = [325]
        for j, v in enumerate(listOfTemporaryFaceIDs):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC006: fixed temperature - 50 K (straps)
        k = k+1
        listOfTemporaryFaceIDs = [662, 566, 482, 578, 530, 626, 518, 614]
        for j, v in enumerate(listOfTemporaryFaceIDs):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC007: heat radiation boundary
        k = k+1
        listOfTemporaryFaceIDs = [320, 330, 232, 266, 259, 293, 357, 384, 429, 410, 387, 462, 472, 467, 200, 434, 439, 28, 444, 426, 405, 477, 217, 448, 453, 140, 458]
        for j, v in enumerate(listOfTemporaryFaceIDs):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])
        # FAC008: air boundary
        k = k+1
        listOfTemporaryFaceIDs_air = [674]
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
        listOfTemporaryEdgeIDs_axis = [682]
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
