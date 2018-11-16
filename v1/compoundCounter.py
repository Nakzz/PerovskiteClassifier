import pandas as pd
import collections

file = pd.read_csv('./data/HSE_GGA.csv')


try:
    listOfCompounds = []
    index=0
    totalNumberofCompound =0
    numberofCompounds =0
    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
            listOfCompounds.append(composition)

    counter = collections.Counter(listOfCompounds)
    print(counter)
    for x in counter:
        print(x , ": ",counter[x])
        index =index +1;

    totalNumberofCompound = sum(counter.values())
    # numberofCompounds = (counter.keys()).__sizeof__()

    print("Number of different compounds: ", index)
    print("Total number of compounds: ", totalNumberofCompound)
except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

