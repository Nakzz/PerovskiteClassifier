import pandas as pd
import compoundObject as co




import time
start = time.time()

dataset = "Bandgap"   # Stability or Bandgap
# dataset = "Stability"
# dataset = "ORR"

if (dataset ==  "Stability"): file = pd.read_csv('./data/Input.csv')     # Stability Dataset
if (dataset ==  "Bandgap"): file = pd.read_csv('./data/HSE_GGA.csv')     # Bandgap Dataset
if (dataset ==  "ORR"): file = pd.read_csv('./data/perovskite_ORR_V1.csv')     # ORR Dataset

#compute a b x
# use mastmal get atomic radii (ionic? read goldmans tolerance papers)
# use radii to find goldman tolerance
rAeffFile = pd.read_csv('./COM/rAff.csv') 


try:
    atomList = list()
    moleculeComposition = list()
    organicCationsComposition = list()

    # organicAtoms = co.CompoundObject()
    nameOrganic = list()


    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
        # print(type(composition))
        eachCompound = co.CompoundObject(composition)
        moleculeComposition.append(eachCompound)

    # for i, cell in enumerate(rAeffFile['Material composition']):

    for index, row in rAeffFile.iterrows():
        print(row['rMass'], row['rIon'])


except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

data = list()

for  x in moleculeComposition:
    # print("Composition: " ,x.materialComposition, "   Organic CationA:", x.cationA, "   CationB:", x.cationB, "   AnionX:", )
    data.append((x.materialComposition, x.cationA, x.cationB, x.anionX))


df = pd.DataFrame(data)
df.columns = ['Material Composition', 'A site', 'B site', 'OSite']
print(df.head(100))

# outFilename = "./output/perovskiteClassifierOutput_" + dataset + ".csv"
#
# df.to_csv(outFilename, sep=',')

