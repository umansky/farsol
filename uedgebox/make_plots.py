mp.plotvar(bbb.te/bbb.ev, iso=False, title="Te @ steady state", label='eV', yinv=True)
#plt.savefig('te.pdf')

mp.plotvar(bbb.ni[:,:,0], iso=False, title="Ni @ steady state", label='m-3', yinv=True)
#plt.savefig('ni.pdf')

mp.plotvar(bbb.ni[:,:,1], iso=False, title="Nn @ steady state", label='m-3', yinv=True)
#plt.savefig('nn.pdf')

mp.plotvar(bbb.up[:,:,0], iso=False, title="Up @ steady state", label='m/s', yinv=True)
#plt.savefig('up.pdf')
