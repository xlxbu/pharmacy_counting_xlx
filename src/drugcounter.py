#/usr/bin/python3

"""
:mod:'pharmacy_counting' -- pharmacy counting
=========================================================================================

.. module:: pharmacy_counting
    :platform: MAC OS
    :synopsis: count the # of prescribers and their cost of each drug
.. moduleauthor:: Liangxiao Xin

Requirements::
    1. You may need to use Python 3.6 to run this code.
    2. You will need to download a large dataset containing over 24 million records for the test.
       Download at https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing.
"""

import csv


class DrugCounter(object):
    """Pharmacy Counting for all the Drugs in the Document"""

    def __init__(self, readfrom=None, writeto=None):

        """
        Kwargs:
            readfrom (str): the file to read from
            writeto (str): the file to write to
        """

        self._readfrom = readfrom
        self._writeto = writeto

    def _read_csv_file(self):

        """
        Generator of the lines in the csv file
        """

        with open(self._readfrom, 'r') as read_csv:
            print("start to import data from %s" % (self._readfrom))
            reader = csv.reader(read_csv, delimiter=',', quotechar='"')
            header = True
            for line in reader:
                if header:
                    self._check_file_header(line) #check the format of the first line of the file
                    header = False
                    continue
                yield line
            print("finish importing data")

    def _check_file_header(self, input_header):
        """
        check the names of the columns in the input file
        if it is incorrect, throw a NameError

        :param input_header: (list) - list of the names of the columns of the input file
        """
        if input_header != ["id", "prescriber_last_name", "prescriber_first_name", "drug_name", "drug_cost"]:
            raise NameError('incorrect header format of the input file!')
        else:
            print("check input file header - ok")

    def _write_csv_file(self, output_header, contents):

        """
        write number of unique prescribers and the total cost of each drug into a csv file

        :param output_header: (list) - list of the names of the columns of the output file
        :param contents: (generator) - iterator of the number of prescribers and the total cost of each drug
        """

        with open(self._writeto, 'w') as write_csv:
            print("export result to %s" % (self._writeto))
            writer = csv.writer(write_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(output_header)
            for content in contents:
                writer.writerow(content)

    def _get_identifier(self, line):
        """
        get the identifier
        :param line: (list) - [id (str), prescriber_last_name (str), prescriber_first_name (str), drug_name (str), drug_cost (str)]
        :return: identifier (tuple) - (prescriber_last_name (str), prescriber_first_name (str))
        """
        return tuple(line[1:3])

    def _get_drug_name(self, line):
        """
        get the drug name
        :param line: (list) - [id (str), prescriber_last_name (str), prescriber_first_name (str), drug_name (str), drug_cost (str)]
        :return: drug name (str)
        """
        return line[3]

    def _get_drug_cost(self, line):
        """
        get the cost of the drug
        :param line: (list) - [id (str), prescriber_last_name (str), prescriber_first_name (str), drug_name (str), drug_cost (str)]
        :return: the cost of the drug (float)
        """
        return float(line[4])

    def _drug_cost_sort_desc(self, costs):
        """
        sort the drugs by the total costs in descending order
        :param costs: (dict) - {drug (str): cost (float)}
        :return: (generator) - (drug (str), cost (float))
        """
        for drug, cost in (sorted(costs.items(), key=lambda x: -x[1])):
            yield drug, cost

    def counter_of_drugs(self):
        """
        calculate the number of the prescribers and the total costs of all the drugs.
        """
        print("start to calculate the number of the prescriber and the total cost of each drug")
        prescribers = {}
        costs = {}
        for line in self._read_csv_file():
            identifiers = self._get_identifier(line)
            drug = self._get_drug_name(line)
            cost = self._get_drug_cost(line)

            prescribers.setdefault(drug, set())
            prescribers[drug].update({identifiers})

            costs.setdefault(drug, 0)
            costs[drug] += cost
        output_header = ['drug_name', 'num_prescriber', "total_cost"]
        contents = ([str(drug), str(len(prescribers[drug])), str(int(cost))] for drug, cost in self._drug_cost_sort_desc(costs))
        self._write_csv_file(output_header, contents)
        print("done!")