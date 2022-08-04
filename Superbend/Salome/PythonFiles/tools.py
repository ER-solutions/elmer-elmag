# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english):  12/07/2012
# Units: SI otherwise indicated


# Tool005: (magnetic core)
tool005a = geompy.MakeBoxDXDYDZ(coreInnerHoleDX, coreInnerHoleDY, coreInnerHoleDZ)
tool005a = geompy.MakeTranslation(tool005a, -0.5*coreInnerHoleDX, -0.5*coreInnerHoleDY, -0.5*coreInnerHoleDZ)
tool005b = geompy.MakeCylinderRH(coilInnerRadius+coilWidth, coilThickness)


# Grouping tools #
listOfTools = [tool005a, tool005b]
tools = geompy.MakeCompound(listOfTools)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(tools, "viewTool"))


pass
