import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

data = numpy.loadtxt("dos_0813.dat").T
xmin, xmax = -2, 2.5

cmap = plt.get_cmap('Blues')
fig = plt.figure(figsize=(7.5, 3))

ax1 = plt.subplot(131)
plt.plot(data[0], data[1], ".")
plt.plot(data[0], data[2], "-")
# plt.plot(data[0], data[6], "--", color="grey")
plt.axvline(0, ls=":", c="g")
ax1.axvspan(xmin, xmax, facecolor=cmap(0.1), zorder=-1,
        alpha=0.2, ec='blue')
plt.xlim(xmin, xmax)
plt.xticks([-2,-1,0,1,2])
plt.ylim(0, 9.8)
plt.xlabel("E")
plt.ylabel("Coherent DOS (states/site)")
axins = inset_axes(ax1, width="60%", height="30%", loc="upper center")
plt.plot(data[0], data[1], ".")
plt.plot(data[0], data[2], "-")
plt.plot(data[0], data[6], "--", color="grey", label="HF")
plt.axvline(0, ls=":", c="g")
plt.xlim(-0.22, 0.22)
plt.legend(bbox_to_anchor=(1.25, -0.4))

ax2 = plt.subplot(132, sharex=ax1, sharey=ax1)
plt.plot(data[0], data[3], ".")
plt.plot(data[0], data[4], "-")
# plt.plot(data[0], data[7], "--", color="grey")
plt.axvline(0, ls=":", c="g")

plt.xlabel("E")
#plt.legend(loc='upper right', bbox_to_anchor=(1, 0.96), fontsize="small")
ax2.axvspan(xmin, xmax, facecolor=cmap(0.6), zorder=-1,
        alpha=0.2, ec='blue')

ax3 = plt.subplot(133, sharex=ax1, sharey=ax1)
plt.plot(data[0], data[5], ".", label="Simulation")
plt.plot(data[0], data[5], "-", label="Device(Rigetti)")
# plt.plot(data[0], data[8], "--", color="grey", label="HF")
plt.axvline(0, ls=":", c="g")
plt.xlabel("E")
ax3.axvspan(xmin, xmax, facecolor=cmap(0.4), zorder=-1,
        alpha=0.2, ec='blue')
plt.legend(loc='upper left')

fig.tight_layout()

plt.show()
