import pandas as pd
import numpy as np
import os

firstRun = True
columnTitles = []




dirname = './cif_merge'
organicDirname = './cif_merge_organic'

i =0

for filename in (os.listdir(dirname)):

    file = dirname+ '/'+filename
    organicOnlyFilename = organicDirname + '/'+filename

    organicOnlyFile = open(organicOnlyFilename, 'w');





    with open(file, "r") as filestream:
        data = []



        # propertyNames = ['Chemical Composition']
        propertyNames = []
        propertyValues = []

        for line in filestream:

            if (line[0].__contains__("C") and  not line[1].__contains__("l"))or line[0].__contains__("H") or line[0].__contains__("_") or line[0].__contains__("l") or line[0].__contains__("d") or line[0].__contains__("_") or line[0].__contains__("N"):
                # print(line)
                # data.append(line)
                organicOnlyFile.write(line)

        organicOnlyFile.close()
        # print(data)

