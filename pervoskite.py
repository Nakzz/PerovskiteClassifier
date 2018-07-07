from typing import List, Any

import pandas as pd
import compoundProcessor as cp
from chemspipy import ChemSpider

cs = ChemSpider('f84b99d9-9735-4047-b7e5-10273f7a08aa')

import time
start = time.time()

dataset = "Bandgap"   # Stability or Bandgap

if (dataset ==  "Stability"): file = pd.read_csv('Input.csv')     # Stability Dataset
if (dataset ==  "Bandgap"): file = pd.read_csv('HSE_GGA.csv')     # Bandgap Dataset

organicCatFile = pd.read_csv('organicCations_named.csv')

try:
    atomList = list()
    moleculeComposition = list()
    organicCationsComposition = list()
    eachCompound = cp.CompoundProcessor()
    organicAtoms = cp.CompoundProcessor()
    nameOrganic = list()


    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
        moleculeComposition.append(eachCompound.getComposition(composition))

    for i, compositionOr in enumerate(organicCatFile['Material composition']):
        organicCationsComposition.append(organicAtoms.getComposition(compositionOr))

    for i, compositionName in enumerate(organicCatFile['Name']):
        # print(compositionName)
        nameOrganic.insert(i, [compositionName])

    atomInput = eachCompound.getAtomList(moleculeComposition)
    atomOrganic = organicAtoms.getAtomList(organicCationsComposition)


except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

# print('Input Compound Composition[0]', moleculeComposition[0])
# print('Input Compound Composition[1]', moleculeComposition[1])
# print('Organic (molecular) cations Composition: ', organicCationsComposition[0])
# print('organic (molecular) cations Composition[1]', organicCationsComposition[1])
# print('All Input atoms: ', atomInput)
# print('All Organic atoms: ', atomOrganic)

searchCompound = moleculeComposition.copy()
searchOrganic = organicCationsComposition.copy()


searchOrganicWName = [[0 * j for j in range(2)] for i in range(len(searchOrganic))]

for i, x in enumerate(searchOrganic):
    searchOrganicWName[i][0] = x
    searchOrganicWName[i][1] = nameOrganic[i]

#     print(x ,": ",nameOrganic[i])
#
#
#
# print('organic (molecular) cations Composition')
# for x in searchOrganicWName: print(x)


organicFound = 0



for index, elementComposition in enumerate(searchCompound[50:51]):



    organicFoundName = list()
    organic = 0
    orgElementsCounter = 0
    elementCounter =0

    for elements in elementComposition:             #elements: ['C', 4]
        if elements[0] in atomOrganic:
            organic = True
        else:
            continue

    if (organic):
        print("elementComposition: ", elementComposition, "len: ", len(elementComposition))

        if elements[0] in atomOrganic:
            organic = True

            keepSearching = True
            possible = ""

        #     for orElements in searchOrganicWName[0:1]:
        #
        #         for orgElements in orElements: # orgElements: [['C', 1], ['N', 3], ['H', 6]]
        #
        #             orgAtomNum = 0
        #
        #             if(keepSearching):
        #                 for orgAtom in orgElements:         # orgAtom: ['C', 1]
        #
        #
        #                     if len(orgElements)>1:
        #                         print("orgElements: ", orgElements, "len: ", len(orgElements))
        #                         print("orgAtom: ", orgAtom, "len: ", len(orgAtom))
        #
        #                         orgAtomName = orgAtom[0]
        #                         orgAtomNum = orgAtom[1]
        #
        #                         # print("orgAtomName: ", orgAtomName);
        #                         # print("Checking: ", elements[0], type(elements[0]), "=", orgAtomName, type(orgAtomName));
        #                         # print("orgAtomNum: ", orgAtomNum)
        #                         if elements[0] == orgAtomName:
        #                             print("Match found: ", elementComposition, "= ", orgElements);
        #                             remaining = elements[1] - orgAtomNum
        #                             print("remaining: ", elements[1], "-", orgAtomNum, "= ", remaining)
        #
        #                             if (remaining > -1):
        #                                 keepSearching = True
        #                             else:
        #                                 keepSearching = False
        #                                 print(elements[0], ":", remaining)
        #
        #     orgElementsCounter = 1 + orgElementsCounter
        #
        #     print("Counter: ", orgElementsCounter)
        #
        #     sizeOfOrgElements = len(orgElements)
        #     sizeOfelementComposition = len(elementComposition)
        #
        #     if (orgElementsCounter == sizeOfOrgElements and elementCounter == sizeOfelementComposition):
        #         print(index, ": Last cation atom search for: ", orgElements)
        #
        #         if (keepSearching and (str(orElements[1]) not in organicFoundName)):
        #             print("Possible Organic Cation: ",str(orElements[1]) ,"in ", elementComposition )
        #             possible = (orElements[1])
        #             organicFoundName.append(possible)
        #
        # elementCounter = 1 + elementCounter






    elementComposition.append(organicFoundName)




    if organic!= True:
        # print(elementComposition, "is not organic")
        elementComposition.append("Non-Organic")


#Print The searches for organic and inorganic results.

for x in elementComposition: print(x)

# logFileName = str("log" +dataset+ ".txt")
# fh = open(logFileName,"w")
#
# for num, name in enumerate(searchCompound[0::], start=0):
#     print("searchCompound {}: {}".format(num, name))
#     fh.write("searchCompound {}: {}".format(num, name))
#
# fh.close()


end = time.time()
print("Completion time: ",end - start)