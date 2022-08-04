# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/26/2019


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Volume
solid003_1 = geompy.MakeCylinderRH(coilInnerRadius, coilThickness)
solid003_2 = geompy.MakeCylinderRH(coilInnerRadius+coilWidth, coilThickness)
solid003 = geompy.MakeCut(solid003_2, solid003_1)
solid003 = geompy.MakeTranslation(solid003, 0., 0., (0.5*gap+racetrackThickness-coilThickness))

# List of geometries
listOfSolid003 = [solid003]

listForAssembly.append(solid003)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid003, "view003:coil_1"))

pass
