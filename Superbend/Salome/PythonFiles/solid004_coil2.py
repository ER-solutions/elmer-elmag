# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/26/2019


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Volume
solid004_1 = geompy.MakeCylinderRH(coilInnerRadius, coilThickness)
solid004_2 = geompy.MakeCylinderRH(coilInnerRadius+coilWidth, coilThickness)
solid004 = geompy.MakeCut(solid004_2, solid004_1)
solid004 = geompy.MakeTranslation(solid004, 0., 0., -(0.5*gap+racetrackThickness))


# List of geometries
listOfSolid004 = [solid004]

listForAssembly.append(solid004)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid004, "view004:coil_4"))


pass
