import compoundProcessor as cp
import pandas as pd
import collections

file = pd.read_csv('./data/HSE_GGA.csv')


try:
    listOfCompounds = []
    index=0
    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
            listOfCompounds.append(composition)

    counter = collections.Counter(listOfCompounds)
    print(counter)
    for x in counter:
        print(x , ": ",counter[x])

except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

