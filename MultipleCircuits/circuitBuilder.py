import sys
from elmer_circuitbuilder import *

def main(argv=None):
    output_file = "circuits.definitions_tmp"
    # ---------------------------------------------------------------------------
    c = number_of_circuits(2)
    # ---------------------------------------------------------------------------
    c[1].ref_node = 1
    I1 = I("IS1", 1, 2, 100.0)
    R1 = R("Rcl1", 2, 3, 200.0)
    FEM_1 = ElmerComponent("Coil1", 3, 4, 1, ["Coil1"])
    FEM_3 = ElmerComponent("Coil3", 4, 1, 3, ["Coil3"])
    FEM_1.is3D()
    FEM_1.stranded(1, 0)
    FEM_1.isClosed()
    FEM_3.is3D()
    FEM_3.stranded(1, 0)
    FEM_3.isClosed()
    c[1].components.append([I1, R1, FEM_1, FEM_3])
    # ---------------------------------------------------------------------------
    c[2].ref_node = 1
    I2 = I("IS2", 1, 2, 101.0)
    R2 = R("Rcl2", 2, 3, 201.0)
    FEM_2 = ElmerComponent("Coil2", 3, 1, 2, ["Coil2"])
    FEM_2.is3D()
    FEM_2.stranded(1, 0)
    FEM_2.isClosed()
    c[2].components.append([I2, R2, FEM_2])
    # ---------------------------------------------------------------------------
    generate_elmer_circuits(c, output_file)
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
