from typing import List, Any

import pandas as pd
import re
from chemspipy import ChemSpider

cs = ChemSpider('f84b99d9-9735-4047-b7e5-10273f7a08aa')


class CompoundProcessor:

    # Returns an array of contaiting molecules
    def findMolecules(self):
        self.molecules = re.findall('[A-Z][^A-Z]*', self.compound)

    # Returns an array containting molecule composition
    def findMoleculesComposition(self, molecule):
        smallLetter = "".join(re.findall('[a-z]', molecule))
        if smallLetter == "":
            atom = [molecule[0], molecule[1:]]
            # atom[1] = int(atom[1])
            # print(atom)
            if atom[1] == '':
                atom[1] = 1
            else:
                atom[1] = int(atom[1])
        else:
            moleculeSTR = "".join(molecule)
            indexAtom = moleculeSTR.index(smallLetter)
            atom = [molecule[0:indexAtom + 1], int(molecule[indexAtom + 1:])]

        return atom

    # Adds number of same atoms
    def addSameAtoms(self, atoms):
        leftSearch = (len(atoms)) - 1
        currentSearch = 0;
        duplicates = list()
        alreadyFound = list()

        for i in range(0, len(atoms) - 1):
            # remaining = len(atoms) - i
            for j in range(i + 1, len(atoms)):

                currentAtom = atoms[i][0]
                searchingAtom = atoms[j][0]

                if currentAtom == searchingAtom and j not in alreadyFound:
                    # print("Found Duplicate: ", atoms[i], 'and ', atoms[j] )
                    duplicates += [[i] + [j]]
                    alreadyFound += [j]

        # print("Duplicate atom : ", duplicates)
        sortByIndex = lambda duplicate: duplicate[1]

        duplicates.sort(key=sortByIndex, reverse=True)

        # print("Sorted duplicates atom : ", duplicates)

        for duplicate in duplicates:
            firstAtomIndex = duplicate[0]
            duplicateAtomIndex = duplicate[1]
            # print(atoms[firstAtomIndex], ': ', atoms[duplicateAtomIndex])
            atoms[firstAtomIndex][1] = int(atoms[firstAtomIndex][1]) + int(atoms[duplicateAtomIndex][1])
            # print("Deleting index: ", atoms[duplicateAtomIndex])
            del atoms[duplicateAtomIndex]

        # print(atoms)
        return atoms

    # Getters returning a list of Molecules composition
    def getComposition(self, compound):
        self.compound = compound
        self.findMolecules()
        atoms = list()

        for molecule in self.molecules:
            atoms.append(self.findMoleculesComposition(molecule))

        return self.addSameAtoms(atoms);

    def getAtomList(self, moleculeComp):
        alreadyFound = list()

        for p in moleculeComp:
            for i in range(0, len(p)):
                atomSymbol = (p[i][0])

                if atomSymbol in alreadyFound:
                    # print("Already found: ", atomSymbol)
                    # print(atomSymbol, type(atomSymbol))
                    continue
                else:
                    # print("adding: ", atomSymbol)
                    alreadyFound += [atomSymbol]

        alreadyFound.sort()

        return alreadyFound


file = pd.read_csv('Input.csv')
organicCatFile = pd.read_csv('organicCations.csv')

try:
    atomList = list()
    moleculeComposition = list()
    organicCationsComposition = list()
    eachCompound = CompoundProcessor()
    organicAtoms = CompoundProcessor()

    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
        moleculeComposition.append(eachCompound.getComposition(composition))

    for i, compositionOr in enumerate(organicCatFile['Material composition']):
        organicCationsComposition.append(organicAtoms.getComposition(compositionOr))

    atomInput = eachCompound.getAtomList(moleculeComposition)
    atomOrganic = organicAtoms.getAtomList(organicCationsComposition)


except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

print('Input Compound Composition[0]', moleculeComposition[0])
print('Input Compound Composition[1]', moleculeComposition[1])
print('Organic (molecular) cations Composition: ', organicCationsComposition[0])
print('organic (molecular) cations Composition[1]', organicCationsComposition[1])

for x in organicCationsComposition: print(x)


print('All Input atoms: ', atomInput)
print('All Organic atoms: ', atomOrganic)

searchCompound = moleculeComposition.copy()
searchOrganic = organicCationsComposition.copy()
organicFound = 0

for elementComposition in searchCompound[0::]:
    searchAtomNum = 0
    organic = False
    for elements in elementComposition:             #elements: ['C', 4]
        for x in atomOrganic:
            if elements[0] == x:
                organic = True

                searchAtomNum += elements[1]
                #print("Adding: ", elements[1], "SearchAtomNum: ", searchAtomNum)

                keepSearching = True
                possible = ""
                for orgElements in searchOrganic:           # orgElements: [['C', 1], ['N', 3], ['H', 6]]
                    orgAtomNum = 0
                    orgElementsCounter = 0
                    print("orgElements: ", orgElements, "len: ", len(orgElements))

                    if(keepSearching):
                        for orgAtom in orgElements:         # orgAtom: ['C', 1]
                            orgAtomName = orgAtom[0]
                            orgAtomNum += orgAtom[1]


                            # print("orgAtomName: ", orgAtomName);
                            # print("Checking: ", elements[0], "=", orgAtomName);
                            if elements[0] == orgAtomName:
                                # print("Match found: ", elementComposition, "= ", orgElements);
                                remaining = elements[1] - orgAtomNum

                                if(remaining > -1):
                                    keepSearching = True
                                else:
                                    keepSearching = False
                                    print(elements[0], ":", remaining)

                            orgElementsCounter = 1 + orgElementsCounter
                            print("Counter: ", orgElementsCounter)

                            if(orgElementsCounter == len(orgElements)):
                                print("Last cation atom search for: ", orgElements)

                                if(keepSearching):
                                    possible = ["Possible Organic Cation:" + str(orgElements)]
                                    elementComposition.append(possible)





    if organic!= True:
        # print(elementComposition, "is not organic")
        elementComposition.append("Non-Organic")

# for x in searchCompound: print(x)
fh = open("log.txt","w")



for num, name in enumerate(searchCompound[0::], start=0):
    print("searchCompound {}: {}".format(num, name))
    fh.write("searchCompound {}: {}".format(num, name))

fh.close()