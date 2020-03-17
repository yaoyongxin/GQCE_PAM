import numpy, os

num_samples = 8
ec_range = numpy.arange(1.0, 1.41, 0.1)
emean_list = []
estd_list = []
estd_ratio_list = []
for ec in ec_range:
    path = f"{ec:.2f}"
    e_list = []
    os.chdir(path)
    with open("Gutz.log", "r") as f:
        for line in f:
            if "e_total_model" in line:
                e = float(line.split("=")[1])
                # get rid of outliar
                if e > -1.3:
                    e_list.append(e)
    print(f"{path}: {len(e_list)}")
    if len(e_list) > num_samples:
        e_list = e_list[-num_samples:]
    emean_list.append(numpy.mean(e_list))
    # estd_list.append(numpy.std(e_list))
    estd_list.append((numpy.max(e_list)-numpy.min(e_list))/2)
    estd_ratio_list.append(estd_list[-1]/emean_list[-1])
    os.chdir("..")

data = numpy.array([ec_range, emean_list, estd_list, estd_ratio_list]).T
numpy.savetxt("stat_e.dat", data, fmt="%.5f", delimiter="  ")
