# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/26/2019


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Solid
solid005a_1 = geompy.MakeBoxDXDYDZ(coreDX, coreDY, coreDZ)
solid005a_1 = geompy.MakeTranslation(solid005a_1, -0.5*coreDX, -0.5*coreDY, -0.5*coreDZ)

# chamfering
solid005a_2 = geompy.MakeChamferEdge(solid005a_1, chamfer_D1, chamfer_D2, 33, 13)
solid005a_3 = geompy.MakeChamferEdge(solid005a_2, chamfer_D1, chamfer_D2, 37, 40)
solid005a_4 = geompy.MakeChamferEdge(solid005a_3, chamfer_D1, chamfer_D2, 17, 29)
solid005a = geompy.MakeChamferEdge(solid005a_4, chamfer_D1, chamfer_D2, 36, 46)

solid005a = geompy.MakeCut(solid005a, tool005a)

solid005b_1 = geompy.MakeCylinderRH(coilInnerRadius, racetrackThickness)
solid005b_1 = geompy.MakeTranslation(solid005b_1, 0., 0., 0.5*gap)
solid005b_2 = geompy.MakeMirrorByPlane(solid005b_1, planeVXVY)
solid005b = geompy.MakeCompound([solid005b_1, solid005b_2])
solid005b = geompy.MakeCut(solid005b, geompy.MakeCompound([solid001, solid002]))

solid005c_1 = geompy.MakeCylinderRH(coreCoilRadius, coilThickness)
solid005c_1 = geompy.MakeCut(solid005c_1, tool005b)
solid005c_1 = geompy.MakeTranslation(solid005c_1, 0., 0., 0.5*gap+racetrackThickness-coilThickness)
solid005c_2 = geompy.MakeMirrorByPlane(solid005c_1, planeVXVY)
solid005c = geompy.MakeCompound([solid005c_1, solid005c_2])

solid005 = geompy.MakeCompound([solid005a, solid005b, solid005c])

# List of geometries
listForAssembly.append(solid005)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid005, "view005:core"))

pass
