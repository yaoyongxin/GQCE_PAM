import numpy
import matplotlib.pyplot as plt


data_sv = numpy.loadtxt("iter_statevec.dat").T
data_as = numpy.loadtxt("iter_aspen.dat").T

fig = plt.figure(figsize=(7.5, 3))

ax1 = plt.subplot(131)
ax1.text(0.05, 0.9, "(a)", transform=ax1.transAxes)
plt.plot(range(data_sv.shape[1]), data_sv[0])
plt.plot(range(data_as.shape[1]), data_as[0], "o", fillstyle='none')
plt.ylabel("E")
plt.xlabel("Iteration")

ax2 = plt.subplot(132, sharex=ax1)
ax2.text(0.25, 0.9, "(b)", transform=ax2.transAxes)
plt.plot(range(data_sv.shape[1]), data_sv[2], label="Simulation")
plt.plot(range(data_as.shape[1]), data_as[2], "o", fillstyle='none',
        label="Device(Rigetti)")
ax2.legend(loc="upper right", fontsize="small", bbox_to_anchor=(1.0, 0.76))
plt.ylabel("Z")
plt.xlabel("Iteration")

ax3 = plt.subplot(133, sharex=ax1)
ax3.text(0.25, 0.9, "(c)", transform=ax3.transAxes)
plt.ylim(3.e-4, 2)
plt.yscale('log')
plt.plot(range(data_sv.shape[1]), data_sv[1], label="Simulation")
plt.plot(range(data_as.shape[1]), data_as[1], "o", fillstyle='none',
        label="Device(Rigetti)")
plt.ylabel("Max. Error")
plt.xlabel("Iteration")

fig.tight_layout()

plt.show()
