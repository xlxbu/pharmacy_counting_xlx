#/usr/bin/python3

"""
:main function of pharmacy counting
=========================================================================================
.. author:: Liangxiao Xin

Requirements::
    1. You may need to use Python 3.6 to run this code.
    2. You will need to download a large dataset containing over 24 million records for the test.
       Download at https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing.
"""

import sys
from drugcounter import DrugCounter


def main():
    if len(sys.argv) != 3:
        sys.exit("Not enough args")
    readfrom = str(sys.argv[1])
    writeto = str(sys.argv[2])
    p = DrugCounter(readfrom, writeto)
    p.counter_of_drugs()


if __name__=="__main__":
    main()