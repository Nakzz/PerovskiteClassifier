# PerovskiteClassifier

Scripts to identify and parse Organic cation A, cation X and anion B from a dataset of 1,346 HOIPs, which features 16 organic cations, 3 group-IV cations and 4 halide anions.

# Getting Started
## Prerequisite Packages
```sh
pip install pandas
pip install numpy 
```

### Running the scripts
The scrips contain no arguments. So just run the following in comandline. 
```sh
python perovskiteClassifier.py
```


## Scripts

### perovskiteClassifier.py
Can pick from two datasets available. 
     dataset = "Bandgap"  
     dataset = "Stability"
Create object using compoundObject.py and outputs object information to a CSV file using pandas


### compoundObject.py
Identifies Organic cation A, cation X, anion B and other propersites from chemical composition.


## Note
 Currently only works with Bandgap dataset.


## Authors

* **Ajmain Naqib** - *Initial work* - (https://github.com/nakzz)

