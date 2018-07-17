#/usr/bin/python3

"""
Unit test for the module DrugCounter.

author: Liangxiao Xin
"""

import unittest
import filecmp

from drugcounter import DrugCounter

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.readfrom = "../input/unittest_itcont.txt"
        self.writeto = "../output/unittest_top_cost_drug.txt"
        self.data = [["1000000001","Smith","James","AMBIEN","100"],
                            ["1000000002","Garcia","Maria","AMBIEN","200"],
                            ["1000000003","Johnson","James","CHLORPROMAZINE","1000"],
                            ["1000000004","Rodriguez","Maria","CHLORPROMAZINE","2000"],
                            ["1000000005","Smith","David","BENZTROPINE MESYLATE","1500"]]
        self.data_header = ["id", "prescriber_last_name", "prescriber_first_name", "drug_name", "drug_cost"]
        self.result_header = ["drug_name","num_prescriber","total_cost"]
        self.result_data = (line for line in [["CHLORPROMAZINE","2","3000"],
                        ["BENZTROPINE MESYLATE","1","1500"],
                        ["AMBIEN","2","300"]])
        self.dc = DrugCounter(self.readfrom, self.writeto)

    def test_read_csv_file(self):
        result = []
        expected = self.data
        for line in self.dc._read_csv_file():
            result.append(line)
        self.assertEqual(result, expected)

    def test_check_file_header(self):
        header = self.data_header
        self.assertRaises(NameError, self.dc._check_file_header(header))

    def test_write_csv_file(self):
        self.dc._write_csv_file(self.result_header, self.result_data)
        self.assertTrue(filecmp.cmp(self.writeto, "../output/top_cost_drug_ref.txt"))

    def test_get_identifier(self):
        result = self.dc._get_identifier(self.data[0])
        expected = ("Smith","James")
        self.assertEqual(result, expected)

    def test_get_drug_name(self):
        result = self.dc._get_drug_name(self.data[0])
        expected = "AMBIEN"
        self.assertEqual(result, expected)

    def test_get_drug_cost(self):
        result = self.dc._get_drug_cost(self.data[0])
        expected = 100.0
        self.assertEqual(result, expected)

    def test_drug_cost_sort_desc(self):
        result = []
        expected = [("CHLORPROMAZINE", 3000), ("BENZTROPINE MESYLATE",1500), ("AMBIEN",300)]
        cost_dic = {"CHLORPROMAZINE": 3000, "BENZTROPINE MESYLATE":1500, "AMBIEN":300}
        for drug, cost in self.dc._drug_cost_sort_desc(cost_dic):
            result.append((drug, cost))
        self.assertEqual(result, expected)

    def test_counter_of_drugs(self):
        self.dc.counter_of_drugs()
        self.assertTrue(filecmp.cmp(self.writeto, "../output/top_cost_drug_ref.txt"))

    def tearDown(self):
        del self.readfrom
        del self.writeto
        del self.data
        del self.data_header
        del self.result_data
        del self.result_header
        del self.dc


if __name__ == '__main__':
    unittest.main()
