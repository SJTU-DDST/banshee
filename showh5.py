import h5py # presents HDF5 files as numpy arrays
import numpy as np

f = h5py.File('zsim-ev.h5', 'r')
#print(f["stats"])
dset = f["stats"]["root"]
print(dset)
print(dset.shape)

# Phase count at end of simulation
endPhase = dset[-1]['phase']
print endPhase

# If your L2 has a single bank, this is all the L2 hits. Otherwise it's the
# hits of the first L2 bank
l2_0_hits = dset[-1]['l2'][0]['hGETS'] + dset[-1]['l2'][0]['hGETX']
print l2_0_hits

# Hits into all L2s
l2_hits = np.sum(dset[-1]['l2']['hGETS'] + dset[-1]['l2']['hGETX'])
print l2_hits

# Total number of instructions executed, counted by adding per-core counts
# (you could also look at procInstrs)
#totalInstrs = np.sum(dset[-1]['simpleCore']['instrs'])
#print totalInstrs

# You can also focus on one sample, or index over multiple steps, e.g.,
lastSample = dset[-1]
allHitsS = lastSample['l2']['hGETS']
firstL2HitsS = allHitsS[0]
print firstL2HitsS

# There is a certain slack in the positions of numeric and non-numeric indices,
# so the following are equivalent:
print dset[-1]['l2'][0]['hGETS']
#print dset[-1][0]['l2']['hGETS'] # can't do
print dset[-1]['l2']['hGETS'][0]
print dset['l2']['hGETS'][-1,0]
print dset['l2'][-1,0]['hGETS']
print dset['l2']['hGETS'][-1,0]

# However, you can't do things like dset[-1][0]['l2']['hGETS'], because the [0]
# indexes a specific element in array 'l2'. The rule of thumb seems to be that
# numeric indices can "flow up", i.e., you can index them later than you should.
# This introduces no ambiguities.

# Slicing works as in numpy, e.g.,
print dset['l2']['hGETS'] # a 2D array with samples*per-cache data
print dset['l2']['hGETS'][-1] # a 1D array with per-cache numbers, for the last sample
print dset['l2']['hGETS'][:,0] # 1D array with all samples, for the first L2 cache

print dset['l3']
