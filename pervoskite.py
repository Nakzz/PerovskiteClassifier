from typing import List, Any

import pandas as pd
import compoundProcessor as cp
from chemspipy import ChemSpider
import csv

cs = ChemSpider('f84b99d9-9735-4047-b7e5-10273f7a08aa')

import time
start = time.time()

dataset = "Bandgap"   # Stability or Bandgap
# dataset = "Stability"

if (dataset ==  "Stability"): file = pd.read_csv('./data/Input.csv')     # Stability Dataset
if (dataset ==  "Bandgap"): file = pd.read_csv('./data/HSE_GGA.csv')     # Bandgap Dataset

organicCatFile = pd.read_csv('./data/organicCations_named.csv')

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
        nameOrganic.insert(i, compositionName)

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



for index, elementComposition in enumerate(searchCompound[0::]):
    organic = 0

    for elements in elementComposition:             #elements: ['C', 4]
        if elements[0] in atomOrganic:
            organic = organic + 1
        else:
            continue

    if (organic < 2):
        elementComposition.append("Non-Organic")

    else:
        # print("elementComposition: ", elementComposition, "len: ", len(elementComposition))
        dontSearch = list()
        possibleOrganic = list()

        for elements in elementComposition:  # elements: ['C', 4]
            # print(" elements: ", elements, "len: ", len(elements))
            organicSearchCounter = 0
            currElem = elements[0]
            currElemNum = elements[1]

            for orgElementsWName in searchOrganicWName[0::]:
                # print("       orgElementsWName: ", orgElementsWName, "len: ", len(orgElementsWName))

                organicCompoundName = orgElementsWName[1]

                for orgElements in orgElementsWName[0]:
                    #print("         orgElements: ", orgElements, "len: ", len(orgElementsWName))
                    if (organicCompoundName not in dontSearch):
                        organicElem = orgElements[0]
                        organicElemNum = orgElements[1]

                        # print("            currElem: ", currElem, "    currElemNum: ", currElemNum)
                        # print("         organicElem: ", organicElem, " organicElemNum: ", organicElemNum, " organicCompoundName: ", organicCompoundName)

                        if (currElem != organicElem): continue
                        else:
                            numDifference = (currElemNum - organicElemNum)
                            if numDifference < 0:
                                # print("          !!!", currElem, "[", currElemNum, "] -", organicElem, "[",
                                #       organicElemNum, "] =", numDifference)
                                dontSearch.append(organicCompoundName)
                                continue

                            else:
                                print("             ",currElem,"[" , currElemNum,"] -" ,organicElem ,"[" , organicElemNum,"] =" ,numDifference)


        possibleOrganic = [item for item in  nameOrganic[0:len(nameOrganic)] if item not in dontSearch]
        elementComposition.append(possibleOrganic)

#Print The searches for organic and inorganic results.

# for x in elementComposition: print(x)

logFileName = str("./output/log" +dataset+ ".txt")
fh = open(logFileName,"w")

for id, content in enumerate(searchCompound[0::], start=0):
    print("searchCompound {}: {}".format(id, content))
    fh.write("searchCompound {}, {}".format(id, content))
    # for x in content:
    #     print(id, ", ", x )
fh.close()


end = time.time()
print("Completion time: ",end - start)


# find the biggest cation in every search
# OPTION 2 check the database where the data was bing parsed: Cif files from datadryad.org
# poster info: talk about coding related project and talk about specific lession
# learning more about perofskite specific
# talk about stucture. talk about hwo they are tradetionally, now how we are placing organic molecules in different sites, preserving their stuff.
# talk more about descriptor parsing  from databases