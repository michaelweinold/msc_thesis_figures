#!/usr/bin/env python

# PACKAGES
# =====================================================================

# Plotting
# =====================================================================
import matplotlib # For advanced plotting
import matplotlib.pyplot as plt # (subpackage has to be imported explicitly)
#import tikzplotlib # For export of figures to LaTeX pgfplot

# Data Science
# =====================================================================
import math
import numpy as np
import pandas as pd
import scipy
import scipy.interpolate as interpolate # (subpackage has to be imported explicitly)

# File Handling
# =====================================================================
import os # For I/O and path handling
import pathlib # For advanced path handling
import csv # For CSV file import and manipulation

# Colour Science
# =====================================================================
import colour
import colour.plotting # (subpackage has to be imported explicitly)

# Colour temperature script for producing LaTeX figures

# LaTeX
# =====================================================================
import tikzplotlib

__author__ = "Michael Weinold"
__copyright__ = "Copyright 2020, Michael Weinold"
__license__ = "???"
__version__ = "???"
__maintainer__ = "Michael Weinold"
__email__ = "mweinold@ethz.ch"
__status__ = "Testing"

colour.plotting.plot_visible_spectrum()

cctarray = colour.CCT_to_xy(5000, method='CIE Illuminant D Series')
