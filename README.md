
# Digital Advertising Cost-Volume Optimization System - Compilerm

A simple Python application designed to analyze and predict the cost-volume relationship of digital advertising based on the input CSV data & Machine Learning, aiming to optimize budget allocation and enhance ROI. This project is built following the guidelines provided in the Software Development Assignment and integrates multiple tools and techniques learned throughout the course.

1.installing dependencies: pip install -r requirements.txt

2.If you don't have raw data of advertisement, you can use my [data](https://github.com/shin7965977/SRH-berlin-software-engineering/tree/master/data)

3.start the program: python src/__main__.py

## Table of Contents

- [Feature](https://github.com/shin7965977/SRH-berlin-software-engineering#Feature)
- [Prerequisites](https://github.com/shin7965977/SRH-berlin-software-engineering#Prerequisites)
- [SOFTWARE ENGINEERING REQ](https://github.com/shin7965977/SRH-berlin-software-engineering#SOFTWARE-ENGINEERING-REQ)
- [Git Commit History](https://github.com/shin7965977/SRH-berlin-software-engineering#Git-Commit-History)
- [Project Management Tool](https://github.com/shin7965977/SRH-berlin-software-engineering#Project-Management-Tool)
- [Build Tool](https://github.com/shin7965977/SRH-berlin-software-engineering#Build-Tool)
- [UML Diagrams](https://github.com/shin7965977/SRH-berlin-software-engineering#UML-Diagrams)
- [Unit Tests](https://github.com/shin7965977/SRH-berlin-software-engineering#Unit-Tests)
- [Clean Code](https://github.com/shin7965977/SRH-berlin-software-engineering#Clean-Code)


## Feature

- #### CSV Upload and Reading: 
Enter the path to your CSV file to load data.

- #### Cost-Volume exploration& visualization : 
Visualize relationships between ROI, costs, and Buy.

- #### Cost-Volume Optimization Model(MAB): 
We can use Multi-Armed Bandit (MAB) strategies for advertising budget allocation by analyzing past performance reports, thereby achieving maximization of ROI or BUY.

- #### hypothesis testing: 
Hypothesis testing can be used to determine whether the effectiveness of digital advertising has grown due to the implementation of machine learning.
## Prerequisites

#### Python == 3.12
#### Required libraries:

- matplotlib
- numpy
- pandas
- scikit-learn
- scipy
- seaborn
- statsmodels


## SOFTWARE ENGINEERING REQ
- #### Compilerm must be able to upload CSV files.
- #### Compilerm must visualize the data in the CSV files into line graphs, box plots, and scatter plots.
- #### Compilerm must be capable of executing three machine learning methods: Thompson Sampling, epsilon-greedy, and Upper Confidence Bound (UCB).
- #### Compilerm must be able to perform hypothesis testing. 

## Git Commit History
- [Git Commit History](https://github.com/shin7965977/SRH-berlin-software-engineering/commits/master/)

## Project Management Tool
- [Project Management Tool](https://github.com/shin7965977/SRH-berlin-software-engineering/tree/master/Requirements%20Engineering)

## Build Tool
- [Build Tool](https://github.com/shin7965977/SRH-berlin-software-engineering/tree/master/.github/workflows)
- [![Lint Code Base and Run Tests](https://github.com/shin7965977/Compilerm/actions/workflows/Lint%20Code%20Base.yml/badge.svg)](https://github.com/shin7965977/Compilerm/actions/workflows/Lint%20Code%20Base.yml)
## IDE

#### Visual Studio Code
Ctrl + P:
Function: Quickly open files.

Ctrl + /:
Function: Comment or uncomment the current line or selected lines of code.

Ctrl + H:
Function: Perform a global search and replace across the entire workspace.

F2:
Function: Rename variables or functions.

Ctrl + `:
Function: Open or close the integrated terminal.

## UML Diagrams
- [UML Diagrams](https://github.com/shin7965977/SRH-berlin-software-engineering/tree/master/UML)

## Unit Tests
- [Unit Tests](https://github.com/shin7965977/SRH-berlin-software-engineering/blob/master/src/test_unittest.py)

## Clean Code
- [Clean Code](https://github.com/shin7965977/SRH-berlin-software-engineering/blob/master/Clean%20Code%20Development%20-%20Cheatsheet.pdf)
