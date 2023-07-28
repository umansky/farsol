from runcase import *
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp
from uedge.rundt import *



#-short run to initialize everything
bbb.ftol=1e8; bbb.exmain()
bbb.ftol=1e-8

#-set up some initial state
bbb.ngs=1e14; bbb.ng=1e14
bbb.nis=1e20; bbb.ni=1e20 
bbb.ups=0.0;  bbb.up=0.0
bbb.tes=bbb.ev;   bbb.te=bbb.ev
bbb.tis=bbb.ev;   bbb.ti=bbb.ev


#-run to steady state
bbb.restart=1; bbb.ftol=1e-8;
bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
#rundt()
hdf5_restore("cmod_box3.h5")
bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()
mu.paws("Expecting a converged solution now")


filename='cmod_box3.h5'
print("Saving solution in ", filename)
hdf5_save(filename, addvarlist=['com.bphi', 'com.bpol', 'com.b', 'com.psi',
                                'com.iysptrx1','com.iysptrx2',
                                'com.ixpt1','com.ixpt2'
                                ])

exec(open("make_plots.py").read())
