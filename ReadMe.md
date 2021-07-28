# dockME LiTe - Simplified tool for Robust Researchers
[![DOI](https://zenodo.org/badge/390092382.svg)](https://zenodo.org/badge/latestdoi/390092382)

dockME Lite is a Python-based biotech software for dealing with multiple autodock macromolecules and ligands files to be used at Autodock systems.


### CITE THIS SOFTWARE

COSTA, R.B.G.M., & Xavier-Júnior, F.H. (2020, May 25). dockME LITE: An  Automated Open-Source Solution for Molecular Docking Scientists (Version v1.0.5-alpha). Zenodo. http://doi.org/10.5281/zenodo.5140346


## Installation

#### On Windows:

Using [Autodock VINA](http://vina.scripps.edu/):

1- Copy the entire folder content to the same path of where Autodock Vina has been installed/extracted (or just bring VINA executable files to the same path)

2- copy 'dockme-lite.exe' from the 'dist' directory bringing to the root directory

3- RUN 'dockme-lite.exe'.


#### On LINUX:

1-Copy the entire folder content to the same path of where Autodock Vina has been installed/extracted (or just bring VINA executable files to the same path).

( NOTE:You must install Python 3.8 or later in order to run this package.)

Having VINA at the same directory, just run:

```bash
python dockme-lite.py
```

## Usage

####  BEFORE USING

Before start to use this program, we strongly recommend to organise all your macromolecules and ligands in the following way:

Create two spreadsheet somewhere (or just a simple table/chart using pen and paper) - one for ligands, and other for macromolecules - listing all your .pdbqt files ordered in a sequence starting from zero. 

##### Why? 
This will help you to don't get lost if there is any corrupted data along the process due to any error caused during the running program.

E.G.

MACROMOLECULES:

0 - Protein 1

1 - Protein 2

2 - Protein 3

... and so on

###### After organise the table, rename the files to the corresponding number in your table. For example, Protein 1 should be renamed to 0.pdbqt, and should be sent to the '/macromolecules' directory.

###### The following STEP is to organise all the config files at the root folder. You may find the 'standard.txt' file useful to do so! You just have to put all the grid parameters known from your pre-docking working and rename it as 'macromoleculenumber_ligandnumber.txt' file.
###### E.G.: Suppose that our macromolecule order in our organised chart is '3' and the ligand is at the 2nd position (which means '1', because we start from zero), then, our parameter file should be named as 3_1.txt . That's it. No rocket science in here! :D


#### USING THE SOFTWARE

There are two (2) simple options. The first one makes interactions with all the macromolecules and ligands, while the second one is indicated to make single interactions between a specified ligand and a specified macromolecule.

Therefore, in order to do this, you should previously have created the configuration files to run this code.

#### THE NEXT INFORMATION IS VERY IMPORTANT!! 

FILES MUST BE NAMED BY THE FOLLOWING ORDER:
macromolecule_ligand.txt (e.g. Let's say that you have organised your table of ligands and your macromolecule number in this list is the 3rd one, while the second one, related to the ligand list, is the 1st one, then, the file should be named as:  "3_1.txt").


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache](http://www.apache.org/licenses/LICENSE-2.0.txt)
