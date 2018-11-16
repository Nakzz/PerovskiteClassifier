from chemspipy import ChemSpider

cs = ChemSpider('GjJ8lV1RhGh97v3N48vyQ7fUDGbAdJ5v')     #change to your key from ChemSpyder

c = cs.get_compound(2157)

print(c.molecular_formula)

filename = 'data\organicCations.csv'
filename_out = 'output\organicCations_named.csv'

# organicCatFile = pd.read_csv(filename)
#
# names = list()
#
#
# for i, compositionOr in enumerate(organicCatFile['Material composition']):
#
#     compoundNames = list()
#
#     for j, result in enumerate(cs.search(compositionOr)):
#
#         compoundName = result.common_name
#         if compoundName != 'PAF': compoundNames.insert(j,compoundName )
#
#     print(organicCatFile.loc[i][0], ": ", compoundNames)
#
#     names.append(compoundNames)
#
#
# for i, name in enumerate(names):
#     for j,x in enumerate(name):
#         # print(name, x)
#         if j == 0: colName = 'Name'
#         else : colName = "Name_" + str(j)
#         if colName not in organicCatFile.columns: organicCatFile[colName] = ""
#         organicCatFile.at[i, colName] = x
#
#
#
# pd.set_option('display.expand_frame_repr', False)
# print(organicCatFile.head())

# organicCatFile.to_csv(filename_out, index=False, encoding='utf-8')
