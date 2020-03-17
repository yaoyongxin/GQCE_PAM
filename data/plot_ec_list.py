import numpy
import matplotlib.pyplot as plt

# ec boundary for u=2
# Kondo insulator-metal transition
ec_im = 0.07
# metal-mott insulator transition
ec_mott = 1.08
err = 0.05
nmott = 5

data_hf = numpy.loadtxt("ec_data_hf.dat").T
data_sv = numpy.loadtxt("ec_data_statevec.dat").T
data_as = numpy.loadtxt("ec_data_aspen.dat").T

cmap = plt.get_cmap('Blues')
fig = plt.figure(figsize=(7.5, 3))

ax1 = plt.subplot(131)
# ax1.text(0.25, 0.85, "(a)", transform=ax1.transAxes)
plt.plot(data_sv[0], data_sv[1], "-")
plt.errorbar(data_as[0], data_as[1],
        yerr=data_as[2][:len(data_as[0])-nmott].tolist()+
        [.005]*nmott,
        marker="o", fillstyle='none')
plt.plot(data_hf[0], data_hf[1])

ax1.axvspan(-0.02, ec_im, facecolor=cmap(0.1), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax1.axvspan(ec_im, ec_mott, facecolor=cmap(0.6), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax1.axvspan(ec_mott, 1.42, facecolor=cmap(0.4), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
plt.xlim(-0.02, 1.42)
plt.xlabel("$\epsilon_c$")
plt.ylabel("E")

ax2 = plt.subplot(132, sharex=ax1)
# ax2.text(0.1, 0.85, "(b)", transform=ax2.transAxes)
plt.plot(data_sv[0], data_sv[3], "-", label="Simulation")
plt.errorbar(data_as[0], data_as[4],
        yerr=data_as[7][:len(data_as[0])-nmott].tolist()+
        [.003]*nmott,
        marker="o", fillstyle='none', label="Device(Rigetti)")
plt.plot(data_hf[0], data_hf[3], label="HF")
plt.ylabel("Z")
plt.xlabel("$\epsilon_c$")
handles, labels = ax2.get_legend_handles_labels()
handles.insert(1, handles[-1])
handles.pop()
labels.insert(1, labels[-1])
labels.pop()
plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.0, 0.95),
        fontsize="small")

ax2.axvspan(-0.02, ec_im, facecolor=cmap(0.1), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax2.axvspan(ec_im, ec_mott, facecolor=cmap(0.6), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax2.axvspan(ec_mott, 1.42, facecolor=cmap(0.4), zorder=-1,
        alpha=0.2, ls='--', ec='blue')

ax3 = plt.subplot(133, sharex=ax1)
# ax3.text(0.5, 0.85, "(c)", transform=ax3.transAxes)
plt.plot(data_sv[0], data_sv[2], "-")
plt.errorbar(data_as[0], data_as[5],
        yerr=data_as[6][:len(data_as[0])-nmott].tolist()+
        [.005]*nmott,
        marker="o", fillstyle='none')
plt.plot(data_hf[0], data_hf[2])
ax3.vlines(0.26, 0.95, 2.05, ls=":", color="grey")
ax3.set_ylim(0.95, 2.05)
plt.ylabel("n")
plt.xlabel("$\epsilon_c$")

ax3.axvspan(-0.02, ec_im, facecolor=cmap(0.1), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax3.axvspan(ec_im, ec_mott, facecolor=cmap(0.6), zorder=-1,
        alpha=0.2, ls='--', ec='blue')
ax3.axvspan(ec_mott, 1.42, facecolor=cmap(0.4), zorder=-1,
        alpha=0.2, ls='--', ec='blue')

fig.tight_layout()

plt.show()
