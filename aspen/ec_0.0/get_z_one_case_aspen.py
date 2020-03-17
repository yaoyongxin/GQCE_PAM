import numpy

fname = "./0.00/Gutz.log"


z_list = []
with open(fname, "r") as f:
    lread = False
    for line in f:
        if "imp=  1 eigen values of         z" in line:
            lread = True
        elif lread:
            z = float(line.split()[0])
            lread = False
        elif "maxerr = " in line:
            z_list.append(z)


numpy.savetxt("zlist.dat", z_list, fmt="%.4f")
