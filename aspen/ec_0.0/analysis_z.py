import numpy, os

num_samples = 20
ec_range = [0.0]
zmean_list = []
zstd_list = []
zstd_ratio_list = []
for ec in ec_range:
    path = f"{ec:.2f}"
    z_list = []
    os.chdir(path)
    lread = False
    with open("Gutz.log", "r") as f:
        for line in f:
            if "imp=  1 eigen values of         z" in line:
                lread = True
            else:
                if lread:
                    z = float(line.split()[0])
                    z_list.append(z)
                lread = False
    if len(z_list) > num_samples:
        z_list = z_list[-num_samples:]
    zmean_list.append(numpy.mean(z_list))
    zstd_list.append(numpy.std(z_list))
    zstd_ratio_list.append(zstd_list[-1]/zmean_list[-1])
    os.chdir("..")

data = numpy.array([ec_range, zmean_list, zstd_list, zstd_ratio_list]).T
numpy.savetxt("stat_z.dat", data, fmt="%.5f", delimiter="  ")
