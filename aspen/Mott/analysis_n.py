import numpy, os

num_samples = 8
ec_range = numpy.arange(1.1, 1.41, 0.1)
nmean_list = []
nstd_ist = []
for ec in ec_range:
    path = f"{ec:.2f}"
    n_list = []
    os.chdir(path)
    with open("Gutz.log", "r") as f:
        for line in f:
            if "total number of electrons in simulation" in line:
                n = float(line.split(":")[1])
                n_list.append(n)
    if len(n_list) > num_samples:
        n_list = n_list[-num_samples:]
    nmean_list.append(numpy.mean(n_list))
    nstd_ist.append(numpy.std(n_list))
    os.chdir("..")

data = numpy.array([ec_range, nmean_list, nstd_ist]).T
numpy.savetxt("stat_n.dat", data, fmt="%.5f", delimiter="  ")
