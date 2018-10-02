import pandas as pd
import numpy as np
import os

firstRun = True
columnTitles = []



data = []
dirname = './cif_merge'


i =0
file = pd.read_csv('HSE_GGA.csv')
fileID = file['ID(Khazana)'].copy()
fileComposition = file['Material composition'].copy

for filename in (os.listdir(dirname)):

    file = dirname+ '/'+filename
    with open(file, "r") as filestream:
        # propertyNames = ['Chemical Composition']
        propertyNames = []
        propertyValues = []

        for line in filestream:
            if line.__contains__("#"):
                line = line.replace("   ", "")
                property = line.split(":")
                propertyName = property[0].replace("#", "").strip()
                propertyValue = property[1].strip()

                # print(propertyName)

                # if propertyName.__contains__('Khazana'):
                #     khazana = int(propertyValue)
                #     print(khazana, type(khazana))
                #
                #     fileID = (fileID[i])
                #     print(fileID, type(fileID))
                #
                #     if khazana == fileID:
                #         chemicalName = fileComposition[i]
                # else:
                propertyNames.append(propertyName)
                propertyValues.append(propertyValue)

        if (firstRun):
            data.append(propertyNames)
            firstRun = False

        # propertyValues.insert(0, chemicalName)
        data.append(propertyValues)


dataframe = pd.DataFrame(data)

print(dataframe.to_string())

dataframe.to_csv("./parsedExport.csv",mode='w', index=False, header=False )

# for i, id in enumerate(file['ID(Khazana)']):
#     print(id)
#
# for i, composition in enumerate(file['Material composition']):
#     print(composition)


