# pdtug
Unweighted graphs from pandas numerical dataframes

## Getting Started
#### Dependencies
You need Python 3.7 or later to use **pdtug**. You can find it at [python.org](https://www.python.org/).

You also need pandas and numpy packages, which is available from [PyPI](https://pypi.org). If you have pip, just run:
```
pip install pandas
pip install numpy
```
#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/caiocarneloz/pdtug.git
```

## Features
- Get a unweighted graph from a pandas dataframe
  - ~~Choose from multiple distance functions~~(soon)
  - ~~Choose between k-nearest neighbours and distance threshold~~(soon)


## Usage
The **pdtug** function takes as argument a dataframe containing numerical data and an integer _k_ value which represents the number of nearest neighbours to be considered on the edge creation. As example, the image below shows the relationship between nodes with _k_ = 2:

![alt text](https://i.imgur.com/fnHbRGy.gif)

As output, the function returns a python dictionary with the format of an adjacency list:
```
{0: [8, 3, 4, 7],
 1: [8, 6, 7],
 2: [8, 9, 5, 6],
 3: [0, 8, 4],
 4: [8, 0, 3],
 5: [8, 9, 2],
 6: [1, 2, 7],
 7: [0, 1, 6],
 8: [0, 1, 2, 3, 4, 5, 9],
 9: [8, 2, 5]}
```
Each value corresponds to the dataframe row index.
