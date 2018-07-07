
import pandas as pd
import compoundProcessor as cp
from chemspipy import ChemSpider

cs = ChemSpider('f84b99d9-9735-4047-b7e5-10273f7a08aa')


filename = 'organicCations.csv'
filename_out = 'organicCations_named.csv'

organicCatFile = pd.read_csv(filename)

names = list()


for i, compositionOr in enumerate(organicCatFile['Material composition']):

    compoundNames = list()

    for j, result in enumerate(cs.search(compositionOr)):

        compoundName = result.common_name
        if compoundName != 'PAF': compoundNames.insert(j,compoundName )

    print(organicCatFile.loc[i][0], ": ", compoundNames)

    names.append(compoundNames)


for i, name in enumerate(names):
    for j,x in enumerate(name):
        # print(name, x)
        if j == 0: colName = 'Name'
        else : colName = "Name_" + str(j)
        if colName not in organicCatFile.columns: organicCatFile[colName] = ""
        organicCatFile.at[i, colName] = x



pd.set_option('display.expand_frame_repr', False)
print(organicCatFile.head())

organicCatFile.to_csv(filename_out, index=False, encoding='utf-8')
