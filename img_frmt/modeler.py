#!/bin/env python

'''
This script aligns the numpy arrays, calculates reflection coefficients,
and models (convolves w a wavelet) them.
'''

# deps
import numpy as np
import glob
import scipy.misc
import bruges

# folder names
in1 = '../dat/fold_dyke_fault_model/*'
in2 = '../dat/fault_dyke_fold_model/*'
in3 = '../dat/gbasin_simplified_model/*'

out = '../dat/clean_imgs/'

# initialize
idx = 1
ricker = bruges.filters.ricker(duration=1, dt=0.002, f=35)

##########################################
import matplotlib.pyplot as plt
pic = np.load('../dat/gbasin_simplified_model/out_0037_xz400.npy')
pic = pic[:200, :200]
pic = np.transpose(pic)
pic = np.flip(pic, axis=0)
plt.imshow(pic)
plt.show()
rc = (pic[1:,:] - pic[:-1,:]) / (pic[1:,:] + pic[:-1,:])
synth = np.array([np.apply_along_axis(lambda t: np.convolve(t, ricker, mode='same'), axis=0, arr=trace) for trace in rc])
plt.imshow(synth)
plt.show()
#########################################


'''
# all files in first folder
for name in glob.glob(in1):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]
	
	# flip
	pic = np.transpose(pic)

	# calc refl coef
	rc = (pic[1:,:] - pic[:-1,:]) / (pic[1:,:] + pic[:-1,:])

	# write out
	#scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1

# all files in second folder
for name in glob.glob(in2):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]

	# calc refl coef
	rc = (pic[1:,:] - pic[:-1,:]) / (pic[1:,:] + pic[:-1,:])

	# write out
	#scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1


# all files in third folder
for name in glob.glob(in3):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]

	# flip
	pic = np.transpose(pic)
	pic = np.flip(pic, axis=0)

	# calc refl coef
	rc = (pic[1:,:] - pic[:-1,:]) / (pic[1:,:] + pic[:-1,:])

	# write out
	#scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1
'''

