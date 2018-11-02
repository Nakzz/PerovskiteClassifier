# PerovskiteClassifier

Scripts to identify and parse Organic cation A, cation X and anion B from a dataset of 1,346 HOIPs, which features 16 organic cations, 3 group-IV cations and 4 halide anions.

## Getting Started

Scripts


#### Prerequisite Packages

pip install pandas
pip install numpy 
pip install ChemSpider


## Scripts

### compoundName.py
Finds name for compound based on their chemical formual from a CSV file using ChemSpyder api.

filename = 'data\organicCations.csv'
filename_out = 'output\organicCations_named.csv'

### perovskite.py {developing}
Identify Organic cation A, cation X and anion B from the dataset.
Can pick from two datasets available. 
     dataset = "Bandgap"  
     dataset = "Stability"
 
 Currently developing with Bandgap dataset.
 

### propertiesParse.py
Parses atom properties from every CIF file in a folder and exports them into a CSV file.

dirname = './cif_merge'


### compoundProcessor.py
Helper class for perovskite.py that can -
  - Finds available molecules
  - Add same atoms for a composition to an array
  - Returns an array of unique Atoms in an composition (sorted)
  - Returns an array containing molecule composition


## Running the scripts
The scrips contain no arguments. So just run them in comandline. 


## Authors

* **Ajmain Naqib** - *Initial work* - (https://github.com/nakzz)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
