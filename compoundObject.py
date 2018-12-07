import re
import json

class CompoundObject:

    ##parse from descriptors JSON
    with open('./data/descriptors.json') as json_data_file:
        descriptorsData = json.load(json_data_file)

    allAnionsX = descriptorsData["anionX"]
    allCationsB = descriptorsData["cationB"]
    allOrganicCationsA = descriptorsData["organicCations"]

    materialComposition = ""
    anionX = ""
    cationB = ""
    anionX = ""
    cationA = ""
    # organic = False                 #TODO: add classifier for organic
    composition = []



    def __init__(self, ChemicalFormula):
        self.materialComposition = ChemicalFormula
        self.composition = self.getComposition(ChemicalFormula)



        self.indentifyOrganicCation(self.composition)

        # for x in self.allAnionsX:
        #     print(x)

        print(self.cationA)




        # Identifies CationB and AnionX
    def indentifyClassifiers(self, atomName):
        # print(atomName)

        ## identify catB
        for catB in self.allCationsB:
            if catB == atomName:
                # print(catB, ": ", type(catB))
                self.cationB = self.cationB + catB

        ## identify anionX
        for anX in self.allAnionsX:
            if anX == atomName:
                # print(anX, ": ", type(anX))
                self.anionX = self.anionX + anX



    # Identifies CationA
    def indentifyOrganicCation(self, composition):

        cationA = composition.copy()

        # remove catB from composition
        for atom in cationA:
            # print(atom)
            if (atom[0] == self.cationB.replace(" ", "")):
                # print("removing: ", atom[0])
                self.cationB = self.cationB + str(atom[1])
                cationA.remove(atom)

        for atom in cationA:
            # print(atom[0])
            if (atom[0] == self.anionX.replace(" ", "")):
                # print("removing: ", atom[0])
                self.anionX = self.anionX + str(atom[1])
                cationA.remove(atom)

        for x in cationA:
            # print(x)
            for i in x:
                self.cationA += str(i)
        # ## identify catA
        # for catA in self.allOrganicCationsA:
        #     print(catA, ": ", type(catA))




    # Returns an array of contaiting molecules
    # also identifies classifiers

    def findMolecules(self):
        self.molecules = re.findall('[A-Z][^A-Z]*', self.compound)

    # Returns an array containting molecule composition
    def findMoleculesComposition(self, molecule):
        # print(molecule)

        smallLetter = "".join(re.findall('[a-z]', molecule))
        if smallLetter == "":
            atom = [molecule[0], molecule[1:]]
            # atom[1] = int(atom[1])
            # print(atom)
            self.indentifyClassifiers(atom[0])
            if atom[1] == '':
                atom[1] = 1
            else:
                atom[1] = int(atom[1])
        else:
            moleculeSTR = "".join(molecule)
            indexAtom = moleculeSTR.index(smallLetter)
            atomName = molecule[0:indexAtom + 1]

            self.indentifyClassifiers(atomName)
            try:
                atomNumber = int(molecule[(indexAtom + 1):])
                atom = [atomName, atomNumber]
            except ValueError:
                #print("Value Error. Info: ",moleculeSTR )
                atom = [atomName, 1]
                return atom



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


