# pdtug
Unweighted graphs from pandas numerical dataframes

## Getting Started
#### Dependencies
You need Python 3.5 or later to use **pdtug**. You can find it at [python.org](https://www.python.org/).

You aso need pandas and numpy packages, which is available from [PyPI](https://pypi.org). If you have pip, just run:
```
pip install pandas
```
```
pip install numpy
```
#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/caiocarneloz/pdtug.git
```

## Features
- Get a unweighted graph from a pandas dataframe
  - ~~Choose from multiple distance functions~~
  - ~~Choose between k-nearest neighbours and distance threshold~~


## Usage
The **pdtug** function takes as argument a dataframe containing numerical data and an integer _k_ value which represents the number of nearest neighbours. As example, the image below shows the relationship between nodes with _k_ = 2:

![alt text](https://i.imgur.com/fnHbRGy.gif)
