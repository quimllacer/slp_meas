# ============================================================================
# Name        : cpx400sp_example.py
# Author      : Julian Stiefel (jstiefel@ethz.ch)
# Version     : 1.0.0
# Created on  : 25.08.2020
# Copyright   :
# Description : This is an example script on how to control the Aim TTi
#               CPX400SP.
# ============================================================================

#!/usr/bin/env python3

import sys
import time

sys.path.append(".")
from cpx400sp import CPX400SP

def main():
    #Set variables
    voltage = 0


    #Set parameters    
    cpx = CPX400SP('192.168.1.131', 9221)
    print(cpx.get_identification())
    current = 20
    cpx.set_current(current)
    cpx.set_voltage(voltage)
    cpx.set_output(0)

    del cpx

if __name__ == "__main__":
    main()

#For safety, when script is exited, voltage and current should turn to 0.
