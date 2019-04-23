import pandas as pd
import math
import re

df = pd.read_csv('./HSE_GGA.csv')

chartStateRadii = {
    "Ge":	0.73,
"Sn":	1.18,
"Pb":	1.19,
"F"	:1.285,
"Cl":	1.81,
"Br":	1.96,
"I":	2.2,
}

def atomOnly(atomName):
    return " ".join(re.findall("[a-zA-Z]+", atomName))


df1= pd.DataFrame(columns=['ToleranceFactor'])

for index, row in df.iterrows():
    # print(row['CationA'], row['CationB'], row["Anion X"], row["rMass"], row["rIon"])

    catA = atomOnly(row['CationA'])
    catB = atomOnly(row['CationB'])
    anX = atomOnly(row["Anion X"])
    rMass = row["rMass"]
    rIonName = atomOnly(row["rIon"])

    #TODO: compute rION from rIonName. what would these be?
    # print(rIonName)
    rIon =0;

    #compute for rA_Eff
    rA_Eff = float(rMass) + float(rIon)

    #TODO: compute for rX_eff from anX
    rX_eff = chartStateRadii.get(anX);

    # print(anX, rX_eff)

    #TODO: compute for rB
    rB = chartStateRadii.get(catB);

    if(rB <= 0):
        print("Error: rB is not found")

    if (rX_eff <= 0):
        print("Error: rX_eff is not found")

    if (rIon <= 0):
        print("Error: rIon is not found")


    tf = (rA_Eff + rX_eff)/ (math.sqrt(2) *( rB + (.5*rX_eff)) )

    df1.loc[index] = [tf]

    # print(tf)


# print(df1)

# df1.to_csv("./tf.csv", sep=',')
