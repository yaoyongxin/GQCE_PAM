import numpy, os, h5py, shutil
# from pygrisb.model.almcubic_c1 import gutz_model_setup
from pygrisb.model.almbethlattice_c1 import gutz_model_setup
from pygrisb.run.cygutz import driver_cygutz, get_cygtail
from pygrisb.gsolver.bank import qc_bank


z_list = []
eps_c_list = numpy.arange(0.0, 1.5, 0.1)

path_old = None
with open("z_epsc_1.txt", "w") as frec:
    for eps_c in eps_c_list:
        qc_bank.xopt_list.append(0)
        path = f"{eps_c:.2f}"
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)

        gutz_model_setup(
                eps_c=eps_c,
                dtype=numpy.float,
                u=2.0,
                iembeddiag=-2,
                )

        if path_old is not None:
            shutil.copy(f"../{path_old}/GLog.h5", "./")
        path_old = path

        driver_cygutz(path=os.environ['WIEN_GUTZ_ROOT'],
                cygtail=get_cygtail(),
                rmethod="hybr",
                tol=1e-6,  # norm
                )
        with h5py.File("GLog.h5", "r") as f:
            r = f["/impurity_0/R"][::2,::2].T
            nelect = f["/"].attrs["nelectrons"]
            emodel = f["/"].attrs["etot_model"]
        with h5py.File("GIter.h5", "r") as f:
            err = f["/v_err"][()]
        maxerr = numpy.max(numpy.abs(err))
        shutil.copyfile("GLog.h5", f"GLog_{eps_c:.2f}.h5")
        z = r.T.conj().dot(r)
        w, v = numpy.linalg.eigh(z)
        frec.write(f"{eps_c:.4f} {emodel:.4f} {nelect:.4f} {w[0]:.4f}" +\
                f" {v[:,0]} {maxerr:.2e}\n")
        frec.flush()
        qc_bank.save_xopts()
        os.chdir("..")
