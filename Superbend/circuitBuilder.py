import sys
from elmer_circuitbuilder import *

def main(argv=None):
    output_file = "circuits.definitions_tmp"
    # ---------------------------------------------------------------------------
    c = number_of_circuits(2)
    # ---------------------------------------------------------------------------
    c[1].ref_node = 1
    PS1 = I("IS1", 1, 2, 1.0)
    Rcl1 = R("Rcl1", 2, 3, 1.0)
    Rdp1 = R("Rdp1", 3, 1, 1.0)
    FEM_1 = ElmerComponent("Coil1", 3, 4, 1, ["Coil1"])
    # FEM_1 = ElmerComponent("Coil1", 3, 4, number of the Component field in sif == 1 associated to coil 1, ["Coil1"])
    FEM_1.is3D()
    FEM_1.stranded(1, 0)
    FEM_1.isClosed()
    FEM_2 = ElmerComponent("Coil2", 4, 1, 2, ["Coil2"])
    FEM_2.is3D()
    FEM_2.stranded(1, 0)
    FEM_2.isClosed()
    c[1].components.append([PS1, Rcl1, Rdp1, FEM_1, FEM_2])
    # ---------------------------------------------------------------------------
    c[2].ref_node = 1
    PS2 = I("IS2", 1, 2, 1.0)
    Rcl2 = R("Rcl2", 2, 3, 1.0)
    Rdp2 = R("Rdp2", 3, 1, 1.0)
    FEM_3 = ElmerComponent("Coil3", 3, 4, 3, ["Coil3"])
    FEM_3.is3D()
    FEM_3.stranded(1, 0)
    FEM_3.isClosed()
    FEM_4 = ElmerComponent("Coil4", 4, 1, 4, ["Coil4"])
    FEM_4.is3D()
    FEM_4.stranded(1, 0)
    FEM_4.isClosed()
    c[2].components.append([PS2, Rcl2, Rdp2, FEM_3, FEM_4])
    # ---------------------------------------------------------------------------
    generate_elmer_circuits(c, output_file)
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
