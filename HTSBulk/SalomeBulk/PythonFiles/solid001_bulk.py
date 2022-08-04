# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 01/02/2022
# Units: SI otherwise indicated


# Printing id number and corresponding geometry:
print(listOfSolidNumbers[0]+': '+listOfSolids[0])

# Volume #
solid001 = geompy.MakeCylinderRH(bulk1Radius, bulk1Height)
solid001 = geompy.MakeTranslation(solid001, 0., 0., -0.5*bulk1Height)

# List of geometries #
listOfSolid001 = [solid001]
listForAssembly.append(solid001)

# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid001, 'view001:bulk'))


pass
