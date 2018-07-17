# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Instructions](README.md#instructions)
4. [Approach](README.md#approach)
5. [Run Instructions](README.md#run-instructions)


# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

Disclosure: The projects that Insight Data Engineering Fellows work on during the program are much more complicated and interesting than this coding challenge. This challenge only tests you on the basics. 

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Output 

Your program needs to create the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file should contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers


# Approach
1. Create a modular called DrugCounter with two keyword arguments: 1.the file path for reading and 2.the file path for writing
2. In modular DrugCounter, we create two dictionaries using drug names as the key. One is a dictionary of the set of the prescribers and another one is a dictionary of the total costs.
3. We use python standard library csv to read data from the file and add them into the dictionaries.
4. We sort the dictionary of the total costs in descending order.
5. Based on the descending order, we write the drug name, the number of the prescribers, and the total costs into the file using csv

Note: a prescriber is considered the same person if two lines share the same prescriber first and last names. Id is not considered.

# Run Instructions
Test OS: MAC OS
Python version: 3.6
List of Python standard libs used: sys, csv, unittest, filecmp

## General running
1. Put input data file under the direct /pharmacy_counting/input/ using file name "itcont.txt"
2. Run run.sh under the direct /pharmacy_counting/
3. The output file is under the direct /pharmacy_counting/output/top_cost_drug.txt

## Unit test
1. Run /pharmacy_counting/insight_testsuite/tests/my_own_test/src/test_drugcounter.py


# Questions?
Email me at xlx@bu.edu
