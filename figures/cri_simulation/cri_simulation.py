# PACKAGES
# =====================================================================

import luxpy

# Required by luxpy
import os
import warnings
from collections import OrderedDict as odict
from mpl_toolkits.mplot3d import Axes3D
import colorsys
import itertools
import copy
import time
import tkinter
import ctypes
import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import interpolate
from scipy.optimize import minimize
from scipy.spatial import cKDTree
from imageio import imsave

# =====================================================================
# =====================================================================
# CRI Illumination Simulation Script
# Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================
# =====================================================================

img_org_1 = os.getcwd()+'/files/input/vertumnus_original.jpg'
img_org_2 = os.getcwd()+'/files/input/strawberries_original.jpg'

outpath = os.getcwd()+'/files/output/'

# SPD data import from csv file
# =============================

# Get spline and new x-axis points
# ================================

# Set new x-axis points
# Not that a dictionary is unordered, so it does not make sense to get the last key
X = spd_raw.
x_max = spd_raw[-1]
print('x-max=', x_max)
x_min = spd_raw[0]
step_size = 1

x_start = int( math.ceil(x_min) )
x_stop = int( math.floor(x_max) )

print('x_min=', x_min, 'x_max=', x_max)
print('x_start=', x_start, 'x_stop=', x_stop)

X_new = list()
for i in range(x_start, x_stop):
    X_new.append(i)

# Calculate spline from original data points
#spd_spline = interpolate.splrep(X, Y)
#spd_ndarray_new = interpolate.splev(X_new, spd_spline)



# Rendering of image
# =============================


luxpy.toolboxes.hypspcim.render_image(img=img_org_1,
                                      spd=cri_low_1,
                                      out='img_ren',
                                      show=True,
                                      write_to_file=outpath+'img_rend_1')