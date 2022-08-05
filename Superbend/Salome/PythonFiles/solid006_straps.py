# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/26/2019


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Solid
solid006a = geompy.MakeBoxDXDYDZ(coreLegDX+coreLegLength, 2*coreLegDY, coreLegDZ)
solid006a = geompy.MakeTranslation(solid006a, -0.5*(2*coreLegDY+coreLegLength), -0.5*coreLegDY, -0.5*coreLegDZ)
solid006a = geompy.MakeRotation(solid006a, VX, (75/360)*2*math.pi)
solid006a = geompy.MakeRotation(solid006a, VY, (32.5/360)*2*math.pi)
solid006a = geompy.MakeTranslation(solid006a, 0.0, 0.5*coreLegDistance, 0.0)
solid006b = geompy.MakeMirrorByPlane(solid006a, planeVXVY)
solid006c = geompy.MakeCompound([solid006a, solid006b])
solid006c = geompy.MakeMirrorByPlane(solid006c, planeVXVZ)
solid006d = geompy.MakeCompound([solid006a, solid006b, solid006c])
solid006 = geompy.MakeCut(solid006d, tool005a)
solid006 = geompy.MakeCut(solid006, solid005)


# List of geometries #
listForAssembly.append(solid006)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid006, "view006:straps"))


pass
