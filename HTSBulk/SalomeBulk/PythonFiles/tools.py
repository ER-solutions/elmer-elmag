# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english):  05/12/2021
# Units: SI otherwise indicated


# Grouping tools #
#listOfTools = []
#tools = geompy.MakeCompound(listOfTools)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(tools, 'viewTool'))


pass
