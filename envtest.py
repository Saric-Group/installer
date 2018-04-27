from lammps import lammps
import argparse

import os.path

def runLammps(script):
    lmp = lammps()
    try:
        lmp.file(script)
    except:
        print("error")
    lmp.close()
    return

runLammps('lammpstest.in')